#Esta es el apartado de los recursos
from flask_restful import Resource
from flask import make_response, render_template
#Definimos una clase tipo flask que nos permita devolver un recurso
#dicho recursos sera aquel que nosotros definamos como programadores

class PantallaInicio(Resource):
    def get(self):
        #Renderizamos el contenido en un html
        contenido = render_template("index.html")
        #Retornamos el contenido renderizado en una respuesta
        return make_response(contenido)

class Login(Resource):
    def get(self):

        contenido = render_template("login.html")

        return make_response(contenido)

class Signup(Resource):
    def get(self):

        contenido = render_template("Signup.html")

        return make_response(contenido)
