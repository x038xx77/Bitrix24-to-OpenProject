import * as fs from 'fs';
import FormData from 'form-data';
import axios from 'axios';
import { checkTaskID } from './checkTaskID';

export async function create_file_openprojectname(task_id:number, file_path:string, file_name:string) {
    try {
        const metadata: any = { fileName: file_name };       
    
        // Создаем FormData и добавляем метаданные и файл
        const formData = new FormData();
        formData.append('metadata', JSON.stringify(metadata));
        formData.append('file', fs.createReadStream(`${file_path}/${file_name}`), { filename: file_name });
        
        const task_id_opj = checkTaskID(Number(task_id))
        // Отправляем POST-запрос на /api/v3/work_packages/49/attachments
        // console.log("task_id_opj=================", formData, task_id_opj, file_name, file_path);
        const response = await axios.post(`http://localhost:8080/api/v3/work_packages/${task_id_opj}/attachments`, formData, {
          headers: {
            ...formData.getHeaders(),
          },
          auth: {
            username: 'apikey',
            password: '9b58c13ff1051fb65108878e945627f822b38efd9878071022855017246be55e',
          },
        });
    
        // Обрабатываем ответ от сервера
        // console.log(response.data);
        
        // Вернуть ответ клиенту
        
      } catch (error) {
        // console.error(error);
       
      }
}