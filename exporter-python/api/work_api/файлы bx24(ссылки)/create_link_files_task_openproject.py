import requests
import base64
import json
import os

from dotenv import load_dotenv, find_dotenv


def create_openproject_links_files_task(project_payload, id):

   
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
    identifier = f'bt24-{id}'
   
   
    try:
        print("URL======",f'{base_url}/api/v3/projects/{identifier}/work_packages', project_payload )
        response = requests.post(f'{base_url}/api/v3/projects/{identifier}/work_packages', json=project_payload, headers=headers)
        
        if response.status_code == 201:
            task = response.json()
            print(f"Task {task['id']} created successfully.")      
           
            return task['id']
        elif response.status_code == 422:
            print(f"Task {id} Error code 422. Skipping.")
            return null
        else:
            print(f"Failed to create task {id}. Error: {response.text}")
            return null
    except Exception as e:
        print(f"An error occurred while creating task {id}: {str(e)}")