from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
async def adsf():
    return {"jabber": "wock"}
