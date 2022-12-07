from flask import request, jsonify, Blueprint

openface = Blueprint('openface', __name__)

@openface.route('openface', request=['POST'])
def openface(): 
    if request.method == 'POST':
        f = request.files['file']
        
        # si queremos guardar la foto
        filename = f.filename
        path = "D://SOFTWARE_CONSTRUCTION//images//" + filename
        f.save(path)       
           
        # call openfaceAPI ##################################
        url = 'http://127.0.0.1:81/openfaceAPI'
        files = {'file': open(path, 'rb')}
        #files = {'file': f}

        result = request.post(url, files=files)

        print(result.json())
        ######################################################

    return jsonify(result.json())