import numpy as np
from django.shortcuts import render
from pylab import *
import array_to_latex as a2l

history = ""

def extract(command,ele):
    chaine = command.replace(ele, "").replace("(", "").replace(")", "")
    return chaine

def determinant(chaine):
    x = np.matrix(chaine)
    return str(np.linalg.det(x))


def format_matrix(chaine, num):
    return "$$" + str(a2l.to_ltx(chaine, print_out=False, arraytype='pmatrix', frmt='{:.' + str(num) + 'f}', )) + "$$"


def inverse_matrix(chaine):

    x = np.matrix(chaine)
    x = np.linalg.inv(x)

    return format_matrix(x, 5)


def matrix_calculator(chaine):
    op = {"/": np.divide, "\+": np.add, "\*": np.multiply ,"\-": np.subtract}
    for ele in op :
        if re.search(ele, chaine):
            chaine = chaine.split(ele.strip("\\"))
            a = np.matrix(chaine[0])
            b = np.matrix(chaine[1])
            chaine = op[ele](a, b)
            return format_matrix(chaine, 0)





def doc(request):
    return render(request, 'documentation.html', {'output': "bonjour"})


def run(request):
    global history
    res = "bonjour veuiller entrer help pour la syntax"

    if request.method == 'POST':
        command = request.POST["cal"]

        try:

            commands = {"inverse_matrix": inverse_matrix, "determinant": determinant,"matrix_calculator": matrix_calculator}  # this dosent display correctly with determinant
            # what this does is extract the name of the function if it exist in the dictionary from user input then executes it with the argument given
            res = ''.join([commands[ele](extract(command,ele)) for ele in commands if re.search(ele, command)])  # or i can use eval(ele+"(command)") but dosnt work with determinabt

            return render(request, 'index.html', {'output': str(res)})

            '''
            if re.search("inverse_matrix", command):
                res = inverse_matrix(command)
                return render(request, 'index.html', {'output': str(res)})

            if re.search("determinant", command):
                res = determinant(command)
                return render(request, 'index.html', {'output': str(res)})

            if re.search("matrix_calculator", command):
                res = matrix_calculator(command)
                return render(request, 'index.html', {'output': str(res)})

             '''
            if command == "help" or command == "help()":
                command = ""
                res = "vous pouver voir la documentation dans /documentation"
                return render(request, 'index.html', {'output': str(res)})

            if command == "quit" or command == "exit":
                command = ""
                pass

            else:
                #else its a number
                res = eval(command)
                history = str(res) + "\n" + history

        except (IndexError, ZeroDivisionError):
            res = "division par 0"

        except np.linalg.LinAlgError:
            return "Last 2 dimensions of the array must be square"

        except:

            res = "Veuiller entrer une formule valid"

    return render(request, 'index.html', {'output': str(res), 'history': str(history)})
