import uvicorn
from fastapi import FastAPI

from config import get_settings
from app.libs.logging import logger
from api.apiv1 import router_api_v1
from api.apiv2 import router_api_v2


config = get_settings()

# Main app instance
app = FastAPI(title=config.APP_NAME)

# Include multiple versions of APIs in the main app
app.include_router(router_api_v1)
app.include_router(router_api_v2)


@app.get('/')
async def root():
    return {'message': 'Hello World...'}


if config.ENVIRONMENT in 'development':
    uv_reload = 'True'
    uv_debug = 'True'
else:
    uv_reload = 'False'
    uv_debug = 'False'

if __name__ == "__main__":
    logger.debug("FasAPI Template")
    uvicorn.run("main:app",
                host='0.0.0.0',
                port=config.PORT,
                reload=uv_reload,
                debug=uv_debug,
                workers=5
                )
