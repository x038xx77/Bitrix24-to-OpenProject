import re
import os

# Путь к вашей папке с файлами
folder_path = "./comments_task/all_create_task"

# Получение списка файлов в папке
files = os.listdir(folder_path)

# Использование регулярного выражения для извлечения чисел из названий файлов
numbers = [int(re.search(r'\d+', filename).group()) for filename in files if re.search(r'\d+', filename)]

# Вывод списка чисел
print("Список чисел из названий файлов:", numbers)
