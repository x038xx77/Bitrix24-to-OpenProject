import requests
import base64
import json
import os

from dotenv import load_dotenv, find_dotenv


def create_comments_task(id_task_openprogect, comment_payload):
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
         
    try:
        response = requests.post(f'{base_url}/api/v3/work_packages/{id_task_openprogect}/activities', json=comment_payload, headers=headers)
        comment_obj = response.json()
        if response.status_code == 201:
            print(f"Task {comment_obj['id']} created successfully.")
            return comment_obj
        elif response.status_code == 422:
            print(f"Task {id_task_openprogect} already exists. Skipping.")
        else:
            print(f"Failed to create task {id_task_openprogect}. Error: {response.text}")
    except Exception as e:
        print(f"An error occurred while creating task {id_task_openprogect}: {str(e)}")