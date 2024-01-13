import os
import json
from fast_bitrix24 import Bitrix

def get_user(id_user, webhook):
    # Определение относительного пути к папке
    output_folder = 'user_task'

    # Создание папки, если её нет
    os.makedirs(output_folder, exist_ok=True)

    # Формирование полного пути для файла
    output_file = os.path.join(output_folder, f'user_{id_user}.json')

    b = Bitrix(webhook)
    comment_items = b.get_all('user.get', params={"id": id_user})

    # Сохраняем комментарии в файл
    if (len(comment_items) > 0):
        with open(output_file, 'w') as json_file:
            json.dump(comment_items, json_file, indent=2)

    # Подсчитываем количество комментариев
   
    print(f'Пользователь записан в файл: {comment_items}')
    return comment_items



url_webhook = "https://a-link-a.bitrix24.ru/rest/692/hocor6r4tn1144y0/"

# get_user(1000, url_webhook)

# Создаем список для хранения словарей с id и identifier
user_list = []

# Заполняем список
# counter = 0
for item in range(0, 700):
    # counter += 1

    data_user = []
    try:
        data_user = get_user(item, url_webhook)[0]
    except Exception as e:
        print(f"An error occurred while get user : {str(e)}")

    if (len(data_user)>0):
        identifier_dict = {
            "id":  data_user.get("ID", ""),
            "name": data_user.get("NAME", ""),
            "last_name": data_user.get("LAST_NAME", ""),
            "second_name": data_user.get("SECOND_NAME", ""),
            "email": data_user.get("EMAIL", ""),
            "date_register": data_user.get("DATE_REGISTER", ""),
            "personal_gender": data_user.get("PERSONAL_GENDER", ""),
            "personal_www": data_user.get("PERSONAL_WWW", ""),
            "personal_birdthday": data_user.get("PERSONAL_BIRTHDAY", ""),
            "personal_photo": data_user.get("PERSONAL_PHOTO", ""),
            "personal_mobile": data_user.get("PERSONAL_MOBILE", ""),
            "work_phone": data_user.get("WORK_PHONE", ""),
            "work_position": data_user.get("WORK_POSITION", ""),
            "uf_phone_inner": data_user.get("UF_PHONE_INNER", ""),
            }
        user_list.append(identifier_dict)

        
        with open('users_list.json', 'w') as json_file:
            json.dump(user_list, json_file, indent=2)

        print("Данные записаны в файл users_list.json.", user_list)

