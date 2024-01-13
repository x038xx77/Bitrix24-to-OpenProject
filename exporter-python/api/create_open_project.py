import requests
import base64
import json
import os

from dotenv import load_dotenv, find_dotenv


def create_openproject_projects_is_null(project_id, name):
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

    identifier = f'bt24-{project_id}'

    project_payload = {
            'project': {
                'identifier': identifier,
                'name': name
            }
        }

    try:
        response = requests.post(f'{base_url}/api/v3/projects', json=project_payload['project'], headers=headers)
        if response.status_code == 201:
            print(f"Project {name} created successfully.")
        elif response.status_code == 422:
            print(f"Project {name} already exists. Skipping.")
        else:
            print(f"Failed to create project {name}. Error: {response.text}")
    except Exception as e:
        print(f"An error occurred while creating project {name}: {str(e)}")
