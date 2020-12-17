from fastapi import APIRouter

# Importing routers for API features
from api.health_check.v1.main import router as router_v1_health_check


# API Version 2 Router
router_api_v2 = APIRouter(prefix='/api/v2')

router_api_v2.include_router(router_v1_health_check, tags=['Health Check'])
