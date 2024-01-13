import json
from extract_task_info import extract_task_info

# Открываем файл tasks.json на чтение
with open('tasks.json', 'r') as json_file:
    # Загружаем данные из файла
    data = json.load(json_file)

# Теперь переменная data содержит данные из файла tasks.json
# Пример использования:
# print(data)
count=0
for item in data:
    count +=1
    extract_task_info(item)
print("Кол-во", count)

