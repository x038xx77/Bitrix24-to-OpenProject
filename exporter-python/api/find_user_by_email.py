import requests
import base64
import json
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
env_file = find_dotenv("../.env")
API_KEY = os.environ.get("API_KEY")
URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")

def find_user_by_email(api_url, api_key, email):

    
    api_key_base64 = base64.b64encode(api_key.encode()).decode()

    headers = {
        'Authorization': f'Basic {api_key_base64}',
        'Content-Type': 'application/json',
    }

    # Используйте соответствующий эндпоинт API для поиска пользователя по электронной почте
    # Пример: /api/v3/users?where={%22email%22:%22user@example.com%22}
    params = {
        'where': f'{{"email":"{email}"}}'
    }

    response = requests.get(api_url + '/api/v3/users.xls?filters=%5B%5D&offset=1&pageSize=700', headers=headers, params=params)
    
    # Определение относительного пути к папке
    output_folder = 'user_list_openproject'
    # Создание папки, если её нет
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, f'user_list_openproject.json')
    with open(output_file, 'w') as json_file:
            json.dump(response.json(), json_file, indent=2)

    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print(f"Failed to retrieve users. Status code: {response.status_code}")
        return None

# Пример использования
api_url = URL_OPENPROJECT  
api_key = API_KEY 
email_to_find = 'ffadmin@example.net'  # Замените на нужный email

found_users = find_user_by_email(api_url, api_key, email_to_find)

if found_users:
    print(f"Найденные пользователи: {found_users}")
else:
    print("Пользователь не найден.")
