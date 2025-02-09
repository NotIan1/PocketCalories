import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# http://127.0.0.1:8000/assets/products/almond_milk.jpg