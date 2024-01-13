import json

def find_value_by_key(key_to_find):
    # Загрузка данных из файла user_idbx24_idop.json
    with open('user_idbx24_idop.json', 'r') as json_file:
        user_idbx24_idop_list = json.load(json_file)

    # Поиск значения по ключу
    for user_mapping in user_idbx24_idop_list:
        for key, value in user_mapping.items():
            if str(key) == str(key_to_find):
                return value

    # Возвращаем None, если ключ не найден
    return None

# Пример использования
key_to_find = 8  # Замените на нужный ключ
result = find_value_by_key(key_to_find)

if result is not None:
    print(f"Значение для ключа {key_to_find}: {result}")
else:
    print(f"Ключ {key_to_find} не найден в файле.")
