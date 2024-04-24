from pymongo import mongo_client
import os.path
import json
import pydantic

pydantic.json.E

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
print('Connected to Mongodb...')

mydb = client['test']
mycol = mydb['testdb']

@app.get('/')
async def healthcheck():
    return "OK"

@app.get('/getmongo')
async def getMongo():
    data = list(mycol.find({}, {"_id":0}).limit(10))
    print(data)
    return data