import fs from 'fs';
import path from 'path';
import { create_file_openprojectname } from './create_file_opj';

export async function get_file_folder_tasks(id_task_bx24: any) {
  const folderPath = path.join(__dirname, `data-bx24/${id_task_bx24}`);

  // Check if the folder exists
  if (fs.existsSync(folderPath)) {
    // Read the contents of the folder
    fs.readdir(folderPath, (err, files) => {
      if (err) {
        console.error('Error reading folder:', err);
        return;
      }

      // Log the file names
      console.log(`Files in folder ${id_task_bx24}:`);
      files.forEach((file) => {
        console.log(file);
        create_file_openprojectname(id_task_bx24, folderPath, file);
      });
    });
  } else {
    console.log(`Folder ${id_task_bx24} does not exist.`);
  }
}

// Example usage
// const exampleId = 'exampleTaskId';
// get_file_folder_tasks(exampleId);
