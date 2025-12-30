#Esta es el apartado de los recursos
from flask_restful import Resource
from extensiones import inicializar_db
from flask import make_response, render_template, request
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

    #Aqui haremos una funcion con metodo post para poder recibir informacion
    def post(self):
        #aqui al recibir un post agregamos como diccionario los datos que reciba
        print("se ha recibido una peticion")
        datos = request.form.to_dict()
        print(datos)
        #aqui generamos una condicion que si coinciden las contraseñas arroja otra pagina que es la de inicio de sesion
        if datos["correo"] == "kiubo@correo.com" and datos["password"] == "123456":
            return make_response(render_template("sesioniniciada.html"))

class Signup(Resource):
    def get(self):

        contenido = render_template("Signup.html")

        return make_response(contenido)
    def post(self):
        print("se ha recibido una peticion")
        datos = request.form.to_dict()
        print(datos)
        #aqui generamos una condicion que si coinciden las contraseñas arroja otra pagina que es la de inicio de sesion
        if datos["passwordconfirmed"] == datos["password"]:
            return make_response(render_template("sesioniniciada.html"))