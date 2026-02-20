from itertools import product
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Pydantic model to define the schema of the data for PUT, POST, & DELETE
class Products(BaseModel):
    ProductID: int
    Name: str


@app.get("/")
def root():
    return {"message": "some assignment"}