# dpdzerobackend
This is a small crud operation project where i have used token authentication and have all functionality related to crud, the project is developed in django

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

pipenv install

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
