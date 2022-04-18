from turtle import title
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import Settings
from tkinter import *
from tkinter import ttk
from turtle import title
# postgres
from . import models
import socket
import sys
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
settings = Settings()
# impot models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
# my_posts = [{"title": "fastapi", "content": "permier chapitre", "id": 1}, {
# "title": "fastapi mmm", "content": "permier chapitre", "id": 2}]


# def find_post(id):
# for p in my_posts:
#  if p["id"] == id:
# return p


# def find_index_post(id):
# for i, p in enumerate(my_posts):
# if p['id'] == id:
# return i


hostname = socket.gethostname()

version = f"{sys.version_info.major}.{sys.version_info.minor}"


@app.get("/")
async def read_root():
    return {
        "name": "my-app",
        "host": hostname,
        "version": f"Hello world! From FastAPI running on Uvicorn. Using Python {version}"
    }

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
