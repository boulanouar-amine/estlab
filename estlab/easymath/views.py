import re

import array_to_latex as a2l
import numpy as np
import sympy as sp
import pandas as pd
import csv,os
from django.core.files.storage import default_storage, FileSystemStorage
from django.shortcuts import render


commands = ("calculate", "inverse", "transposée", "determinant",
            "trace", "vector_difference", "moyenne", "valeur propre", "nombre_parfait",
            "intervalle_parfait", "nombre_premier", "derivée", "primitive", "integrale")

mat = np.zeros((1, 1))
premier=""
parfait=""
uploaded_file_url=""

# la premier fonction qui contient le get

def moy(list):
    s=0
    n=len(list)
    for k in range(0,n):
        s=s+int(list[k])
    #print('s=',s,'n=',n,'moyenne=',s/n)
    return s/n



def run(request):
    global mat, commands,premier,parfait,uploaded_file_url,moy,med
    res = ""
    try:

        if request.method == 'GET':

            if request.GET.get("upload") == "upload+file":
                res = format_all(0)

            if request.GET.get("matrice") == "matrice":
                res = format_all(0)
            else:
                res = ''.join([eval("format_all(" + ele.replace(" ", "_") + "(mat))") for ele in commands if
                               str(request.GET.get(ele)) == str(ele)])


        elif request.method == 'POST':

            try :

                myfile = request.FILES['inp']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                file_path = os.path.join('media/', filename)

                df = pd.read_csv(file_path)
                moy = print(df.mean())
                med =  print(df.median())


            except:

                try :
                    premier = str(nombre_premier(eval(request.POST["nbrP"])))

                except:
                    try:
                        parfait = str(nombre_parfait(eval(request.POST["nbrParfait"])))
                    except:
                        command = request.POST["cal"]

                        if re.search("!", command):
                            command = command.replace("!", "")
                            res = np.math.factorial(eval(command))
                            return render(request, 'index.html',
                                          {'output': str(res), 'mat': str(mat), 'premier': str(premier),
                                           'parfait': str(parfait), 'uploaded_file_url': uploaded_file_url})

                        if re.search("x", command):

                            if request.GET.get("derivée") == "derivée":
                                res = str(derivée(command))

                            if request.GET.get("primitive") == "primitive":
                                res = str(primitive(command))

                            if request.GET.get("integrale") == "integrale":
                                res = str(integrale(command))


                        else:
                            res = format_all(calculate((command)))

    # res = ''.join([eval("str(" + ele + "(command))") for ele in commands if str(request.GET.get(ele)) == str(ele)])
    # res = ''.join([eval("format_all(" + ele + "(extract(command,ele)))") for ele in commands if re.search(ele, command)])

    except (IndexError, ZeroDivisionError):
        res = "division par 0"

    except np.linalg.LinAlgError:

        res = "la matrice n'est pas une matrice carrée"



    except ValueError:
        res = "veuillez entrer une expression"

    except:

        res = ""

    return render(request, 'index.html', {'output': str(res), 'mat': str(mat),'premier':str(premier),'parfait':str(parfait), 'uploaded_file_url': uploaded_file_url})


def Home(request):
    return render(request, 'Home.html')


def Matrice(request):
    return render(request, 'Matrice.html')


def Contact(request):
    return render(request, 'Contact.html')


def Services(request):
    return render(request, 'Services.html')


def statistique(request):
    return render(request, 'statistique.html')


def Fraction(request):
    return render(request, 'Fraction.html')


def NombreAmi(request):
    return render(request, 'NombreAmi.html')


def NombreAmi(request):
    return render(request, 'NombreAmi.html')


def NombreParfait(request):
    return render(request, 'NombreParfait.html')


def NombrePremier(request):
    return render(request, 'NombrePremier.html')


def Syntax(request):
    return render(request, 'Syntax.html')


def Probabilite(request):
    return render(request, 'Probabilite.html')


def calculate(chaine):
    global mat
    if re.search("]", chaine):
        chaine = matrix_calculator(chaine)

    else:
        chaine = eval(chaine)
        mat = chaine
    return chaine


# general functions

def format_all(chaine):
    global mat
    if type(chaine) is np.matrix:
        mat = chaine
        return "$$" + str(a2l.to_ltx(chaine, print_out=False, arraytype="pmatrix", frmt="{:.2f}", mathform=True)) + "$$"

    elif type(chaine) is str:
        return chaine

    elif type(chaine) is sp.latex:
        return str("$$" + chaine + "$$")

    else:
        return str("$$" + "{:.2f}".format(chaine) + "$$")


"""
def extract(command, ele):

    chaine = command.replace(ele, "").replace("(", "").replace(")", "")
    if not (re.search("matrix_calculator", command) or re.search("vector_difference", command)) and re.search("]", chaine):
        chaine = np.matrix(chaine)

    return chaine
"""


# matrix functions

def trace(chaine):
    return  np.trace(chaine)


def determinant(chaine):
    return  np.linalg.det(chaine)


def inverse(chaine):
    chaine = np.linalg.inv(chaine)
    return chaine


def transposée(chaine):
    chaine = chaine.transpose()
    return chaine


def matrix_calculator(chaine):
    op = {"/": np.divide, "\+": np.add, "\*": np.multiply, "\-": np.subtract}
    for ele in op:
        if re.search(ele, chaine):
            chaine = chaine.split(ele.strip("\\"))
            a = np.matrix(chaine[0])
            b = np.matrix(chaine[1])
            chaine = op[ele](a, b)

            return chaine
    else:
        chaine = np.matrix(chaine)
        return chaine


# vectores

def valeur_propre(chaine):
    chaine = np.linalg.eigvals(chaine)
    chaine = np.sort(chaine)
    chaine = np.matrix(chaine)
    return chaine


def vector_difference(chaine):
    chaine = chaine.replace(";", "-")
    chaine = matrix_calculator(chaine)
    return chaine


# statistique


def moyenne(chaine):
    chaine = np.average(chaine)
    return chaine


# traitement des nombre


def nombre_parfait(chaine):
    num = int(chaine)
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    if num == sum:
        return "le nombre " + str(num) + " est parfait"
    else:
        return "le nombre " + str(num) + " n'est pas parfait"


def nombre_premier(chaine):
    num = int(chaine)

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "le nombre " + str(num) + " n'est pas premier"
    return "le nombre " + str(num) + " est premier"


def intervalle_parfait(chaine):
    chaine = chaine.split(",")
    start = int(chaine[0])
    end = int(chaine[1])
    res = []
    for num in range(start, end + 1):
        sum = 0

        for i in range(1, num):
            if num % i == 0:
                sum += i

        if num == sum:
            res.append(sum)
    res = np.asmatrix(res)
    return res


# derivee

def derivée(mat):
    x = sp.symbols('x')
    y = mat
    F = sp.diff(y, x)

    return str("$$" + sp.latex(F) + "$$")


# primitives

def primitive(mat):
    x = sp.symbols('x')
    F = sp.integrate(mat)
    return str("$$" + sp.latex(F) + "$$")


# integrale

def integrale(mat):
    mat = mat.split(",")
    x = sp.symbols('x')  # utiliser la variable x pour mes calculs.
    y = mat[0]
    F = sp.integrate(y, (x, mat[1], mat[2]))  # integrale de y dan l intervale {1 , 3 }
    return str("$$" + sp.latex(F) + "$$")

# <!--{% if request.get_full_path == "/?derivée=derivée" or request.get_full_path == "/index?primitive=primitive"  or request.get_full_path == "/index?clr=clr"  or request.get_full_path == "/index?%2B=%2B"  or request.get_full_path == "/index?-=-"  or request.get_full_path == "/index?x=x"  or request.get_full_path == "/index?%2F=%2F"   or request.get_full_path == "/index?%5E=%5E"  or request.get_full_path == "/index?ln=ln"  or  request.get_full_path == "/index?e=e"  or request.get_full_path == "/index?%28=%28"  or request.get_full_path == "/index?%29=%29" %}-->  <form method='get'>
