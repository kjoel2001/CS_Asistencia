import numpy as np
import requests

# Convert Dictionary to String
# Return string list 
def toString(dic):
    res = []
    result = dic['result'].replace("\n", "").replace("  ", " ").replace("[", "").replace("]", "") 
    result = list(result.split(' ')) 
   
    for i in result:
        if i == '':
            pass
        else:
            res.append(i)
   
    return res

# Convert String list to Float list 
# Return Float list
def stringToFloat(arr):
    vector = []
    for i in arr:
        vector.append(float(i))

    return vector


# Calculate Euclidean distance
# Return Float
def euclidianaDistance(vector1, vector2):
    dist = np.sqrt(np.sum(np.square(vector1 - vector2)))
    return dist


def savePath(f):
    # si queremos guardar la foto
    filename = f.filename
    path = "E://LaSalle//2022-II//ConstruccionSoftware//Parcial//img//" + filename
    f.save(path)  

    return path

def callOpenFaceAPI(path):
    url = 'http://127.0.0.1:81/openfaceAPI'
    files = {'file': open(path, 'rb')}

    result = requests.post(url, files=files)
    result = result.json()

    return result