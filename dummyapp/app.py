from fastapi import FastAPI
from dummyapp.bar.app import router as bar_router
from dummyapp.foo.app import router as foo_router


app = FastAPI()
app.include_router(foo_router, prefix="/foo")
app.include_router(bar_router, prefix="/bar")


@app.get("/")
async def hi():
    return {"hello": "world"}
