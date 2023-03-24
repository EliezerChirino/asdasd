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



ordenes_MttoBD= r'C:\\Users\\echirino\\Documents\\Proyecto N°1 ordnes mtto\\Mantienimiento SAP\\App_Ordenes_Mtto\\static\\db\\ordenes_Mtto.db'




app = Flask(__name__)
app.secret_key = 'mi_clave'
csrf = SessionCSRF()


@app.route("/", methods = ["GET","POST"])
def login():
    
    titulo = "Inicio_de_sesion"
    login_form = forms.login(request.form)
    
    
    
    if request.method == "POST" and login_form.validate():
        
        username = login_form.username.data.lower()
        clave = login_form.clave.data
        connect=sqlite3.connect(ordenes_MttoBD)
        cursor= connect.cursor()
        
        sentencia= (""" SELECT username, password from usuarios where username = ?"""  
        )
        
        tabla=cursor.execute(sentencia, (username,))
        tabla=tabla.fetchone()
        connect.commit()
        connect.close()
        try:
            password= tabla[1]
            username= tabla[0]
        except:
            password=None
        if clave == password and username is not None:
            session['user']=username
            return  redirect(url_for ('orden_mantenimiento'))
            
        else:
        
            pass
       
    return render_template("index.html", titulo=titulo,form = login_form)


@app.route("/orden", methods = ["GET", "POST"])
def orden_mantenimiento():
    titulo = "orden_mantenimiento"
    orden_form = forms.orden_mantenimiento(request.form)
    status_form= forms.orden_mantenimiento(request.form)
    descripcion_orden_form= forms.orden_mantenimiento(request.form)
    if request.method== "POST":
        
        orden=orden_form.orden.data
        status=status_form.status.data
        descripcion= descripcion_orden_form.descripcion_orden.data
    
        connect=sqlite3.connect(ordenes_MttoBD)
        cursor= connect.cursor()
        
        sentencia= (""" INSERT INTO ordenes (orden,status,decripcion_orden) VALUES (?,?,?)""" )
        cursor.execute(sentencia, ( orden, status, descripcion))
        connect.commit()
        connect.close()
        
       
        return redirect(url_for('pagina_3'))
    return render_template("indexformulario.html",titulo=titulo, form=orden_form)
 

@app.route("/pagina_3", methods = ["GET", "POST"])

def pagina_3():
    datos_form= forms.pagina_3(request.form)
    titulo= "pagina_3"
    puestos_d_trabajo_form = forms.pagina_3(request.form)
    ficha_form= forms.pagina_3(request.form)
    tiempoReal_form= forms.pagina_3(request.form)
    selecNotificacion_form= forms.pagina_3(request.form)
    timeStart_form= forms.pagina_3(request.form)
    timeEnd_form= forms.pagina_3(request.form)
    texto_forms= forms.pagina_3(request.form)
    orden_form=forms.orden_mantenimiento(request.form)
    
    if request.method== "POST":
            
            puestos_d_trabajo=puestos_d_trabajo_form.puestos_d_trabajo.data
            ficha=ficha_form.ficha.data
            tiempo_real=tiempoReal_form.tiempo_real.data
            selec_notificacion=selecNotificacion_form.selec_notificacion.data
            time_start=timeStart_form.time_start.data
            time_end=timeEnd_form.time_end.data
            texto=texto_forms.texto.data
            orden=orden_form.orden.data
            connect=sqlite3.connect(ordenes_MttoBD)
            cursor= connect.cursor()
            
            sentencia= (""" INSERT INTO notificacion (orden,tiempo_real,fecha_inicio, fecha_terminado, selec_notificacio, textArea, puesto_trabajo) VALUES (?,?,?,?,?,?,?)""" )
            cursor.execute(sentencia, ( orden, tiempo_real, time_start, time_end, selec_notificacion, texto, puestos_d_trabajo ))
            connect.commit()
            connect.close()

            return redirect(url_for('pagina_3'))
    return render_template("pagina_3.html", form=datos_form)



        

    
if __name__ == "__main__":
    
	app.run(debug=True, port=5000, host="0.0.0.0")
        
        