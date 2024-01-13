import requests
import base64
import json
import os
from dotenv import load_dotenv, find_dotenv
import uuid

# Чтение user_list из файла
# open_file_name = 'transformed_data.json' #Пользователи
open_file_name_bx24 = 'tasks_bx24.json' #Компании Клиенты
open_file_name_openproject = 'task_list_openproject.json' #Компании Клиенты

with open(open_file_name_bx24, 'r') as file:
    task_list_bx24 = json.load(file)
with open(open_file_name_openproject, 'r') as file:
    task_list_openproject = json.load(file)
# Сравнение списков по электронным адресам
# Список для хранения пар id_bx24: email_op
task_idbx24_idop_list = []

# Сравнение списков по электронным адресам
for task_bx24 in task_list_bx24:
    id_bx24 = task_bx24.get("ID")
    title_bx24 = task_bx24.get("TITLE")

    for task_openproject in task_list_openproject:
        title_openproject = task_openproject.get("title")
        id_task_openproject = task_openproject.get("id")

        if title_bx24 and title_openproject and title_bx24 == title_openproject:
            task_idbx24_idop_list.append({id_bx24: id_task_openproject})
            break  # Если адрес найден, выходим из внутреннего цикла

# Запись результата в файл tasks_idbx24_idop.json
with open('tasks_idbx24_idop.json', 'w') as json_file:
    json.dump(task_idbx24_idop_list, json_file, indent=2)
count_task = len(task_idbx24_idop_list)
print("Создан файл tasks_idbx24_idop.json. кол-во задач: ", count_task, len(task_list_bx24), len(task_list_openproject))