from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from wtforms.csrf.session import SessionCSRF
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import jsonify
import forms
from wtforms.widgets import html_params
import sqlite3
from sqlite3 import Error




datos_ordenesdb= r'C:\\Users\\Usuario\\Documents\\Nueva carpeta\\asdasd-main\\Mantienimiento SAP\\App_Ordenes_Mtto\\base_de_datos_ordenes.db'



app = Flask(__name__)
app.secret_key = 'mi_clave'
csrf = SessionCSRF()


@app.route("/", methods = ["GET","POST"])
def login():
    
    titulo = "Inicio_de_sesion"
    login_form = forms.login(request.form)
    
   
    
    if request.method == "POST" and login_form.validate():
        
        usuario = login_form.usuario.data.lower()
        clave = login_form.clave.data
        connect=sqlite3.connect(datos_ordenesdb)
        cursor= connect.cursor()
        sentencia= (""" SELECT usuario, contraseña from usuarios where usuario = ?"""  
        )
        tabla=cursor.execute(sentencia, (usuario,))
        tabla=tabla.fetchone()
        connect.commit()
        connect.close()
        try:
            contraseña= tabla[1]
            user= tabla[0]
        except:
            contraseña=None
        if clave == contraseña and user is not None:
            session['user']=usuario
            return  redirect(url_for ('orden_mantenimiento'))
            
        else:
        
            pass
       
    return render_template("index.html", titulo=titulo,form = login_form)

@app.route("/orden", methods = ["GET", "POST"])
def orden_mantenimiento():
    titulo = "orden_mantenimiento"
    orden_form = forms.orden_mantenimiento(request.form)
    if request.method== "POST":
        orden=orden_form.orden.data.lower()
       
        return redirect(url_for('pagina_3'))
    return render_template("indexformulario.html",titulo=titulo, form=orden_form)
 

@app.route("/pagina_3", methods = ["GET", "POST"])

def pagina_3():
    datos_form= forms.pagina_3(request.form)
    titulo= "pagina_3"
    if request.method == "POST": 
        ficha = datos_form.ficha()

        return redirect(url_for('pagina_3'))
    return render_template("pagina_3.html", form=datos_form)



        

    
if __name__ == "__main__":
    
	app.run(debug=True, port=5000, host="0.0.0.0")
        
        