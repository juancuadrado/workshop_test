from flask import Flask 
from flask import request
import glance 
import nova
import neutron


app = Flask('Workshop Test')


@app.route("/")
def hello_world():
    return "hola mundo!"


#Request Info From The Ormuco API

@app.route("/G_I", methods=['GET'])
def Images():
    data = glance.list_images()
    print(data)
    return data


@app.route("/N_F", methods=['GET'])
def flavors():
    data = nova.list_flavors()
    print(data)
    return data

@app.route("/N_K", methods=['GET'])
def keypairs():
    data = nova.list_keypairs()
    print(data)
    return data


@app.route("/N_S", methods=['GET'])
def security_group():
    data = nova.list_security()
    print(data)
    return data   

@app.route("/N_N", methods=['GET'])
def networks():
    data = neutron.list_networks()
    print(data)
    return data   


@app.route("/server_data", methods=['GET'])
def server_data():

    data={}

    data['image'] = nova.server_specs('ubuntu-18.04-amd64', glance.list_images())

    data['network']  = nova.server_specs('default-network', neutron.list_networks())

    data['flavors'] = nova.server_specs('general.nano.uat.linux', nova.list_flavors())

    data['keypairs']  = nova.server_specs('juan_cuadrado', nova.list_keypairs())

    data['security_groups'] = nova.server_specs('juan_cuadrado', nova.list_security())
    
    return data
    

@app.route("/server", methods=['POST'])
def server_create():
    payload = request.get_json()
    nova.create_server(payload)
    return payload



#Create Selecction of the Componentes and print Payload

#Create Server API





##### Def Function to POST Login Openstack


##### Def Function to Get Data From Openstack


##### Def Function to Put New Items


##### Def Function to Images

#Flask es  super sencillo y liviano


###Prueba Mañana Hacer un API en un ANSENBILE O DOCKER para crear instancia
###server y demas caracteristicas.

### Prueba Mañana
#OPS posibles targets Server y demas caracteristicas.
#    
# 
# 

#Hacer flask con el script de lo que hicimos
#Api mandar el request y hacer que haga el login y crear una instancia
#Con todas las caracteristicas
#Puntos Extras: Frontend que consuma recursos del API
#Puntos Extras: Desde el 8 a 9
#Punto Ultra: Instalar ese servicio o pagina web dentro del portal

#El codigo en multiples archivos 

#Importar un archivo desde otro archivo __init__.py
#Y desde ese archivo importo las librearias importantes
#leer bien un utils o init 
