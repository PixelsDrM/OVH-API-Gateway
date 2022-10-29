# OVH-API-Gateway
## FastAPI Gateway to OVH API

### Get your API keys here: 
https://eu.api.ovh.com/createToken/

### Setup your python environment
```bash
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

### Declare your API keys in a .env file
```bash
cp .env.example .env
```

### Run the server
```bash
uvicorn main:app --reload
```

## Or use docker
```bash
docker build -t ovh-api-gateway .
docker run -d --restart always -p 80:80 --name ovh-api-gateway ovh-api-gateway
```

## OVH Endpoints used in this project
```
GET /domain/zone
GET /domain/zone/{zoneName}
GET /domain/zone/{zoneName}/record
POST /domain/zone/{zoneName}/record
GET /domain/zone/{zoneName}/record/{id}
PUT /domain/zone/{zoneName}/record/{id}
DELETE /domain/zone/{zoneName}/record/{id}
POST /domain/zone/{zoneName}/refresh
```