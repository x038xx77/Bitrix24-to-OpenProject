# https://github.com/leshchenko1979/fast_bitrix24

import json
from fast_bitrix24 import Bitrix
from api_get_task_comments import get_task_comments

# Замените на ваш вебхук для доступа к Bitrix24
url_webhook = "https://a-link-a.bitrix24.ru/rest/692/o4wsv5u9wd14z8hk/"
b = Bitrix(url_webhook)
tasks = b.get_all('task.item.list')

for item_task in tasks:
    
    # Добавление комментариев
    try:
        if int(item_task['COMMENTS_COUNT']) > 0:
            get_task_comments(item_task['ID'], url_webhook)
    except Exception as e:
        print("An exception occurred:", e)

# Сохраняем задачи в файл tasks.json
with open('tasks.json', 'w') as json_file:
    json.dump(tasks, json_file, indent=2)

# Подсчитываем количество задач
task_count = len(tasks)
print(f'Количество задач: {task_count}')

