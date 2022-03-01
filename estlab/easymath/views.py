import numpy as np
from django.shortcuts import render
from pylab import *

history = ""

def del_double_bracket(chaine):
    chaine = chaine.replace("[[", "")
    chaine = chaine.replace("]]", "")
    return chaine

def del_simple_bracket(chaine):
    if chaine[0] == '[' and chaine[len(chaine) - 1] == ']':
        chaine = chaine[1:-1]
    return chaine

def split_matrix(chaine):

    op = ["/","\\","*","-","+"]
    for i in op:
        print(i)


    if re.search("/", chaine):

        chaine = chaine.split("\\")
        a = np.matrix(chaine[0])
        b = np.matrix(chaine[1])

        return np.divide(a, b)

    if re.search("\\\\", chaine):
        chaine = chaine.split("\\")

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

    if re.search("\*",chaine):

        chaine = chaine.split("*")

        a = np.matrix(chaine[0])
        b = np.matrix(chaine[1])
        'matrix_calculator([10;10]*[3;1])'
        'matrix_calculator([[2;2];[10;10]]⋅[[3;1];[2;4]]−[[1;2];[1;3]]),'
        return np.multiply(a,b)



def matrix_calculator(chaine):
    chaine = chaine.replace("matrix_calculator(","")
    chaine = chaine.replace(")", "")
    return split_matrix(chaine)



def doc(request):
    return render(request, 'documentation.html', {'output': "bonjour"})

def run(request):

    global history
    res = "bonjour veuiller entrer help pour la syntax"

    if request.method == 'POST':
        command = request.POST["cal"]

        try:

            if re.search("matrix_calculator",command):

                res = matrix_calculator(command)
                return render(request, 'index.html', {'output': str(res)})
                history = str(res) + "\n" + history

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

    return render(request, 'index.html', {'output': str(res), 'history': str(history)  })
