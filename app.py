from flask import Flask, render_template, request, redirect, jsonify, redirect, url_for, flash
import business as business
from werkzeug.utils import secure_filename
import os
import csv
import pandas as pd
import json

UPLOAD_PATH = "static/"
USERS_JSONPATH = "data.json"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload.html', files=files)

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        store_file_name(filename)

    return '', 204

@app.route('/show', methods=['POST','GET'])
def create_chart():

    json_data = get_json()

    file_name = json_data['file_name']

    result_dict,column_names = read_data(file_name)

    return render_template('bar_graph.html', result_dict = result_dict, column_names = column_names)

def read_data(file_name):

    df = pd.read_csv("static/" + str(file_name))

    list_of_column_names = list(df.columns)

    result  = df.to_dict('list')

    return result,list_of_column_names

def store_file_name(file_name):

    data_dict = {
        "file_name":file_name
    }

    json_data = get_json()

    # json_data["data"].append(data_dict)

    store_json(data_dict)

@app.route('/admin/view',methods=['GET','POST'])
def get_json():

    json_file = open(USERS_JSONPATH)
    json_data = json.load(json_file)

    return json_data

def store_json(data_dict):

    with open(USERS_JSONPATH, 'w') as outfile:
        json.dump(data_dict, outfile)

@app.route('/admin/flush',methods=['GET','POST'])
def flush_json():

    data_dict = get_json()

    data_list = []

    empty_data_dict = {
        "data": data_list
    }

    with open(USERS_JSONPATH, 'w') as outfile:
        json.dump(empty_data_dict, outfile)

    return 'Flushed'



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")