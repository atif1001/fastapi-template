from fastapi import APIRouter

# Importing routers for API features
from api.health_check.v1.main import router as router_v1_health_check
from api.auth.v1.main import router as router_v1_auth
from api.demo_feature_1.v1.main import router as router_v1_demo_feature_1
from api.admin.v1.main import router as router_v1_admin


# API Version 1 Router
router_api_v1 = APIRouter(prefix='/api/v1')

router_api_v1.include_router(router_v1_health_check, tags=['Health Check'])
router_api_v1.include_router(router_v1_auth, tags=['Auth'])
router_api_v1.include_router(router_v1_demo_feature_1, tags=['Demo Feature 1'])
router_api_v1.include_router(router_v1_admin, tags=['Admin'])
