import json

# Имя исходного JSON файла
input_json_filename = 'company_client_suppliers.json'

# Имя нового JSON файла
output_json_filename = 'transformed_data.json'

# Загружаем данные из исходного JSON файла
with open(input_json_filename, 'r', encoding='utf-8') as input_file:
    original_data = json.load(input_file)

# Преобразуем данные в новый формат
transformed_data = []
for user_data in original_data:
    transformed_user_data = {
       
            'login': user_data['login'],
            'firstName': user_data['firstname'],
            'lastName': user_data['lastname'],
            'email': user_data['login'],  # Используем поле login как email
            'status': 'active',  # Устанавливаем статус по умолчанию
            'admin': False,  # Устанавливаем admin в False по умолчанию
            'password': user_data['login'],  # Используем поле login как пароль
            'language': 'ru'  # Устанавливаем язык по умолчанию
        
    }
    transformed_data.append(transformed_user_data)

# Записываем преобразованные данные в новый JSON файл
with open(output_json_filename, 'w', encoding='utf-8') as output_file:
    json.dump(transformed_data, output_file, ensure_ascii=False, indent=2)

print(f'Data from "{input_json_filename}" has been successfully transformed and saved to "{output_json_filename}".')
