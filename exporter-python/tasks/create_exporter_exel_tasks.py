import requests
import base64
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
env_file = find_dotenv("../.env")
API_KEY = os.environ.get("API_KEY")
URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")


def create_openproject_tasks(task_list, base_url, api_key):

    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {api_key}'
    }
    print(f'Basic {api_key}')


if __name__ == "__main__":
    openproject_base_url = URL_OPENPROJECT
    api_key_string = API_KEY

    # Кодирование в формате Base64
    api_key_base64 = base64.b64encode(api_key_string.encode()).decode()

    # Чтение user_list из файла
    with open('task_list.json', 'r') as file:
        user_list = json.load(file)

    # create_openproject_tasks(task_list, openproject_base_url, api_key_base64) 