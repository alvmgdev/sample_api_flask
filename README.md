# api_flask_sample

A sample to show that implement an API in Flask it is easy.

### PREREQUISITES

* Python 3
* CURL

### SETUP

1. Clone this repository
2. Open a terminal and move to the repository folder
3. Create a virtualenv:
    ```
    python3 -m venv .venv
    ```
4. Activate your virtualenv:
   ```
   Unix:
   source env/bin/activate

   Windows:
   .venv\Scripts\activate.bat
   ```
5. Install all dependencies:
    ```
    pip install -r requirements.txt
    ```
6. Launch the creation of the database:
    ```
    python create_db.py
    ```
    A file called app.db it was created by this script. (a db in sqlite format)
7. Launch the app:
    ```
    python run.py
    ```

### CHECK THE API IS RUNNING
1. Connect via web browser to http://localhost:5000 and you should see a hello world message

### USER ENDPOINTS. TEST WITH CURL
### Create user
```
curl -d '{ "username": "myuser", "email": "user@localhost" }' -H "Content-Type: application/json" -X POST http://localhost:5000/users
```
### Get users
```
curl -X GET http://localhost:5000/users
```
### Get user
```
curl -X GET http://localhost:5000/users/1
```
### Update user
```
curl -d '{ "username": "myusername", "email": "myusername@localhost" }' -H "Content-Type: application/json" -X PUT http://localhost:5000/users/1
```
### Delete user
```
curl -X DELETE http://localhost:5000/users/1
```

### Authors

* **Alvaro Merino Garcia**
