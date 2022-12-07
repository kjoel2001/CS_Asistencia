import requests, json

''' call openfaceAPI, return vector de   caracteristicas '''
def openfaceAPI(path):
    url = 'http://127.0.0.1:81/openfaceAPI'
    files = {'file': open(path, 'rb')}

    result = requests.post(url, files=files) # opening a binary file
    result = result.json()
    # print(result)

    return result