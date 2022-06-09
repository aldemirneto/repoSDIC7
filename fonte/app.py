from ast import stmt
from unittest import result
from fastapi import FastAPI, Response
import config
from sqlalchemy import create_engine, select, text
import mysql.connector as mysql




def return_list():
    x = config.config()
    user = x["user"]
    password = x["password"]
    path = x["path"]
    bd = x["bd"]
    engine  = create_engine(f'mysql+mysqlconnector://{user}:{password}@{path}/{bd}')
    with engine.connect() as conn:
            result = conn.execute(text("select u.idcliente, u.PrimeiroNome, p.ultimopagamento from cliente u inner join plano p on p.idcliente = u.idcliente;"))
            conn.close()
    return result.all()




app = FastAPI()


@app.get("/")
async def retorno():
    return return_list()




        