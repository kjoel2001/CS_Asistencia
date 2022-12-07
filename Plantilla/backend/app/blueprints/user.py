from cgitb import reset
from .functions import *
from flask import Blueprint, request, jsonify
from app.models.User import *
from flask_cors import cross_origin
import requests, json
import numpy as np

model = User()
user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/test', methods=['POST'])
# @wrap('decorator')
def test():
    if request.method == 'POST':
        f = request.files['file']
        data=json.loads(request.form.get('data'))
        
        # si queremos guardar la foto
        filename = f.filename
        path = "E://LaSalle//2022-II//ConstruccionSoftware//Parcial//img" + filename
        f.save(path)       
        

        # call openfaceAPI ##################################
        url = 'http://127.0.0.1:81/openfaceAPI'
        files = {'file': open(path, 'rb')}
        #files = {'file': f}

        result = requests.post(url, files=files)
        result = result.json()

        # print(result)
        
        # result = result['result'].replace("\n", "") 
        # result = result.replace("  ", " ") 
        # result = result.replace("[", "") 
        # result = result.replace("]", "") 
        # result = list(result.split(' ')) 

        result = result['result'].replace("\n", "").replace("  ", " ").replace("[", "").replace("]", "")   
        print(result)
        vector = []

        for i in result:
            if i == '':
                pass
            else: 
                vector.append(float(i))

        #print(vector)
        arr = np.array(vector)
        dist = np.sqrt(np.sum(np.square(arr - arr)))
        print(dist)
        
        ######################################################
       
        # queda pendiente: registrar los demas datas del 
        # usuario en la BD junto con el vector de caracteristicas
       
        #string = listToString(result)
        #print(result)

    return jsonify(result)

@user.route('/test1', methods=['POST'])
# @wrap('decorator')
def test1():
    if request.method == 'POST':
        # File and JSON data
        f    = request.files['file']
        data = json.loads(request.form.get('data'))
        # data = json.loads(request.files['data'])

        ####################################################

        # si queremos guardar la foto    
        path = savePath(f)

        # call openfaceAPI ##################################
        result = callOpenFaceAPI(path)
     
        usr_dni         = data['usr_dni']
        usr_photo       = path
        usr_pass        = data['usr_pass']
        usr_name        = data['usr_name']
        usr_last_name   = data['usr_last_name']
        usr_dob         = data['usr_dob']
        usr_email       = data['usr_email']
        usr_vec         = toString(result)
        ust_id          = data['ust_id']

        new_user = User(
                        usr_dni,  
                        usr_pass,
                        usr_photo,
                        usr_name,
                        usr_last_name, 
                        usr_dob, 
                        usr_email, 
                        usr_vec, 
                        ust_id
                        )
    
        db.session.add(new_user)
        db.session.commit()

    return user_schema.jsonify(new_user)

@user.route('/create_user', methods=['POST'])
def create_user():
    return model.create_user(request.files['file'], json.loads(request.form.get('data')))

@user.route('/users', methods=['GET'])
@cross_origin()
def users():
    return jsonify(model.users())

@user.route('/delete_user', methods=['DELETE'])
@cross_origin()
def delete_user():
    return model.delete_user(request.json['usr_id'])

@user.route('/update_user', methods=['PUT'])
@cross_origin()
def update_user():
    return model.update_user(request.json['usr_id'], request.json['usr_name'])

@user.route('/select_user', methods=['GET'])
@cross_origin()
def select_user():
    return (model.select_user(request.json['usr_id']))

@user.route('/select_dni', methods=['GET'])
@cross_origin()
def select_dni():
    return model.select_dni(request.json['usr_dni'])