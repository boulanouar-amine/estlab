import numpy as np
import re

'''
def check_bracket(chaine):
    counter = 0
    for c in chaine:
        if c == '[':
            counter += 1
        elif c == ']':
            counter -= 1
        else:
            raise AttributeError('invalid character in the argument')
        if counter < 0:
            return False
    return counter == 0
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
            val1 = np.matrix(str(new))
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


def del_double_bracket(chaine):
    chaine = chaine.replace("[[", "")
    chaine = chaine.replace("]]", "")
    return chaine


def del_simple_bracket(chaine):
    if chaine[0] == '[' and chaine[len(chaine) - 1] == ']':
        chaine = chaine[1:-1]
    return chaine


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


res = matrix_calculator('matrix_calculator([[2,2];[10,10]]/[[3,1];[2,4]])')
'matrix_calculator([10;10]*[3;1])'
'matrix_calculator([[2,2];[10,10]]*[[3,1];[2,4]]−[[1,2];[1,3]]),'

print(evaluate("[2,1]/[3,1]+[8.6]"))
