import json

def check_identifier_in_file(identifier_to_check, file_path='projects_list_identifier.json'):
    # Загружаем данные из файла
    with open(file_path, 'r') as json_file:
        identifier_list = json.load(json_file)

    # Проверяем наличие identifier в списке
    for item in identifier_list:
        if item["identifier"] == identifier_to_check:
            print(f"Идентификатор {identifier_to_check} найден с id {item['id']}.")
            return True

    print(f"Идентификатор {identifier_to_check} не найден.")
    return False

# Пример использования
# result = check_identifier_in_file("bt24-456")
