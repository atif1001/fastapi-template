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
To install latest versions: `pip install fastapi uvicorn flake8 python-multipart python-dotenv`

OR 

install exact versions at time of development: `pip install -r requirements.txt`

Pip install this app itself: `pip install -e .`
*This required to support importing python root level package. Using command above we are installing this app in editable state in the root folder using dot (.)*

To generate pip requirements file: `pip freeze > requirements.txt`


# Configuration
- Copy `.env-SAMPLE` file to `.env` and populate values.


# Usage

## Start server
Inside the `app` directory execute the following command to start server pointing to the module `main` and object `app`:

`cd app`

`uvicorn main:app --reload` 

## API Documentation Swagger & ReDoc
Once server is started, API docs can be found at:

Swagger: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


# Developmet

## Add new configuration option
- Add an attribute to `config.py` file
- If value for new configuration is not "Optional" then add it to `.env` file.

## Add new API endpoints
- Create a new folder in `app/api/` directory.
- Add `__init__.py` file to it.
- Add API version folder. e.g. `app/api/v1/`
- Add `__init__.py` file to it.
- Create `main.py` file.
- Add `router = APIRouter()` to the file along with code for APIs.
- Import & include router in `app/api/apiv[N].py` file.
- New API endpoints will now be available, and added to Swagger & ReDoc.