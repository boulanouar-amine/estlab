import numpy as np
import re
import array_to_latex as a2l

'''

 def clean_res(chaine):
                return str(chaine).replace('[', '').replace(']', '').replace('\'', '')



def del_brackets(chaine):
    return  str(chaine).replace('[','').replace(']','').replace('[[','').replace(']]','')

def matrix_calculator(chaine):
    chaine = chaine.replace("matrix_calculator(", "")
    chaine = chaine.replace(")", "")

    return split_matrix(chaine)


def split_matrix(chaine):

    if re.search("/", chaine):
        chaine = chaine.split("/")
        a = np.matrix(chaine[0])
        b = np.matrix(chaine[1])

        return np.divide(a, b)

    if re.search("\-", chaine):
        chaine = chaine.split("-")

        a = np.matrix(chaine[0])
        b = np.matrix(chaine[1])

        return np.subtract(a, b)

    if re.search("\+", chaine):
        chaine = chaine.split("+")

        a = np.matrix(chaine[0])
        b = np.matrix(chaine[1])

        return np.add(a, b)

    if re.search("\*", chaine):
        chaine = chaine.split("*")

        a = np.matrix(chaine[0])
        b = np.matrix(chaine[1])
        return np.multiply(a, b)


def format_matrix(chaine,num):
    begin = '$$\\begin{pmatrix}'
    data ="\\\\".join(str(i) for i in chaine)
    end = '\end{pmatrix}$$'
    return begin + del_brackets(data) + end
    
    return "$$" + str(a2l.to_ltx(chaine, arraytype='pmatrix', frmt='{:.'+str(num)+'f}', )) + "$$"


def inverse(chaine):
    chaine = chaine.replace("inverse(", "").replace(")", "")
    x = np.matrix(chaine)
    x = np.linalg.inv(x)
    return format_matrix(x,5)


def determinant(chaine):
    chaine = chaine.replace("determinant(", "").replace(")", "")
    x = np.matrix(chaine)
    print(np.linalg.det(x))
    return np.linalg.det(x)




res = matrix_calculator('matrix_calculator([1,2];[10,10]+[3,1];[2,4])')

'
           if re.search("inverse", command):
               res = inverse(command)
               return render(request, 'index.html', {'output': str(res)})

           if re.search("determinant", command):
               res = determinant(command)
               return render(request, 'index.html', {'output': str(res)})

           if re.search("matrix_calculator", command):
               res = matrix_calculator(command)
               return render(request, 'index.html', {'output': str(res)})

            
res1 =('inverse([6, 1, 1];[4, -2, 5])')

res2 = ('determinant([3,1,0];[3,2,1];[4,1,7]),')
determinant(res2)


def format_number(chaine):
    return str("$$" + "{:.2f}".format(chaine) + "$$")


def vecteur_propre(chaine):
    chaine = np.matrix(chaine)
    x = np.linalg.eigvals(chaine)
    print(np.sort(x))
    return x

def format_matrix(chaine, num=0, arrtype="pmatrix"):
    return "$$" + str(
        a2l.to_ltx(chaine, arraytype=arrtype, frmt='{:.' + str(num) + 'f}', mathform=True)) + "$$"



res3='[6,1,1];[4,-2,5];[2,8,7]'

vecteur_propre(res3)


def calcule_parfait(chaine):
    n = int(chaine)
    S = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            S = S + i
    return bool(S == n)


def parfait(chaine):
    if calcule_parfait(chaine):
        return "ce nombrer est parfait"
    else:
        return "ce nombrer n'est pas parfait"


def intervalle_premier(chaine):
    chaine = chaine.split(",")
    start  = int(chaine[0])
    end    = int(chaine[1])
    res = []
    for num in range(start, end + 1):
        sum = 0

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print( "le nombre " + str(num) + " n'est pas premier")
        print( "le nombre " + str(num) + " est premier")

    if num == sum:
           res.append(sum)
    res = np.asmatrix(res)
    return format_matrix(res)
# views code

intervalle_premier(1,29)

[eval("format_all(" + ele + "(extract(command,ele)))") for ele in commands if re.search(ele, command)]'''





import csv
'''
from sympy import *
from sympy.interactive import printing # Pour avoir des belles sorties ...
printing.init_printing(use_latex=True) # ... en LaTeX
from IPython.display import display



def primitives():
    x = symbols('x')  # utiliser la variable x pour mes calculs.
    F = integrate(sqrt(x+2),x)
    display(F)


def integrale_intervalle():
    x = symbols('x')  # utiliser la variable x pour mes calculs.
    y = 5 * x
    F=integrate(y, (x, 1, 3)) #integrale de y dan l intervale {1 , 3 }
    display(F)

'''
from django.shortcuts import render
import numpy as np
import array_to_latex as a2l
import re

import sympy as sp


mat = "4"
def derivée(mat):

    x = sp.symbols('x')
    y=mat
    F=sp.diff(y,x)

    return F





print(derivée(mat))
