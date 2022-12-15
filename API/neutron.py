import requests
import API.keystone as keystone

def list_networks():

    neutron_port = '9696'

    env_url = 'https://api-uat-001.ormuco.com'

    networks = requests.get(url=f"{env_url}:{neutron_port}/v2.0/networks", headers=keystone.login())

    networks = networks.json().get('networks')
    
    return networks