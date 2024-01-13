from create_open_project import create_openproject_projects_is_null 
import uuid

random_unique_ids = str(uuid.uuid4())
print(random_unique_ids)


create_openproject_projects_is_null(f'test-{random_unique_ids}', "PR NULL")