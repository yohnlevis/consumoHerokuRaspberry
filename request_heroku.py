import requests
import json
"""url = 'https://apirestprof1cloaiza.herokuapp.com/api/animal'
r = requests.get(url)
print(json.loads(r.content))"""

API_ENDPOINT = "https://apirestprof1cloaiza.herokuapp.com/"
url = "{0}{1}".format(API_ENDPOINT,'api/usuario/autenticar')
headers = {'Content-type':'application/json'}
data = {'email':'carloaiza@umanizales.edu.co','password':'123456'}

req = requests.post(url, data=json.dumps(data),headers= headers)
if req.status_code>=200 and req.status_code < 300: 
    pass
else:
    print("Error al intentar obtener el token", req.status_code, req.content.decode('utf-8'))

animal_service= "{0}{1}".format(API_ENDPOINT,'api/animal')
auth= "Bearer {0}".format(req.json()['token']['access_token'])
headers= {'Content-type':'application/json','Authorization':auth}
req = requests.get(animal_service,headers= headers)
if req.status_code>=200 and req.status_code < 300:
    print(json.loads(req.content))
else:
    print("Error al intentar los animales" , req.status_code, req.content.decode('utf-8'))
          
    

