import os
from dotenv import load_dotenv

def config():
    # argumentos = {
    #     "user":"remoto",
    #     "password":"Ag0r4V4i!",
    #     "path":"0.0.0.0:3306",
    #     "bd":"padrao"
    # }
    
    load_dotenv()
    print(os.environ['DATABASE_USER'])
    argumentos = {
        "user": os.environ['DATABASE_USER'],
        "password": os.environ['DATABASE_PASSWORD'],
        "path": os.environ['DATABASE_PATH'],
        "bd": os.environ['DATABASE_DB']
    }
    return argumentos