import axios from 'axios';

export async function get_tasks_openproject(id_task:number) {


    try {

    const url = `http://pr.inntechsys.ru:3580/api/v3/work_packages/${id_task}`


    const response = await axios.get(url, {

        // URL_OPENPROJECT = 'http://pr.inntechsys.ru:3580'
// API_KEY="apikey:511424e29736aa738bde3e8c6deee6647bf6391ba7aa4f3bccb1c5939fc690f4"
          
          auth: {
            username: 'apikey',
            password: '511424e29736aa738bde3e8c6deee6647bf6391ba7aa4f3bccb1c5939fc690f4',
          },
        });
   
    
    if(response.status === 200) {
        const result = {
            "id":response?.data.id,
            "title": response?.data.subject,
        }
        return result
    }
}catch(err){console.log("Err GET TASK", id_task)}
    
}