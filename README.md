# FastAPI Template
This codebase provides a basic structure to create an API micro-service using FastAPI. The starting point of the app is in `app/main.py`.
- **Folder/File structure:** The structure of this template supports *divisional* folder structure instead of *functional*. e.g., All the files related to an API endpoint (/api/v1/health-check) are in `api/health_check/v1/` folder. This app uses `APIRouter` from FastAPI to accomplish this. More details on how this works are at: https://fastapi.tiangolo.com/tutorial/bigger-applications/
- **API Versioning:** To version an API, we will create another python package (folder + \_\_init\_\_.py) inside app/api/{api_feature} folder with the folder name v[N] and include the router from the newly created API feature + version in app/main.py
- **Data Validation:** API request and response models are pydantic data models. FastAPI does data validation based on these models, plus generating Swagger & ReDoc documentation. More information on this at: https://fastapi.tiangolo.com/tutorial/body/

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