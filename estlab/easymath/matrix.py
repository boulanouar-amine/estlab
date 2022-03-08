import numpy as np
import re
import array_to_latex as a2l

"""

 def clean_res(chaine):
                return str(chaine).replace('[', '').replace(']', '').replace('\'', '')



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
    begin = '$$\\begin{pmatrix}'
    data ="\\\\".join(str(i) for i in chaine)
    end = '\end{pmatrix}$$'
    return begin + del_brackets(data) + end
    
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

'
           if re.search("inverse_matrix", command):
               res = inverse_matrix(command)
               return render(request, 'index.html', {'output': str(res)})

           if re.search("determinant", command):
               res = determinant(command)
               return render(request, 'index.html', {'output': str(res)})

           if re.search("matrix_calculator", command):
               res = matrix_calculator(command)
               return render(request, 'index.html', {'output': str(res)})

            
res1 =('inverse_matrix([6, 1, 1];[4, -2, 5])')

res2 = ('determinant([3,1,0];[3,2,1];[4,1,7]),')
determinant(res2)
"""

def format_number(chaine):
    return str("$$" + "{:.2f}".format(chaine) + "$$")


def vecteur_propre(chaine):
    chaine = np.matrix(chaine)
    x = np.linalg.eigvals(chaine)
    print(np.sort(x))
    return x

def format_matrix(chaine, num=0, arrtype="pmatrix"):
    return "$$" + str(
        a2l.to_ltx(chaine, arraytype=arrtype, frmt='{:.' + str(num) + 'f}', mathform=True)) + "$$"



res3='[6,1,1];[4,-2,5];[2,8,7]'

vecteur_propre(res3)

