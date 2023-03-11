import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests

app = FastAPI()

origins = [
"http://localhost",
"http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=os.getenv('allow_origins'),
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{url_path:path}")
async def read_item(url_path):
    url = f"http://{url_path}"
    response = requests.get(url).json()
    return response["status"]

if __name__ == '__main__':
     uvicorn.run("main:app", port=5000, host="0.0.0.0", log_level="info")