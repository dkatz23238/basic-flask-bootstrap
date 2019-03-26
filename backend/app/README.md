# Backend API Docs

This specifies behaviour of REST API backend.

# Endpoints
## ``` /api/tables?token=<token>```
    - GET Returns a list of tables in JSON format:
        {"table_names": ["bots", "users", "botevents"]} 
        
 ##  ```api/users```
    - GET api/users?username=<username> returns JSON user data.
    - POST api/users with JSON data to create User: {"username": <username>, "password": <password>}

 ##  ```api/roboticprocessautomations```
    - GET api/roboticprocessautomations?rpa_id=<rpa_id> returns JSON rpa data.
    - GET api/roboticprocessautomations returns JSON for all rpa data.
    - POST api/roboticprocessautomations to create new rpa. JSON needs to have following fields: ['cron_fmat_schedule', 'git_repository', 'rpa_name']


 ##  ```api/events```
    - GET api/events?rpa_id=<rpa_id> returns JSON events for single rpa.
    - GET api/events returns JSON for all events data.
    - POST api/events to create new event. JSON needs to have following fields: ['message', 'rpa_id', 'status']


# Output Of Tests
``` json
USERS POST
{
    "password": "test1", 
    "user_id": "e9eb4e28-1707-4cd8-9f4b-63c170bb2266", 
    "username": "test1"
}

USERS GET
{
    "password": "test1", 
    "user_id": "e9eb4e28-1707-4cd8-9f4b-63c170bb2266", 
    "username": "test1"
}

RPA POST
{
    "creation_date": "2019-03-26 15:41:06.841479", 
    "cron_fmat_schedule": "0 0 * * 0", 
    "git_repository": "githib.com", 
    "rpa_id": "f46ad989-2cff-4bae-869a-60525c54ab91", 
    "rpa_name": "rpa"
}

RPA GET
{
    "creation_date": "2019-03-26 15:41:06.841479", 
    "cron_fmat_schedule": "0 0 * * 0", 
    "git_repository": "githib.com", 
    "rpa_id": "f46ad989-2cff-4bae-869a-60525c54ab91", 
    "rpa_name": "rpa"
}

EVENT POST
{
    "event_datetime": "2019-03-26 15:41:06.857679", 
    "event_id": "3c188caf-ec7e-4717-9ebf-f00b6641048a", 
    "message": "STARTED", 
    "rpa_id": "f46ad989-2cff-4bae-869a-60525c54ab91", 
    "tag": "execution"
}

[
    {
        "event_datetime": "2019-03-26 15:41:06.857679", 
        "event_id": "3c188caf-ec7e-4717-9ebf-f00b6641048a", 
        "message": "STARTED", 
        "rpa_id": "f46ad989-2cff-4bae-869a-60525c54ab91", 
        "tag": "execution"
    }
]
```