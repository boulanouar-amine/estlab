import numpy as np
import re
import array_to_latex as a2l

'''
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def applyOp(a, b, op):
    if op == '+': return np.add(a, b)
    if op == '-': return np.subtract(a, b)
    if op == '*': return np.multiply(a, b)
    if op == '/': return np.divide(a, b)


def evaluate(chaine):
    values = []
    ops = []
    i = 0

    while i < len(chaine):

        if chaine[i] == ' ':
            i += 1
            continue

        elif chaine[i] == '+' or chaine[i] == '-' or chaine[i] == '/' or chaine[i] == '*':
            ops.append(chaine[i])
            i += 1

        elif chaine[i] == '[' or chaine[i].isdigit() or chaine[i] == ',' or chaine[i] == ';':
            values.append(chaine[i])
            i += 1

        elif chaine[i] == ']':
            values.append(chaine[i])
            new = ""
            for x in values:
                new += str(x)
            val1 = np.matrix(new)
            print(val1)
            values.clear()
            i += 1


    else:

        while (len(ops) != 0 ):

            val2 = np.matrix(values)
            op = ops.pop()

            values.append(applyOp(val1, val2, op))

        i += 1

        return values[-1]
'''

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

def format_matrix(chaine):
    """begin = '$$\\begin{pmatrix}'
    data ="\\\\".join(str(i) for i in chaine)
    end = '\end{pmatrix}$$'
    return begin + del_brackets(data) + end
    """
    return "$$"+str(a2l.to_ltx(chaine , print_out=False , arraytype = 'pmatrix' , frmt = '{:.0f}',) )+"$$"

def inverse_matrix(chaine):
    chaine = chaine.replace("inverse_matrix(", "").replace(")", "")
    x = np.matrix(chaine)
    print(x)
    x = np.linalg.inv(x)
    print(x)
    return x

res = matrix_calculator('matrix_calculator([1,2];[10,10]+[3,1];[2,4])')

res1 =('inverse_matrix([[6, 1, 1];[4, -2, 5];[2, 8, 7]])')

inverse_matrix(res1)