from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
async def adsf():
    return {"fiddle": "sticks"}
