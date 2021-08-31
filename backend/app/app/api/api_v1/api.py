from fastapi import APIRouter

from app.api.api_v1.endpoints import personalities, login, users, utils, comments, health

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(personalities.router, prefix="/personalities", tags=["personalities"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
