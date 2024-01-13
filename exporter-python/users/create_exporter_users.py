import requests
import base64
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
env_file = find_dotenv("../.env")
API_KEY = os.environ.get("API_KEY")
URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")

def create_openproject_users(user_list, base_url, api_key):

    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {api_key}'
    }
    

    for user_data in user_list:
        user_payload = {
            'user': {
                'login': user_data['login'],
                'firstName': user_data['firstName'],
                'lastName': user_data['lastName'],
                'email': user_data['email'],
                'status': user_data.get('status', 'active'),
                'admin': user_data.get('admin', False),
                'password': user_data.get('password', ''),
                'language': user_data.get('language', 'en')
            }
        }

        try:
            response = requests.post(f'{base_url}/api/v3/users', json=user_payload['user'], headers=headers)
              


            if response.status_code == 201:
                print(f"User {user_data['login']} created successfully.")
            elif response.status_code == 422:
                print(f"User {user_data['login']} already exists. Skipping.")
            else:
                print(f"Failed to create user {user_data['login']}. Error: {response.text}")
        except Exception as e:
            print(f"An error occurred while creating user {user_data['login']}: {str(e)}")

if __name__ == "__main__":
    openproject_base_url = URL_OPENPROJECT
    api_key_string = API_KEY

    # Кодирование в формате Base64
    api_key_base64 = base64.b64encode(api_key_string.encode()).decode()

    # Чтение user_list из файла
    # open_file_name = 'transformed_data.json' #Пользователи
    open_file_name = 'transformed_data.json' #Компании Клиенты

    with open(open_file_name, 'r') as file:
        user_list = json.load(file)

    create_openproject_users(user_list, openproject_base_url, api_key_base64)

