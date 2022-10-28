from dotenv import load_dotenv
from fastapi import FastAPI
import os
import ovh

load_dotenv()

app = FastAPI()

ovh_application_key = os.getenv("OVH_APPLICATION_KEY")
ovh_application_secret = os.getenv("OVH_APPLICATION_SECRET")
ovh_consumer_key = os.getenv("OVH_CONSUMER_KEY")

client = ovh.Client(
    endpoint='ovh-eu',
    application_key=ovh_application_key,
    application_secret=ovh_application_secret,
    consumer_key=ovh_consumer_key,
)

@app.get("/")
async def root():
    return {"Application": "OVH API Gateway"}

@app.get("/domain/zone")
async def get_domain_zone():
    return client.get('/domain/zone')

@app.get("/domain/zone/{zoneName}")
async def get_domain_zone(zoneName: str):
    return client.get('/domain/zone/' + zoneName)

@app.get("/domain/zone/{zoneName}/record")
async def get_domain_zone_record(zoneName: str):
    return client.get('/domain/zone/' + zoneName + '/record')

@app.post("/domain/zone/{zoneName}/record")
async def post_domain_zone_record(zoneName: str, fieldType: str, subDomain: str, target: str, ttl: int):
    return client.post('/domain/zone/' + zoneName + '/record', fieldType=fieldType, subDomain=subDomain, target=target, ttl=ttl)

@app.get("/domain/zone/{zoneName}/record/{id}")
async def get_domain_zone_record_id(zoneName: str, id: int):
    return client.get('/domain/zone/' + zoneName + '/record/' + str(id))

@app.put("/domain/zone/{zoneName}/record/{id}")
async def put_domain_zone_record_id(zoneName: str, id: int, fieldType: str, subDomain: str, target: str, ttl: int):
    return client.put('/domain/zone/' + zoneName + '/record/' + str(id), fieldType=fieldType, subDomain=subDomain, target=target, ttl=ttl)

@app.delete("/domain/zone/{zoneName}/record/{id}")
async def delete_domain_zone_record_id(zoneName: str, id: int):
    return client.delete('/domain/zone/' + zoneName + '/record/' + str(id))

@app.post("/domain/zone/{zoneName}/refresh")
async def post_domain_zone_refresh(zoneName: str):
    return client.post('/domain/zone/' + zoneName + '/refresh')