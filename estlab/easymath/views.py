from django.shortcuts import render
import numpy as np
import array_to_latex as a2l
import re


# general functions

def format_number(chaine):
    return str("$$" + "{:.2f}".format(chaine) + "$$")


def extract(command, ele):

    chaine = command.replace(ele, "").replace("(", "").replace(")", "")
    if not re.search("matrix_calculator", command) and re.search("]", chaine):
        chaine = np.matrix(chaine)

    return chaine

def calculate(chaine):
    return format_number(eval(chaine))


# matrix functions

def trace(chaine):
    return format_number(np.trace(chaine))


def determinant(chaine):
    chaine = np.linalg.det(chaine)
    return format_number(chaine)  # return 2 number after  comma


def format_matrix(chaine, num=0, arrtype="pmatrix"):
    return "$$" + str(
        a2l.to_ltx(chaine, print_out=False, arraytype=arrtype, frmt='{:.' + str(num) + 'f}', mathform=True)) + "$$"


def inverse_matrix(chaine):
    chaine = np.linalg.inv(chaine)
    return format_matrix(chaine, 5)

def transpose_matrix(chaine):
    return format_matrix(chaine.transpose(), 5)


def matrix_calculator(chaine, arrtype="pmatrix"):
    op = {"/": np.divide, "\+": np.add, "\*": np.multiply, "\-": np.subtract}
    for ele in op:
        if re.search(ele, chaine):
            chaine = chaine.split(ele.strip("\\"))
            a = np.matrix(chaine[0])  # if there is another element redo
            b = np.matrix(chaine[1])
            chaine = op[ele](a, b)
            return format_matrix(chaine, 0, arrtype)


# vectores

def vector_difference(chaine):
    return matrix_calculator(chaine.replace(";", "-"), "bmatrix")


#statistique

def average(chaine):
    return format_number(np.average(chaine))

# views code

def doc(request):
    return render(request, 'documentation.html', {'output': "bonjour"})


def run(request):
    res = "bonjour veuiller entrer help pour la syntax"

    if request.method == 'POST':
        command = request.POST["cal"]

        try:

            commands = ("calculate","matrix_calculator","inverse_matrix","transpose_matrix","determinant",
                        "trace","vector_difference","average")  # can add new functions here

            # or i can use eval(ele+"(command)"),commands[ele](extract(command,ele) with dictionarry
            res = ''.join([eval(ele + "(extract(command,ele))") for ele in commands if re.search(ele, command)])

        except (IndexError, ZeroDivisionError):
            res = "division par 0"

        except np.linalg.LinAlgError:
            res = "la matrice doit etre une matrice carre"

        except:

            res = "Veuiller entrer une formule valid"

    return render(request, 'index.html', {'output': str(res)})
