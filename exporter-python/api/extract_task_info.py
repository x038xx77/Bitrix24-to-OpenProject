
import json
from datetime import datetime

def format_date(original_date):
    # Преобразовываем строку в объект datetime
    original_datetime = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S%z")
    # Форматируем дату обратно в строку в нужном формате
    formatted_date = original_datetime.strftime("%Y-%m-%d")
    return formatted_date

def create_project(progect_id):

    return f'Создан проект: bt24-{progect_id}'


def extract_task_info(data):
    # Проверка наличия ключей в данных
    if "GROUP_ID" in data:
        group_id = data.get("GROUP_ID", "")
        
        title = data.get("TITLE", "")
        
        description = data.get("DESCRIPTION", "")
        responsible_name = data.get("RESPONSIBLE_NAME", "")
        responsible_last_name = data.get("RESPONSIBLE_LAST_NAME", "")
        responsible_second_name = data.get("RESPONSIBLE_SECOND_NAME", "")
        created_date_str = data.get("CREATED_DATE", "")
        closed_date_str = data.get("CLOSED_DATE", "")
        
        created_date=""
        if created_date_str:
             created_date = format_date(created_date_str)
        
        
        closed_date=""
        if closed_date_str:
             closed_date = format_date(closed_date_str)
        

        print(f"TITLE: {title}")
        print(f"DESCRIPTION: {description}")
        print(f"GROUP_ID: bt24-{group_id}")
        print(f"RESPONSIBLE_NAME: {responsible_last_name} {responsible_name} {responsible_second_name}")
        print(f"CREATED_DATE: {created_date}")
        print(f"CLOSED_DATE: {closed_date}")
        print(f"=============================")
    else:
        print("Нет GROUP_ID.")
