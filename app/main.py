from fastapi import FastAPI

from config import get_settings
from api.apiv1 import router_api_v1
from api.apiv2 import router_api_v2


config = get_settings()

# Main app instance
app = FastAPI(title=config.app_name)

# Include multiple versions of APIs in the main app
app.include_router(router_api_v1)
app.include_router(router_api_v2)


@app.get('/')
async def root():
    return {'message': 'Hello World'}
