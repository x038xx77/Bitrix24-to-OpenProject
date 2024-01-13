import requests
import base64
import json
import os

from dotenv import load_dotenv, find_dotenv


def get_all_tasks_openproject():
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
        offset = 0
        page_size = 3000
        all_tasks = []

        while True:
            response = requests.get(f'{base_url}/api/v3/work_packages?filters=%5B%5D&offset={offset}&pageSize={page_size}', headers=headers)
            if response.status_code == 200:
                task_list = response.json()["_embedded"]["elements"]
                all_tasks.extend(task_list)
                offset += page_size
                if offset >= response.json()["total"]:
                    break
            elif response.status_code == 422:
                print(f"Task Error code 422. Skipping.")
                return None
            else:
                print(f"Failed to create task. Error: {response.text}")
                return None
    except Exception as e:
        print(f"An error occurred while creating task: {str(e)}")

    # Создаем и записываем данные в файл task_list_openproject.json
    with open('task_list_openproject.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=2)
    print(f"Task list created successfully.")

if __name__ == "__main__":
    get_all_tasks_openproject()



