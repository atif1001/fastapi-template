# Setup

## Create python virtual environment
`virtualenv -p python3 venv_1_fastapi-template`

`source venv_1_fastapi-template/bin/activate`

## Install Fast API & Server
`pip install fastapi`

`pip install uvicorn`

# Configuration
`pip freeze > requirements.txt`

# Usage
Inside the app directory (where you main file, entry point to FastAPI lives) execute the following command to start server pointing to the module `main` and object `app`:

`uvicorn main:app --reload` 
