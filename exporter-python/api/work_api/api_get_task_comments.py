import os
import json
from fast_bitrix24 import Bitrix

def get_task_comments(id_task_bx24, webhook):
    # Определение относительного пути к папке
    output_folder = 'comments_task'

    # Создание папки, если её нет
    os.makedirs(output_folder, exist_ok=True)

    # Формирование полного пути для файла
    output_file = os.path.join(output_folder, f'task_comments_{id_task_bx24}.json')

    b = Bitrix(webhook)
    comment_items = b.get_all('task.commentitem.getlist', params={"id": id_task_bx24})

    # Сохраняем комментарии в файл
    with open(output_file, 'w') as json_file:
        json.dump(comment_items, json_file, indent=2)

    # Подсчитываем количество комментариев
    comment_count = len(comment_items)
    print(f'Количество комментариев: {comment_count}')
    return comment_items




