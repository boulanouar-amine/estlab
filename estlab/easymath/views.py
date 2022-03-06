import numpy as np
from django.shortcuts import render
from pylab import *
import array_to_latex as a2l

history = ""

def del_brackets(chaine):
    return  str(chaine).replace('[','').replace(']','').replace('[[','').replace(']]','')

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

def format_matrix(chaine):
    """begin = '$$\\begin{pmatrix}'
    data ="\\\\".join(str(i) for i in chaine)
    end = '\end{pmatrix}$$'
    return begin + del_brackets(data) + end
    """
    return "$$"+str(a2l.to_ltx(chaine , print_out=False , arraytype = 'pmatrix' , frmt = '{:.3f}',) )+"$$"

def inverse_matrix(chaine):
    chaine = chaine.replace("inverse_matrix(", "").replace(")", "")
    x = np.matrix(chaine)
    x = np.linalg.inv(x)
    return format_matrix(x)

def matrix_calculator(chaine):
    chaine = chaine.replace("matrix_calculator(", "").replace(")", "")
    chaine = split_matrix(chaine)

    return format_matrix(chaine)


def doc(request):
    return render(request, 'documentation.html', {'output': "bonjour"})

def run(request):

    global history
    res = "bonjour veuiller entrer help pour la syntax"

    if request.method == 'POST':
        command = request.POST["cal"]

        try:

            if re.search("inverse_matrix", command):
                res = inverse_matrix(command)
                return render(request, 'index.html', {'output': str(res)})

            if re.search("matrix_calculator",command):

                res = matrix_calculator(command)
                return render(request, 'index.html', {'output': str(res)})


            if command == "help" or command == "help()":
                command = ""
                res = "vous pouver voir la documentation dans /documentation"
                return render(request, 'index.html', {'output': str(res)})

            if command == "quit" or command == "exit":
                command = ""
                pass

            else:
                res = eval(command)
                history = str(res) + "\n" + history

        except (IndexError, ZeroDivisionError):
            res = "division par 0"
        except:

            res = "Veuiller entrer une formule valid"

    return render(request, 'index.html', {'output': str(res), 'history': str(history)})
