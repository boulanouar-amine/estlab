import numpy as np
import re

def del_double_bracket(chaine):
    chaine = chaine.replace("[[", "")
    chaine = chaine.replace("]]", "")
    return chaine

def del_simple_bracket(chaine):
    if chaine[0] == '[' and chaine[len(chaine) - 1] == ']':
        chaine = chaine[1:-1]
    return chaine


def matrix_calculator(chaine):
    chaine = chaine.replace("matrix_calculator(","")
    chaine = chaine.replace(")", "")
    return split_matrix(chaine)


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


res = matrix_calculator('matrix_calculator([10,51,10]\[311,555,1])')
print(res)



