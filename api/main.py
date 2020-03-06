import uvicorn
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from _defs import main, get_jail
from f2b import ban_ip, unban_ip, generate_files

app = FastAPI()
api_host = "localhost"
api_port = 8000

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    ip: str
    jail: str

@app.get("/")
def read_root():
    uri = 'http://{}:{}/openapi.json'.format(api_host, api_port)
    r = requests.get(uri)
    return(r.json()['paths'])

@app.get("/jails")
def read_jails():
    m = main()
    return(m)

@app.get("/jail/{jail}")
def read_jail(jail):
    jail_data = get_jail(jail)
    return (jail_data)

@app.post("/ban")
async def ip_ban(item: Item):
    ban = ban_ip(item.ip, item.jail)
    return item 

@app.post("/unban")
async def ip_unban(item: Item):
    unban = unban_ip(item.ip, item.jail)
    return item  

@app.get("/refresh")
def refresh():
    generate_files()
    return "OK" 

if __name__ == "__main__":
    uvicorn.run("main:app", host=api_host, port=api_port, reload=True)