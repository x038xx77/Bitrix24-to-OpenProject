import requests
import base64
import json
import os
from dotenv import load_dotenv, find_dotenv
import uuid


load_dotenv(find_dotenv())
env_file = find_dotenv("../.env")
API_KEY = os.environ.get("API_KEY")
URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")

def create_openproject_user(user_obj, base_url, api_key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {api_key}'
    }    

    random_unique_id = str(uuid.uuid4())
    # Сокращение длины строки до 7 символов
    shortened_id = random_unique_id[:7]

    user_payload = {
        'login': user_obj.get('email',  f'{shortened_id}@empty.mail'),
        'firstName': user_obj.get('name', ''),
        'lastName': user_obj.get('last_name', ''),
        'email': user_obj.get('email',  f'{shortened_id}@empty.mail'),
        'status': user_obj.get('status', 'active'),
        'admin': user_obj.get('admin', False),
        # 'avatar': user_obj.get('personal_photo', ''),
        'password': user_obj.get('password', user_obj.get('email',  f'{shortened_id}@empty.mail')),
        'language': user_obj.get('language', 'ru'),
        }

    try:
        response = requests.post(f'{base_url}/api/v3/users', json=user_payload, headers=headers)
        if response.status_code == 201:
            print(f"User {user_obj.get('email',  f'{shortened_id}@empty.mail')} created successfully.")
        elif response.status_code == 422:
            print(f"ELIF User {user_obj.get('email',  f'{shortened_id}@empty.mail')} status 422. Skipping.")
        else:
            print(f"Failed to create user {user_obj.get('email',  f'{shortened_id}@empty.mail')}. Error: {response.text}")
    except Exception as e:
        print(f"An error occurred while creating user {user_obj['email']}: {str(e)}")

if __name__ == "__main__":
    openproject_base_url = URL_OPENPROJECT
    api_key_string = API_KEY

    # Кодирование в формате Base64
    api_key_base64 = base64.b64encode(api_key_string.encode()).decode()

    # Чтение user_list из файла
    # open_file_name = 'transformed_data.json' #Пользователи
    open_file_name_bx24 = 'users_list_bx24.json' #Компании Клиенты
    open_file_name_openproject = 'user_list_openproject.json' #Компании Клиенты

    with open(open_file_name_bx24, 'r') as file:
        user_list_bx24 = json.load(file)
    with open(open_file_name_openproject, 'r') as file:
        user_list_openproject = json.load(file)
    
   
    # Сравнение списков по электронным адресам
    common_emails = []
    for user_bx24 in user_list_bx24:
        email_bx24 = user_bx24.get("email")  # Предполагается, что у пользователя есть поле "email"

        for user_openproject in user_list_openproject['_embedded']['elements']:
            email_openproject = user_openproject.get("email")  # Предполагается, что у пользователя есть поле "email"

            if email_bx24 and email_openproject and email_bx24 == email_openproject:
                common_emails.append(email_bx24)
                break  # Если адрес найден, выходим из внутреннего цикла
                
                # create_openproject_user(user_bx24, openproject_base_url, api_key_base64)
    
    for user_bx24 in user_list_bx24:
        if not user_bx24['email'] in common_emails:
            # print("НЕТ", user_bx24['email'], user_bx24)
            create_openproject_user(user_bx24, openproject_base_url, api_key_base64)

    # Вывод результатов
    print(openproject_base_url, api_key_base64)
    print("Общие электронные адреса:", common_emails)
    
    # create_openproject_users(user_list, openproject_base_url, api_key_base64)