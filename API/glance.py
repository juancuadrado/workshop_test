import requests
import API.keystone as keystone

#Definir Clase
def list_images():

    glance_port = '9292'
    env_url = 'https://api-uat-001.ormuco.com'
    images = requests.get(url=f"{env_url}:{glance_port}/v2/images", headers=keystone.login())
    images = images.json().get('images')
    return images
