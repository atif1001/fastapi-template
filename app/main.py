from fastapi import FastAPI, APIRouter

# Importing routers for API features
from api.health_check.v1.main import router as router_v1_health_check
from api.demo_feature_1.v1.main import router as router_v1_demo_feature_1
from api.admin.v1.main import router as router_v1_admin

# Main app instance
app = FastAPI(title='FastAPI Template')

# API Version 1 Router
router_api_v1 = APIRouter(prefix='/api/v1')
router_api_v1.include_router(router_v1_health_check, tags=['Health Check'])
router_api_v1.include_router(router_v1_demo_feature_1, tags=['Demo Feature 1'])
router_api_v1.include_router(router_v1_admin, tags=['Admin'])

# API Version 2 Router
# router_api_v2 = APIRouter(prefix='/api/v2')
# router_api_v2.include_router(router_v1_health_check, tags=['Health Check'])

# Include multiple versions of APIs in main app
app.include_router(router_api_v1)
# app.include_router(router_api_v2)


@app.get('/')
async def root():
    return {'message': 'Hello World'}
