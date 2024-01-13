import csv
import json

# Путь к вашему CSV-файлу
csv_file_path = 'projects.csv'

# Путь для сохранения JSON-файла
json_file_path = 'project_lict.json'

# Считывание данных из CSV и преобразование в JSON
csv_data = []
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter='\t')
    for row in csv_reader:
        csv_data.append(row)

# Запись данных в JSON-файл
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(csv_data, jsonfile, ensure_ascii=False, indent=2)

print(f'Преобразование завершено. JSON-файл сохранен в {json_file_path}')

