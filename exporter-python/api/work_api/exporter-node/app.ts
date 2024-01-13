

// app.ts
import express, { Request, Response } from 'express';
import * as fs from 'fs';
import path from 'path';


import fileUpload from 'express-fileupload';
import { create_file_openprojectname } from './create_file_opj';
import { get_tasks_openproject } from './get_tasks_openproject';
import readTasksFile from './readTasksFile';
import { get_file_folder_tasks } from './get_file_folder_task';


const app = express();
const PORT = 8090;

app.use(fileUpload());



// Endpoint для отправки запроса
app.get('/get_tasks_openproject', async (req: Request, res: Response) => {
    try {
       // Initialize existingData
    //    const delay = (ms:any) => new Promise(resolve => setTimeout(resolve, ms));

       const existingData: any[] = [];

       for (let i = 0; i <= 2500; i++) {
         try {
           // Fetch tasks from OpenProject for each value of i
           const randomDelay = Math.floor(Math.random() * (3000 - 1000 + 1)) + 1000;
    //   await delay(randomDelay);
           const task: any = await get_tasks_openproject(i);
       
           if (task) {
             console.log("RES==:",i, task.id, task.title);
           

       
             // Append new data to the existing content
             existingData.push({ id: task.id, title: task.title });
             
           }
         } catch (error) {
           console.error(error);
         }
       }
       
       // Write the updated data back to the file
       const jsonData: any = JSON.stringify(existingData, null, 2);
       
       // Write the JSON data to the file
       const filePath = path.join(__dirname, 'openproject_tasks.json');
       
       fs.writeFile(filePath, jsonData, (err) => {
         if (err) {
           return console.error('Error writing to file:', err);
         }
         console.log('Data has been saved to', filePath);
       });
       
       console.log("The file was saved!");

        // Send JSON response directly     



        res.status(200).json({ message: 'Request sent successfully' });
    } catch (error) {
        // console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }

});

app.get('/start', async (req: Request, res: Response) => {
    try {


const filePathTasks = path.join(__dirname, 'tasks_bx24.json');

const  tasks = await readTasksFile(filePathTasks)

// Check if tasks is an array
if (Array.isArray(tasks)) {
  for (const task of tasks) {
    // Access the 'ID' property of each task
    const taskId = task.ID;
    await get_file_folder_tasks(taskId)
    
  }
} else {
  console.error('Invalid format: tasks is not an array.');
}

// console.log('Server is running a tasks', tasks)

  

        

        res.status(200).json({ message: 'Request sent successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }

});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}/start`);
});
