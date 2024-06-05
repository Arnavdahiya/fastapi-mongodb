from fastapi import FastAPI
from routes.user import router

app = FastAPI()

app.include_router(router, tags=["Product"], prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)