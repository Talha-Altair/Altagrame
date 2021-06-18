from app import USERS_JSONPATH
import pandas as pd
import json

USERS_JSONPATH = "data.json"

def get_chart_style():

    chart_style = "N/A"

    json_data = get_json()

    file_name = json_data['file_name']

    result_dict,column_names = read_data(file_name)

    # print(result_dict)

    if len(column_names) == 2:
        if isinstance(result_dict[column_names[1]][1], float) or isinstance(result_dict[column_names[1]][1], int):
            chart_style = "bar_graph"
    if len(column_names) == 4:
        if isinstance(result_dict[column_names[1]][1], float) or isinstance(result_dict[column_names[1]][1], int) :
            chart_style = "scatter-box"
    if len(column_names) == 2:
        if isinstance(result_dict[column_names[0]][1], int) and (isinstance(result_dict[column_names[1]][1], int) or isinstance(result_dict[column_names[1]][1], float)):
            chart_style = "area-simple"

    return chart_style

def get_json():

    json_file = open(USERS_JSONPATH)
    json_data = json.load(json_file)

    return json_data

def read_data(file_name):

    df = pd.read_csv("static/" + str(file_name))

    list_of_column_names = list(df.columns)

    result  = df.to_dict('list')

    return result,list_of_column_names