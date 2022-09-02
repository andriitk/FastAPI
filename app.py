from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import IPs

engine = create_engine('sqlite:///ips.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = FastAPI()


@app.get("/")
async def index():
    data = session.query(IPs).all()
    json_data_all = {}

    for i in data:
        json_data = {}
        json_data["source"] = i.resource
        json_data["ip"] = i.ip
        json_data_all[f"{i.id}"] = json_data
    return json_data_all
