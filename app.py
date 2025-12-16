from flask import Flask
from flask_restful import Api, Resource
from Routes import *
#Importaremos las librerias necesarias para nuestro proyecto, siempre en la parte superior
#Importaremos desde flask la clase FLask, ya que FLask es una clase
#Importamos las rutas para obtener la funcion que hicimos

app = Flask(__name__)
#Se crea el objeto tipo Flask

#Crearemos un objeto tipo api, como argumento le brindamos el objeto app
api = Api(app)
#La appi funciona para comunicarnos con el servidor y obtener una respuesta

#Mandamos llamar la funcion que hicimos y le damos como argumento "api"
crear_rutas(api)


#Se usa IF para evitar que el codigo ejecute el servidor cuando se importe este archivo
#Es una buena practica
if __name__ == '__main__':
    app.run(port=8090,debug=True)
    #Estamos Ejecutando el servidor con puerto 8090