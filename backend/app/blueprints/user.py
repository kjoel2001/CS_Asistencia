from cgitb import reset
from .functions import *
from flask import Blueprint, request, jsonify
from app.models.User import *
from flask_cors import cross_origin
import requests, json
import numpy as np


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
   
    if request.method == 'POST':
        # File and JSON data
        f    = request.files['file']
        data = json.loads(request.form.get('data'))
        # data = json.loads(request.files['data'])

        ####################################################

        # si queremos guardar la foto, return direccion de la foto   
        path = savePath(f)

        # call openfaceAPI, return vector de caracteristicas ##################################
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

@user.route('/users', methods=['POST'])
@cross_origin()
def users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@user.route('/delete_user/<usr_id>', methods=['POST'])
@cross_origin()
def delete_user(usr_id):
    user = User.query.get(usr_id)

    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

@user.route('/update_user/<ust_id>', methods=['POST'])
@cross_origin()
def update_user(ust_id):
    user = User.query.get(ust_id)
    name = request.json['ust_name']

    user.ust_name = name
    db.session.commit()
    return user_schema.jsonify(user)

@user.route('/select_user/<int:usr_id>', methods=['POST'])
@cross_origin()
def select_user(usr_id):
    user = User.query.get(usr_id) 
    print(user)
    return user_schema.jsonify(user)

@user.route('/select_dni/<usr_dni>', methods=['POST'])
@cross_origin()
def select_dni(usr_dni):
    user = User.query.filter_by(usr_dni=usr_dni).first_or_404()
    #print(user.usr_name)
    return user_schema.jsonify(user)