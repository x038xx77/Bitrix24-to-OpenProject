import fs from 'fs';
import path from 'path';

export function checkTaskID(task_id: number): number | null {
  const filePath = path.join(__dirname, 'tasks_idbx24_idop.json');

  try {
    // Read the file synchronously
    const data = fs.readFileSync(filePath, 'utf8');

    // Parse the JSON content
    const taskDataArray = JSON.parse(data);

    // Find the entry with the specified task_id
    const matchingTask = taskDataArray.find((taskData:any) => {
      const id = Object.keys(taskData)[0];
      return parseInt(id) === task_id;
    });

    // Return the value if the task_id is found, otherwise return null
    return matchingTask ? matchingTask[task_id.toString()] : null;
  } catch (error) {
    console.error('Error reading or parsing file:', error);
    return null;
  }
}

// Example usage
// const taskIdToCheck = 3898;
// const result = checkTaskID(taskIdToCheck);

// if (result !== null) {
//   console.log(`Value for Task ID ${taskIdToCheck}: ${result}`);
// } else {
//   console.log(`Task ID ${taskIdToCheck} not found or error occurred.`);
// }
