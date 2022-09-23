import json
import numpy as np
import pandas as pd
from datetime import timedelta, datetime


def print_list(array):
    for item in array:
        print(item)


def load_json_file(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def load_np_file(path):
    return np.load(path)


def save_json_file(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


def save_np_file(path, data):
    with open(path, 'wb') as file:
        np.save(file, data)


def get_dates_between(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    dates = pd.date_range(date1, date2, freq='d').to_list()
    dates_strings = [datetime.strftime('%Y-%m-%d') for datetime in dates]
    return dates_strings
