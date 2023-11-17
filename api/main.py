import uvicorn
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from f2b import ban_ip, unban_ip, get_jails, get_jail

app = FastAPI()
api_host = "0.0.0.0"
api_port = 8999

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

@app.get("/jails")
def read_jails():
    return(get_jails())

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

if __name__ == "__main__":
    uvicorn.run("main:app", host=api_host, port=api_port, reload=True)
