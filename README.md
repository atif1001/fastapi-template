# Setup

## Create python virtual environment
`virtualenv -p python3 venv_1_fastapi_template`

`source venv_1_fastapi_template/bin/activate`

## Install Fast API & Server
`pip install fastapi uvicorn flake8 python-multipart`

# Configuration
`pip freeze > requirements.txt`

# Usage
## Start server
Inside the `app` directory execute the following command to start server pointing to the module `main` and object `app`:

`cd app`

`uvicorn main:app --reload` 

## API Documentation Swagger & ReDoc
Once server is started, API docs can be found at:

Swagger: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc