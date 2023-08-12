# dpdzerobackend
This is a small crud operation project where i have used token authentication and have all functionality related to crud, the project is developed in django

Deployed on here you can check in this link 

http://20.219.91.55:8000/index/ 

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 is installed (you can download it from https://www.python.org/downloads/)
- Pipenv is installed (`pip install pipenv`)
- Docker version 24.0.2 is installed (you can download it from https://docs.docker.com/get-docker/)
- Docker Compose version 1.23.2 is installed (you can download it from https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to set up and run the project:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/project.git
   cd project

2. Create a virtual environment and install dependencies:

```sh 
sudo apt install pipenv
```
3. Activate the virtual environment:

  ```sh 
  pipenv shell
  ```

4. Build and start the Docker containers:

 ```sh
     docker-compose build
     docker-compose up
```

Access the application in your web browser at http://localhost:8000


**Configuring Docker and Docker Compose**
If you're new to Docker and Docker Compose, follow these steps to get started:
1. Download and Install Docker:

Go to https://docs.docker.com/get-docker/
Choose the appropriate version for your operating system and follow the installation instructions.

2. Verify Docker Installation:

Open a terminal and run:
  ```sh
    docker --version
  ```
3. Download and Install Docker Compose:

   
*Go to https://docs.docker.com/compose/install/*

*Choose the appropriate installation method for your operating system and follow the instructions.*

4. Verify Docker Compose Installation:

Open a terminal and run:
```sh 
docker-compose --version
```

## Also Note:

In the settings.py file, configure the database settings based on your preferences. Additionally, ensure that you make the corresponding adjustments in the docker-compose.yml file.

## Troubleshooting


If you encounter any issues during setup or while running the project, feel free to open an issue on GitHub.


## Using Endpoint 

**/index/**

Method: GET

Description: This endpoint returns a simple "Hello world" message.

Request:
```sh 
GET /index/
```

Response:
```sh{
    "Hello": "Hello world"
}
```

**/register/**

Method: POST

Description: This endpoint is used to register a new user.

Request:
```sh
POST /register/

Request Body:
{
    "username": "new_user",
    "password": "new_password"
}
```
Response (Success):
```sh
{
    "status": "success",
    "message": "User successfully registered!",
    "data": {
        "username": "new_user",
        "password": "new_password"
    }
}
```
Response (Error):
```sh
{
    "username": [
        "This field is required."
    ],
    "password": [
        "This field is required."
    ]
}
```

**Endpoint:/token/**

Method: POST

Description: This endpoint is used to authenticate a user and generate an access token.

Request:
```sh
POST /token/

Request Body:
{
    "username": "existing_user",
    "password": "existing_password"
}
```

Response (Success):

```sh
{
    "status": "success",
    "message": "Access token generated successfully",
    "data": {
        "username": "existing_user",
        "password": "existing_password"
    },
    "token": "Bearer <access_token>"
}
```

Response (Error):
```sh
{
    "message": "Invalid Credentials",
    "data": {
        "username": "invalid_user",
        "password": "invalid_password"
    }
}

```

**Endpoint: /data/**

Method: POST

Description: This endpoint is used to store data.

Request:
```sh
POST /data/

Request Body:
{
    "key": "unique_key",
    "value": "data_value"
}
```
Response (Success):
```sh
{
    "status": "success",
    "message": "Data stored successfully."
}
```
Response (Error):
```sh
{
    "key": [
        "This field is required."
    ],
    "value": [
        "This field is required."
    ]
}
```
**Endpoint: /getdata/**

Method: GET

Description: This endpoint retrieves stored data based on a provided key.

Request:
```sh
GET /getdata/?key=unique_key
```
Response (Success):

```sh
{
    "status": "success",
    "data": [
        {
            "key": "unique_key",
            "value": "data_value"
        }
    ]
}
```
Response (Error):

```sh
{
    "message": "Key parameter missing."
}
```
**Endpoint: /updatedata/**

Method: PUT

Description: This endpoint updates stored data based on a provided key.

Request:
```sh
PUT /updatedata/

Request Body:
{
    "key": "unique_key",
    "value": "updated_data_value"
}
```

Response (Success):

```sh
{
    "status": "success",
    "message": "Data updated successfully."
}
```
Response (Error):
```sh
{
    "key": [
        "This field is required."
    ],
    "value": [
        "This field is required."
    ]
}
```
**Endpoint: /delete/**

Method: DELETE

Description: This endpoint deletes stored data based on a provided key.

Request:
```sh 
DELETE /delete/?key=unique_key
```
Response (Success):
```
{
    "status": "success",
    "message": "Data entry deleted successfully."
}
```
Response (Error):
```sh 
{
    "message": "Key parameter missing."
}
```
