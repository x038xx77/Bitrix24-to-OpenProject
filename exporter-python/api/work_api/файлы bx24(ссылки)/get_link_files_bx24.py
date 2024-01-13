import json
import os
import requests
from fast_bitrix24 import Bitrix
from datetime import datetime


def get_task_link_files_bx24(id_task_bx24, webhook):
    # Определение относительного пути к папке
    output_folder = 'links_task_file'

    # Создание папки, если её нет
    os.makedirs(output_folder, exist_ok=True)

    # Формирование полного пути для файла
    output_file = os.path.join(output_folder, f'task_link_files_{id_task_bx24}.json')
    output_file_err = os.path.join(output_folder, f'task_link_files_error.json')

    b = Bitrix(webhook)
    link_files = b.get_all('task.item.getfiles', params={"id": id_task_bx24})
    
    # Подсчитываем количество комментариев
    files_count = len(link_files)

    print(f'Количество ссылок на файлы в задаче {id_task_bx24}: {files_count}')
    
    if (files_count > 0):        
        # Создаем папку с именем, соответствующим идентификатору задачи
        folder_path = f"{id_task_bx24}/"
        os.makedirs(folder_path, exist_ok=True)

        for file in link_files:
            print("FILE", file)
            #disk.file.get
            # Получаем содержимое файла 
            error_file_download = []    
            try:       
                file_content = b.get_all('disk.file.get', params={"id": file['FILE_ID']})   
            
           
                if file_content:
                    # Записываем файл локально
                    file_path = os.path.join(folder_path, file['NAME'])
                    response_file = requests.get(file_content['DOWNLOAD_URL'])

                    if response_file.status_code == 200:
                        with open(file_path, 'wb') as local_file:
                            local_file.write(response_file.content)
                        print(f"File '{file['NAME']}' saved successfully.")
                    else:
                        print(f"Failed to download file. Status code: {response_file.status_code}")
            except Exception as e:
                error_file_download.append(id_task_bx24)
                print(f"An error occurred while creating task: {str(e)}")

        # Сохраняем комментарии в файл
        with open(output_file, 'w') as json_file:
            json.dump(link_files, json_file, indent=2)
        print(f"Ссылки сохранены в файл task_link_files_{id_task_bx24}.json")
        #не сохраненные
        with open(output_file_err, 'w') as json_file_err:
            json.dump(error_file_download, json_file_err, indent=2)
        return link_files


# Загружаем данные из файла
file_path = 'tasks_bx24.json'
with open(file_path, 'r') as json_file:
    task_list = json.load(json_file)
url_webhook = 'https://a-link-a.bitrix24.ru/rest/692/4zka6yl2tukm6glm/'

for task in task_list:
    task_id_bx24 = task['ID']
    get_task_link_files_bx24(task_id_bx24, url_webhook)
