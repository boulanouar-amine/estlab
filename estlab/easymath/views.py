from django.shortcuts import render
import numpy as np
import array_to_latex as a2l
import re

# general functions
mat = np.zeros((2, 1))

def format_all(chaine):
    global mat
    mat = chaine
    if type(chaine) is np.matrix:
        return "$$" + str(a2l.to_ltx(chaine, print_out=False, arraytype="pmatrix", frmt="{:.2f}", mathform=True)) + "$$"
    elif type(chaine) is str:
        return chaine
    else:
        return str("$$" + "{:.2f}".format(chaine) + "$$")


def extract(command, ele):

    chaine = command.replace(ele, "").replace("(", "").replace(")", "")
    if not (re.search("matrix_calculator", command) or re.search("vector_difference", command)) and re.search("]", chaine):
        chaine = np.matrix(chaine)

    return chaine



# matrix functions



def trace(chaine):
    chaine = np.trace(chaine)
    return chaine


def determinant(chaine):
    chaine = np.linalg.det(chaine)
    return chaine


def inverse_matrix(chaine):
    chaine = np.linalg.inv(chaine)
    return chaine


def transpose_matrix(chaine):
    chaine = chaine.transpose()
    return chaine

def matrix_calculator(chaine):
    op = {"/": np.divide, "\+": np.add, "\*": np.multiply, "\-": np.subtract}
    for ele in op:
        if re.search(ele, chaine):
            chaine = chaine.split(ele.strip("\\"))
            a = np.matrix(chaine[0])  # if there is another element redo
            b = np.matrix(chaine[1])
            chaine = op[ele](a, b)
            return chaine


# vectores

def valeur_propre(chaine):
    chaine = np.linalg.eigvals(chaine)
    chaine = np.sort(chaine)
    return chaine


def vector_difference(chaine):
    chaine = chaine.replace(";", "-")
    chaine = matrix_calculator(chaine)
    return chaine


# statistique

def calculate(chaine):
    chaine = eval(chaine)
    return chaine


def average(chaine):
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
        return "le nombre " + str(num)  +" est parfait"
    else:
        return "le nombre " + str(num)  +" n'est pas parfait"


def nombre_premier(chaine):
    num = int(chaine)

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "le nombre " + str(num) + " n'est pas premier"
    return "le nombre " + str(num) + " est premier"


def intervalle_parfait(chaine):
    chaine = chaine.split(",")
    start  = int(chaine[0])
    end    = int(chaine[1])
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
# views code



def doc(request):
    return render(request, 'documentation.html', {'output': "bonjour"})


def run(request):
    global mat
    res = "bonjour veuiller entrer help pour la syntax"
    try:

        if request.GET.get('average') == 'average':
            res = str("$$" + "{:.2f}".format(average(mat)) + "$$")

        if request.GET.get('transpose') == 'transpose':
            res = format_all(transpose_matrix(mat))

        if request.GET.get('inverse') == 'inverse':
            res = format_all(inverse_matrix(mat))

        if request.method == 'POST':

            command = request.POST["cal"]

            commands = ("calculate", "matrix_calculator", "inverse_matrix", "transpose_matrix", "determinant",
                            "trace", "vector_difference", "average", "valeur_propre","nombre_parfait","intervalle_parfait","nombre_premier")  # can add new functions here

            res = ''.join([eval("format_all(" + ele + "(extract(command,ele)))") for ele in commands if re.search(ele, command)])

    except (IndexError, ZeroDivisionError):
        res = "division par 0"

    except np.linalg.LinAlgError:
        res = "la matrice doit etre une matrice carre"

    except:

        res = "Veuiller entrer une formule valid"

    return render(request, 'index.html', {'output': str(res),'mat': str(mat)})



