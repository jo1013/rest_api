from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import dir_path
import csv
import pandas as pd
import application





class Item(BaseModel):
    userid : int
    recomand : List[str] = []
    


    
app = FastAPI()


@app.get("/")
async def read_root():
    return {"DOC": "교통사고 통계"}




@app.get("/{kind}/{year}/{doc}")
async def read_doc(kind: str , year:int, doc:str):
    t = application.APP.main(kind, year, doc)
    result = jsonable_encoder(t)
    return result


# @app.get("/bicycle")
# @app.get("/dawn")
# @app.get("/old")
# @app.get("/pedestrian")
# @app.get("/all")



if '__init__' == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)