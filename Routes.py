# Este es el apartado de las Rutas
from Resources import *
#Importamos los recursos de nuestro otro documento (Resources)
#para poder ocupar las clases que tenemos en ese archivo


#Le damos como argumento "api" para que en el documento app pueda ejecutarse sin problemas
def crear_rutas(api):

    #Lo que hace esto es ejecutar un recurso en especifico en la ruta definida "/hola"
    api.add_resource(Login, '/login')

    api.add_resource(PantallaInicio, '/')

    api.add_resource(Signup, '/signup')

    #EL "/" define la ruta de incio en los sitios web