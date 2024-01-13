import requests
import base64
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
env_file = find_dotenv("../.env")
API_KEY = os.environ.get("API_KEY")
URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")

USERS_FILE = "users_openproject.json"  # Имя файла для сохранения пользователей

def get_openproject_users(base_url, api_key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {api_key}'
    }

    users_data = []

    try:
        # Получаем информацию о пользователях без параметра пагинации
        initial_response = requests.get(f'{base_url}/api/v3/users', headers=headers)
        initial_data = initial_response.json()
        total_users = initial_data["total"]
        page_size = initial_data["pageSize"]

        # Рассчитываем количество страниц для пагинации
        total_pages = (total_users + page_size - 1) // page_size

        for page in range(1, total_pages + 1):
            response = requests.get(f'{base_url}/api/v3/users', headers=headers, params={'pageSize': page_size, 'offset': (page - 1) * page_size})

            if response.status_code == 200:
                current_page_users = response.json()["_embedded"]["elements"]
                users_data.extend(current_page_users)
            else:
                print(f"Failed to get users. Error: {response.text}")
                break

        # Сохранение данных в файл
        with open(USERS_FILE, 'w') as users_file:
            json.dump(users_data, users_file, indent=2)

        print(f"Users saved successfully to {USERS_FILE}")
    except Exception as e:
        print(f"An error occurred while getting users: {str(e)}")

if __name__ == "__main__":
    openproject_base_url = URL_OPENPROJECT
    api_key_string = API_KEY

    # Кодирование в формате Base64
    api_key_base64 = base64.b64encode(api_key_string.encode()).decode()

    get_openproject_users(openproject_base_url, api_key_base64)

