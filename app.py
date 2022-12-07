# importamos la libreria Flask
from flask import Flask, render_template
import requests

# instanciamos la aplicaion
app = Flask(__name__)

@app.route("/")     # ruta de la pag principal
def hola_mundo():
    return "Hola, bootcamp Hernan. Como estan?"

@app.route("/bienvenida")   # ruta de bienvenida
def bienvenida():
    return "Bienvenidos al bootcamp"

@app.route("/enrique")
def enrique():
    return '''<h1>Bienvenido</h1>
              <p>El bootcamp es de Python</p>
              <p> Estoy aca porque me gusta aprender </p>
              '''

# cresr nuevo endpoint para recibit datos del navegador
# @app.route("/contrasenha/<usuario>")
# def validar(usuario):
#     if usuario == "Enri":
#         return f"Bienvenido {usuario}"
    
# Solucion de Renato
# @app.route("/usuario/<usuario>/<contrasenha>")
# def verificar(usuario , contrasenha):

#     if usuario == "rena" and contrasenha == "1234":
#         return f"Bienvenido a tu usuario {usuario} <br> tenemos nuevas notificaciones para vos"

# Solucion de Nikola
@app.route("/arturo/<usuario>/<contrasenha>")# Nomenclatura para chupar datos del navegador
def probar(usuario,contrasenha):
    if usuario == "Arturo" and contrasenha == "123":
        if contrasenha == "123":
            return f"Bienvenido {usuario}"
        else:
            return f"{usuario} error de contraseña"
    else:
        return "Error en carga de usuario"

# Solucion Esteban
@app.route('/usuario/<usuario>/<contrasenha>')
def validar(usuario, contrasenha): 
    if usuario == 'Juan' and contrasenha == 'chinchulin':
        return f'Bienvenido {usuario}' 
    else:
        return 'usuario invalido'

# Snatiguay

@app.route("/validacion/<usuario>/<contrasenha>")
def validacion_de_datos(usuario,contrasenha):
    if usuario=="Santi" and contrasenha=="12345678":
        return(f"<script>alert('bienvenido {usuario}.');</script>")
    else:
        return('''<script>alert('acceso incorrecto.');
        let usuario = prompt("ingresa nuevamente el usuario.");
        let contrasenha= prompt("ingresa nuevamente el usuario.");
        while(true){
        usuario = prompt("ingresa nuevamente el usuario.");
        contrasenha= prompt("ingresa nuevamente la contrasenha.");
        if (usuario=="Santi" && contrasenha=="12345678"){
            alert('bienvenido '+ usuario);
            break;
        }
        } </script>''')

@app.route("/personaje/")
def personaje():
    personaje = requests.get("https://rickandmortyapi.com/api/character/1").json()
    return render_template("index.html", personaje=personaje )


if __name__ == "__main__":
    app.run(debug=True)