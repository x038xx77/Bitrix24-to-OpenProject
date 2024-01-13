// taskModule.js
import fs from 'fs';
import path from 'path';

function readTasksFile(filePath: string): Promise<any> {
  return new Promise((resolve, reject) => {
    // Read the file
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(`Error reading file: ${err}`);
        return;
      }

      try {
        // Parse the JSON content
        const tasks = JSON.parse(data);

        // Return the parsed tasks data
        resolve(tasks);
      } catch (parseError) {
        reject(`Error parsing JSON: ${parseError}`);
      }
    });
  });
}

export default readTasksFile;

