import pandas as pd
import json

USERS_JSONPATH = "data.json"

def check_int(value):
    if isinstance(value, int):
        return True
    else:
        return False

def check_float(value):
    if isinstance(value, float):
        return True
    else:
        return False


def check_string(value):
    if isinstance(value, str):
        return True
    else:
        return False


def check_negative(value):
    for i in value:
        if i < 0:
            return True
    return False


def check(value):
    pass

def get_chart_style():

    chart_style = "N/A"

    json_data = get_json()

    file_name = json_data['file_name']

    result_dict,column_names = read_data(file_name)

    chart_list = []

    # print(result_dict)

    if len(column_names) == 2:
        if check_float(result_dict[column_names[1]][1]) or check_int(result_dict[column_names[1]][1]):
            chart_style = "bar_graph"
            chart_list.append(chart_style)
    if len(column_names) == 4:  
        if check_float(result_dict[column_names[1]][1]) or check_int(result_dict[column_names[1]][1]) :
            chart_style = "scatter-box"
            chart_list.append(chart_style)
    if len(column_names) == 2:
        if check_int(result_dict[column_names[0]][1]) and (check_int(result_dict[column_names[1]][1]) or check_float(result_dict[column_names[1]][1])):
            chart_style = "area-simple"
            chart_list.append(chart_style)
    if len(column_names) == 2:
        if check_int(result_dict[column_names[0]][1]) and (check_int(result_dict[column_names[1]][1]) or check_float(result_dict[column_names[1]][1])) and check_negative(result_dict[column_names[1]]):
            chart_style = "line-chart"
            chart_list.append(chart_style)
    

    return chart_list

def get_json():

    json_file = open(USERS_JSONPATH)
    json_data = json.load(json_file)

    return json_data

def read_data(file_name):

    df = pd.read_csv("static/" + str(file_name))

    list_of_column_names = list(df.columns)

    result  = df.to_dict('list')

    return result,list_of_column_names