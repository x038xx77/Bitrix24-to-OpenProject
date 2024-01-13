import requests
import base64
import json
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
env_file = find_dotenv("../.env")
API_KEY = os.environ.get("API_KEY")
URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")


api_key_base64 = base64.b64encode(API_KEY.encode()).decode()
base_url = URL_OPENPROJECT
headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {api_key_base64}'
    }

response = requests.get(f'{base_url}/api/v3/projects.xls?filters=%5B%5D&offset=1&pageSize=200', headers=headers)
data = response.json()
# Сохраняем данные в файл projects.json
with open('projects.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

print("Данные сохранены в файл projects.json.")

projects = data['_embedded']['elements']

# Создаем список для хранения словарей с id и identifier
identifier_list = []

# Заполняем список
for project in projects:
    identifier_dict = {"id": project["id"], "identifier": project["identifier"]}
    identifier_list.append(identifier_dict)

# Создаем и записываем данные в файл projects_list_identifier.json
with open('projects_list_identifier.json', 'w') as json_file:
    json.dump(identifier_list, json_file, indent=2)

print("Данные записаны в файл projects_list_identifier.json.")



