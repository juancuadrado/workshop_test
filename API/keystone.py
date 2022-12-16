import requests


#Define class to load but later

def login():
    env_url = 'https://api-uat-001.ormuco.com'
    keystone_port = '5000'
    payload = {
        "auth": {
         "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "workshop2022@utb.edu.co",
                        "domain": {
                            "name": "Default"
                     },
                      "password": "XXXXXXX"
                 }
                }
            }
        }
    }
    data = requests.post(url=f"{env_url}:{keystone_port}/v3/auth/tokens", json=payload).json().get('token')
    print(data.get('id'))
    return {'X-Auth-Token':data.get('id')}
