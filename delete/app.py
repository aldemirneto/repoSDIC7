from ast import stmt
from unittest import result
from fastapi import FastAPI, Response
import config, json
from sqlalchemy import create_engine, select, text
import mysql.connector as mysql
import requests as rt



def deleta_dados():
    x = rt.get('http://0.0.0.0:5000')
    z = x._content 
    x = config.config()
    res = json.loads(z)
    user = x["user"]
    password = x["password"]
    path = x["path"]
    bd = x["bd"]
    engine  = create_engine(f'mysql+mysqlconnector://{user}:{password}@{path}/{bd}')
    with engine.connect() as conn:
            for x in res:
                result = conn.execute(text(f"delete from cliente where idcliente={x}"))
            conn.close()

    return 'deletado com sucesso'




#app = FastAPI()










if __name__ == "__main__":
    deleta_dados()
        