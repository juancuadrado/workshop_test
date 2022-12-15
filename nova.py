import requests
import keystone

def list_flavors():
    nova_port = '8774/v2.1'

    env_url = 'https://api-uat-001.ormuco.com'

    flavors = requests.get(url=f"{env_url}:{nova_port}/flavors", headers=keystone.login())

    flavors = flavors.json().get('flavors')
    return flavors


def list_keypairs():

    nova_port = '8774/v2.1'

    env_url = 'https://api-uat-001.ormuco.com'

    key_pairs = requests.get(url=f"{env_url}:{nova_port}/os-keypairs", headers=keystone.login())

    key_pairs = key_pairs.json().get('keypairs')

    key_pairs = [k.get('keypair') for k in key_pairs]

    return key_pairs

#las funciones van en minuscula y las clases en mayusculas
def list_security():
    nova_port = '8774/v2.1'

    env_url = 'https://api-uat-001.ormuco.com'

    security_g = requests.get(url=f"{env_url}:{nova_port}/os-security-groups", headers=keystone.login())

    security_g = security_g.json().get('security_groups')

    return security_g


def create_server(server_specifications):
    
    nova_port = '8774/v2.1'

    env_url = 'https://api-uat-001.ormuco.com'

    server_on_cloud = requests.post(url=f"{env_url}:{nova_port}/servers", json=server_specifications, headers=keystone.login())

    print(server_on_cloud.reason)
    print(server_on_cloud.text)
    return print(f"{server_on_cloud.text} - {server_on_cloud.reason}") 

""""
def server_specs(wanted, originals):
    for original in originals:
        if wanted in original.get('name'):
            name_specs = {
                'name': original.get('name'),
                'id'  : original.get('id')
                }  
    return   name_specs
"""
