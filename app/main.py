from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    returnd {"Hello": "We Love Datascientest, and we did it. We build a CI/CD Pipeline !!"}
