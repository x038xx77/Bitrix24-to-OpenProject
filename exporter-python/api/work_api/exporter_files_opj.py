# import base64
# import requests
# from requests.auth import HTTPBasicAuth
# import json
# import os
# from dotenv import load_dotenv, find_dotenv
# from urllib.parse import urljoin

# load_dotenv(find_dotenv())
# env_file = find_dotenv("../.env")
# API_KEY = os.environ.get("API_KEY")
# URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")
# api_key_base64 = base64.b64encode(API_KEY.encode()).decode()
# base_url = URL_OPENPROJECT

# headers = {
#     'Content-Type': 'multipart/form-data',
#     'Authorization': f'Basic {api_key_base64}'
# }

# project_id = "demo-project"
# work_package_id = "49"
# file_path = "data-bx24/file/image (68).png"

# try:
#     with open(file_path, 'rb') as file:
#         file_contents = file.read()

#     file_name = os.path.split(file_path)[-1]
#     file_stat = os.stat(file_path)
#     file_size = file_stat.st_size
#     file_creation_time = file_stat.st_ctime

#     print(f"Имя файла: {file_name}")
#     print(f"Размер файла: {file_size} байт")
#     print(f"Время создания файла: {file_creation_time}")
#     print(f"Файл {file_path} успешно загружен.")
# except FileNotFoundError:
#     print(f"Файл {file_path} не найден.")
# except IOError as e:
#     print(f"Ошибка при чтении файла {file_path}: {e}")

# try:
#     url_send = urljoin(base_url, f"api/v3/work_packages/{work_package_id}/attachments")
#     files = {'file': (file_name, file_contents)}
#     print("URL====",url_send)

#     params = {
#         'filename': file_name,
#         'description': {
#             'format': 'plain',
#             'raw': file_name,
#         },
#         'filesize': file_size,
#     }

#     # response = requests.post(url_send,  data=file_contents, headers=headers)
#     response = requests.post(url_send, metadata=params, data=file_contents, headers=headers)
#     print("RES----",response )
#     if response.status_code == 201:
#         task = response.json()
#         print(f"Task {task['id']} created successfully.")
#     elif response.status_code == 422:
#         print(f"Task Error code 422. Skipping.")
#     else:
#         print(f"Failed to create task. Error: {response.text}")

# except Exception as e:
#     print(f"An error occurred while creating task: {str(e)}")

#================================================================
import requests
from requests.auth import HTTPBasicAuth
import base64

import json
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

# Замените это на соответствующие значения
openproject_url = os.environ.get("URL_OPENPROJECT")
username = "apikey"
password = "9b58c13ff1051fb65108878e945627f822b38efd9878071022855017246be55e"
work_package_id = 49
file_path = "data-bx24/file/image (68).png"
API_KEY = os.environ.get("API_KEY")
api_key_base64 = base64.b64encode(API_KEY.encode()).decode()
headers = {
    'Content-Type': 'multipart/form-data',
    
    'Authorization': f'Basic {api_key_base64}'
}
# headers = {
#     'Content-Type': 'application/hal+json; charset=utf-8',
    
#     'Authorization': f'Basic {api_key_base64}'
# }



# Формируем URL для загрузки вложения
url = f"{openproject_url}/api/v3/work_packages/{work_package_id}/attachments"

# Создаем сессию и отправляем запрос
with open(file_path, 'rb') as file:
    file_contents = file.read()

file_name = os.path.split(file_path)[-1]
file_stat = os.stat(file_path)
file_size = file_stat.st_size
file_creation_time = file_stat.st_ctime

# metadata = {
#     'fileName': 'report.txt',
#     'description': 'This is a sample report.'
# }

# Prepare the multipart/form-data request

with open('file.txt', 'rb') as file_content:
    # Создаем JSON-объект для метаданных
    metadata = {'fileName': file_name}

    # Собираем данные запроса
    data = {
        'metadata': json.dumps(metadata),
        'file': (file_name, file_content)
    }

    # Собираем файл для отправки
    files = {
        'metadata': json.dumps(metadata),
        'file': (file_name, file_content)  # Имя файла, бинарное содержимое
    }

    hal_json_data = {"metadata": {'fileName': file_name }
    # json_data = json.dumps(hal_json_data)

}


    # Отправляем запрос
    print(url, files)
    response = requests.post(url, json=hal_json_data, files=data, headers=headers)

    # Выводим ответ сервера
    print(response, response.text)