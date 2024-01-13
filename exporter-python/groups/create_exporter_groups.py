import requests
import base64
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
env_file = find_dotenv("../.env")
API_KEY = os.environ.get("API_KEY")
URL_OPENPROJECT = os.environ.get("URL_OPENPROJECT")

def create_openproject_groups(group_list, base_url, api_key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {api_key}'
    }

    for group_data in group_list:
        members = []
        for member_link in group_data['_links']['members']:
            member_id = member_link['href'].split('/')[-1]
            members.append({
                'href': f'/api/v3/users/{member_id}'
            })

        group_payload = {
            'name': group_data['name'],
            '_links': {
                'members': members
            }
        }

        print(group_payload)
        # Uncomment the following block to send the request to OpenProject
        try:
            response = requests.post(f'{base_url}/api/v3/groups', json=group_payload, headers=headers)
        
            if response.status_code == 201:
                print(f"Group {group_data['name']} created successfully.")
            elif response.status_code == 422:
                print(f"Group {group_data['name']} already exists. Skipping.")
            else:
                print(f"Failed to create group {group_data['name']}. Error: {response.text}")
        except Exception as e:
            print(f"An error occurred while creating group {group_data['name']}: {str(e)}")

if __name__ == "__main__":
    openproject_base_url = URL_OPENPROJECT
    api_key_string = API_KEY

    # Кодирование в формате Base64
    api_key_base64 = base64.b64encode(api_key_string.encode()).decode()

    # Чтение group_list из файла
    with open('group_list.json', 'r') as file:
        group_list = json.load(file)

    create_openproject_groups(group_list, openproject_base_url, api_key_base64)
