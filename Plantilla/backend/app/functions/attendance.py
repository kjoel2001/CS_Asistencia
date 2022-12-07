from dis import dis
from os import remove
import numpy as np

# Calculate Euclidean distance
# Return Float
def euclidianaDistance(vector1, vector2):
    dist = np.sqrt(np.sum(np.square(vector1 - vector2)))
    print(dist)
    return dist

def marckAttendanc(vect1, vect2):
    return True if euclidianaDistance(np.array(vect1), np.array(vect2)) < 0.86 else False
      
# Dictionary to string
# Return list string
def dictToString(dic):
    res = []
    result = dic['result'].replace("\n", "").replace("  ", " ").replace("[", "").replace("]", "") 
    result = list(result.split(' ')) 
    for i in result:
        if i == '':
            pass
        else:
            res.append(i)
    return res

# JSON to String
# Return list string
def toString(string):
    result = string.replace('{','').replace('}','')
    result = list(result.split(','))
    return result

def toFloat(arr):
    vector = []
    for i in arr:
        vector.append(float(i))
    return vector

def savePath(f):
    # Para guardar momentaneamente la foto para ser procesada
    filename = f.filename
    path  = 'E://LaSalle//2022-II//ConstruccionSoftware//Parcial//img//input-img//' + filename
    f.save(path)
    return path

