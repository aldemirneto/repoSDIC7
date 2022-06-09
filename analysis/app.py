from fastapi import FastAPI
import json
import logging
from pydantic import BaseModel
import requests as rt





def analisa():
    x = rt.get('http://0.0.0.0:5001')
    z = x._content 
    pessoas = json.loads(z)
    idcliente =[]
    for pessoa in pessoas:
        idcliente.append(pessoa["idcliente"])
    is_odd = list(filter(lambda n: n%2!=0, idcliente))
    print(is_odd)
    return is_odd
    


app = FastAPI()


@app.get("/")
async def retorno():
    return analisa()



