# django_todo

1. To build image
  docker -build -t django_todo .
2. to run image
  docker run -p 8000:8000 django_todo gunicorn django_project.wsgi --bind 0.0.0.0:8000
  
3. Create a user 
  curl --location --request POST 'http://127.0.0.1:8000/register/' \
  --header 'Content-Type: application/json' \
  --data-raw '{"email": "USER_EMAIL","password": "USER_PASSWORD"
  }'

4. Get a token 
  curl --location --request POST '127.0.0.1:8000/api/token/' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'email=USER_EMAIL' \
  --data-urlencode 'password=USER_PASSWORD'

5. Add a task 
  curl --location --request POST 'http://127.0.0.1:8000/tasks/' \
  --header 'Authorization: Bearer ACCESS_TOKEN' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'text=TEXT_VALUE' \
  --data-urlencode 'is_completed=BOOL_VALUE' \
  --data-urlencode 'completed_date=DATE_VALUE(YYYY-MM-DD)' \
  --data-urlencode 'title=TEXT_VALUE'

6. Get all the tasks where author is token owner
  curl --location --request GET '127.0.0.1:8000/tasks/' \
  --header 'Authorization: Bearer USER_TOKEN'

7. Get one task IF created by token owner
  curl --location --request GET '127.0.0.1:8000/tasks/TASK_ID' \
  --header 'Authorization: Bearer USER_TOKEN'

8. Mark task as completed(irreversible)
  curl --location --request PUT '127.0.0.1:8000/tasks/TASK_ID/' \
  --header 'Authorization: Bearer USER_TOKEN' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'is_completed=True'

9. Delete a task 
  curl --location --request DELETE '127.0.0.1:8000/tasks/TASK_ID/' \
  --header 'Authorization: Bearer USER_TOKEN'
