import requests
import base64
import json
import os
from dotenv import load_dotenv, find_dotenv
import uuid

# Чтение user_list из файла
# open_file_name = 'transformed_data.json' #Пользователи
open_file_name_bx24 = 'users_list_bx24.json' #Компании Клиенты
open_file_name_openproject = 'user_list_openproject.json' #Компании Клиенты

with open(open_file_name_bx24, 'r') as file:
    user_list_bx24 = json.load(file)
with open(open_file_name_openproject, 'r') as file:
    user_list_openproject = json.load(file)
# Сравнение списков по электронным адресам
# Список для хранения пар id_bx24: email_op
user_idbx24_idop_list = []

# Сравнение списков по электронным адресам
for user_bx24 in user_list_bx24:
    id_bx24 = user_bx24.get("id")
    email_bx24 = user_bx24.get("email")

    for user_openproject in user_list_openproject['_embedded']['elements']:
        email_openproject = user_openproject.get("email")
        id_user_openproject = user_openproject.get("id")

        if email_bx24 and email_openproject and email_bx24 == email_openproject:
            user_idbx24_idop_list.append({id_bx24: id_user_openproject})
            break  # Если адрес найден, выходим из внутреннего цикла

# Запись результата в файл user_idbx24_idop.json
with open('user_idbx24_idop.json', 'w') as json_file:
    json.dump(user_idbx24_idop_list, json_file, indent=2)

print("Создан файл user_idbx24_idop.json.")