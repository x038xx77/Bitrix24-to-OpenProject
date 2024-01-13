import csv
import json

# Имя CSV файла
# csv_filename = 'create_table_for_import_contact_users_for_create.csv'
csv_filename = 'create_table_for_import_company_client_suppliers_for_create.csv'

# Имя JSON файла, в который будут сохранены данные
# json_filename = 'contact_users.json' # Контакты
json_filename = 'company_client_suppliers.json' # Клиенты Поставщики

# Открываем CSV файл для чтения
with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
    # Создаем читатель CSV файла
    csv_reader = csv.DictReader(csv_file)

    # Создаем пустой список для хранения данных
    data_list = []

    # Итерируемся по строкам CSV файла
    for row in csv_reader:
        # Добавляем данные из каждой строки в список
        data_list.append(row)

# Открываем JSON файл для записи
with open(json_filename, mode='w', encoding='utf-8') as json_file:
    # Записываем данные в JSON файл
    json.dump(data_list, json_file, ensure_ascii=False, indent=2)

print(f'Data from CSV file "{csv_filename}" has been successfully converted to JSON file "{json_filename}".')
