from fastapi import FastAPI, Path, Query
from fastapi.encoders import jsonable_encoder
import requests
import json
from typing import Union
from typing import Optional

app = FastAPI()


base_url = 'http://192.168.1.75:5000/users'

@app.get(path='/')
async def healthCheck():
    return "OK"

@app.get(path='/users')
async def getUsers():
    response = requests.get(base_url)
    return response.json()

@app.post(path='/users')
async def postUsers(id:str, name:str):
    data = dict(id=id, name=name)
    response = requests.post(base_url, json=data)
    return response.json()

@app.get(path='/users/params')
async def user_params(id:Optional[str]=None, name:Optional[str]=None):
    if (id is None) and (name is None):
        return "id, name을 입력하세여"
    else:
        if id is None:
            params = '?name=' + name
        elif name is None:
            params = '?id=' + id
        else:
            params = '?name=' + name
            params += '?id=' + id
    
    url = base_url + params
    response = requests.get(url)

    return response.json()


@app.get(path='/users/data')
async def user_data(id:Optional[str]=None, name:Optional[str]=None):
    if (id is None) and (name is None):
        return "id, name을 입력하세여"
    else:
        if id is None:
            data = dict(name=name)
        elif name is None:
            data = dict(id=id)
        else:
            data=dict(id=id, name=name)
    response = requests.get(base_url, data)
    return response.json()



@app.get(path='/users/{id}')
async def users_param(id=str):
    url = base_url + '/' + id
    response = requests.get(url)
    return response.json()

# put - resource entire update
@app.get(path='/put/{id}')
async def putData(id:str, name:str):
    url = base_url + '/' + str(id)
    data = dict(id=id, name=name)
    response = requests.put(url, json=data)
    return response.json()

# patch - resource partitial update
@app.get(path='/patch/{id}')
async def patchData(id:str, name:str):
    url = base_url + '/' + str(id)
    data = dict(name=name)
    response = requests.patch(url, json=data)
    return response.json()

# delete
@app.get(path='/delete/{id}')
async def deleteData(id:str):
    url = base_url + '/' + str(id)
    data = dict(id=id)
    response = requests.delete(url, json=data)
    response = requests.get(base_url)
    return response.json()
