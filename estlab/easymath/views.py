from django.shortcuts import render
import numpy as np
import array_to_latex as a2l
import re
history = ""

def format_number(command):
    return str("{:.5f}".format(command))

def extract(command,ele):
    chaine = command.replace(ele, "").replace("(", "").replace(")", "")
    return chaine


def calculate(command):
    if command == "help" or command == "help()":
        command = ""
        res = "vous pouver voir la documentation dans /documentation"
    if command == "quit" or command == "exit":
        command = ""
        pass
    else:
        # else its a number
        res = eval(command)
    return  format_number(res)


def determinant(chaine):
    x = np.matrix(chaine)
    return format_number((np.linalg.det(x))) # return 2 number after  comma


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
            a = np.matrix(chaine[0]) #if there is another element redo
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

            commands = ("inverse_matrix","determinant", "matrix_calculator","calculate")  # can add new functions here

            # what this does is extract the name of the function if it exist in the dictionary from user input then executes it with the argument given
            res = ''.join([eval(ele + "(extract(command,ele))") for ele in commands if re.search(ele, command)])  # or i can use eval(ele+"(command)"),commands[ele](extract(command,ele)

        except (IndexError, ZeroDivisionError):
            res = "division par 0"

        except np.linalg.LinAlgError:
            res = "Last 2 dimensions of the array must be square"

        except:

            res = "Veuiller entrer une formule valid"

    return render(request, 'index.html', {'output': str(res),history: str(history)})
