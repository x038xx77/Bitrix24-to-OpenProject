import requests
import base64
import json
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
env_file = find_dotenv("../.env")
API_KEY = os.environ.get("API_KEY")
URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")

def create_openproject_projects(project_list, base_url, api_key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {api_key}'
    }

    for project_data in project_list:
        # Добавляем префикс 'bt24' к значению 'identifier'
        project_data['identifier'] = f'bt24-{project_data["identifier"]}'

        project_payload = {
            'project': {
                'identifier': project_data['identifier'],
                'name': str(project_data['name'])
            }
        }

        try:
            response = requests.post(f'{base_url}/api/v3/projects', json=project_payload['project'], headers=headers)

            if response.status_code == 201:
                print(f"Project {project_data['name']} created successfully.")
            elif response.status_code == 422:
                print(f"Project {project_data['name']} already exists. Skipping.")
            else:
                print(f"Failed to create project {project_data['name']}. Error: {response.text}")
        except Exception as e:
            print(f"An error occurred while creating project {project_data['name']}: {str(e)}")

if __name__ == "__main__":
    openproject_base_url = URL_OPENPROJECT
    api_key_string = API_KEY

    # Кодирование в формате Base64
    api_key_base64 = base64.b64encode(api_key_string.encode()).decode()

    # Чтение project_list из файла
    with open('project_lict.json', 'r') as file:
        project_list = json.load(file)

    create_openproject_projects(project_list, openproject_base_url, api_key_base64)
