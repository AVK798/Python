import requests
from requests.auth import HTTPBasicAuth
import json

url = 'http;//sample.com'
Token=''

Auth=HTTPBasicAuth('Name@gamil.com', Token)
headers={
    "Content-type": 'Applcation/json',
    "Accept": "Applciation/json"

}
response=requests.request("Get", url, headers=headers, auth=Auth)

data = json.loads(response.txt)
Name= data[0]["Name"]
print(Name)