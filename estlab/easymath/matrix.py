import numpy as np
import re
import array_to_latex as a2l


'''
 def clean_res(chaine):
                return str(chaine).replace('[', '').replace(']', '').replace('\'', '')
'''



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


def format_matrix(chaine,num):
    """begin = '$$\\begin{pmatrix}'
    data ="\\\\".join(str(i) for i in chaine)
    end = '\end{pmatrix}$$'
    return begin + del_brackets(data) + end
    """
    return "$$" + str(a2l.to_ltx(chaine, arraytype='pmatrix', frmt='{:.'+str(num)+'f}', )) + "$$"


def inverse_matrix(chaine):
    chaine = chaine.replace("inverse_matrix(", "").replace(")", "")
    x = np.matrix(chaine)
    x = np.linalg.inv(x)
    return format_matrix(x,5)


def determinant(chaine):
    chaine = chaine.replace("determinant(", "").replace(")", "")
    x = np.matrix(chaine)
    print(np.linalg.det(x))
    return np.linalg.det(x)




res = matrix_calculator('matrix_calculator([1,2];[10,10]+[3,1];[2,4])')

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
res1 =('inverse_matrix([6, 1, 1];[4, -2, 5])')

res2 = ('determinant([3,1,0];[3,2,1];[4,1,7]),')
determinant(res2)

def format_number(chaine):
    return str("$$" + "{:.2f}".format(chaine) + "$$")



def average(chaine):
    return format_number(np.average(np.matrix(chaine)))

res3='[1,2,3,4,5,6]'

average(res3)