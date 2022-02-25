from django.shortcuts import render
from pylab import *

history = ""

def doc(request):
    return render(request, 'documentation.html', {'output': "bonjour"})


def run(request):
    global history
    res = "bonjour veuiller entrer help pour la syntax"

    if request.method == 'POST':
        command = request.POST["cal"]

        try:
            if command == "M":
                M = array(((1,2,3), (4,5,6), (7,8,9)))
                history = str(res) + "\n" + history
                return render(request, 'index.html', {'output': str(M)})

            if command == "help" or command == "help()":
                command = ""
                res = "vous pouver voir la documentation dans /documentation"
                return render(request, 'index.html', {'output': str(res)})

            if command == "quit" or command == "exit":
                command = ""
                pass

            else:
                """def my_exec(code):
                               exec('global i; i = %s' % code)
                               global i
                               return i

                res = my_exec(command)"""
                res = eval(command)
                history = str(res) + "\n" + history

        except (IndexError, ZeroDivisionError):
            res = "division par 0"
        except:

            res = "Veuiller entrer une formule valid"

    return render(request, 'index.html', {'output': str(res), 'history': str(history)})
