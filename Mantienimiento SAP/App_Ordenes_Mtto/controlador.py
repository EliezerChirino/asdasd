import sqlite3 

def tabla1():
    connect=sqlite3.connect("ordenes_Mtto.db")
    try:
        cursor= connect.cursor()
        cursor.execute(""" CREATE TABLE usuarios (
            Id integer PRIMARY KEY,
            username VARCHAR(20),
            password VARCHAR(10),
            nombre VARCHAR(10),
            apellido VARCHAR(10),
            nivel integer, 
            ficha integer
            )""")
        print("se creo la tabla usuarios")                        
    except sqlite3.OperationalError:
        print("La tabla articulos 'usuarios' ya existe")      
        connect.commit()
        connect.close()
    connect.close()

def tabla2():
    connect=sqlite3.connect('ordenes_Mtto.db')
    try:
        cursor= connect.cursor()
        cursor.execute(""" CREATE TABLE ordenes (
            orden integer PRIMARY KEY,
            lista_operacion integer,
            status VARCHAR(15),
            decripcion_orden text
            
            )""")
        connect.commit()
        print("se creo la tabla articulos de ordenes")                        
    except sqlite3.OperationalError:
        print("La tabla articulos 'ordenes' ya existe")      
        connect.commit()
        connect.close()
    connect.close()
        

def tabla3():
    connect=sqlite3.connect('ordenes_Mtto.db')
    try:
        cursor= connect.cursor()
        cursor.execute(""" CREATE TABLE notificacion (
            orden integer FOREIGNKEY,
            tiempo_real integer, 
            fecha_inicio text,
            fecha_terminado VARCHAR(10),
            selec_notificacio text, 
            textArea text,
            puesto_trabajo text
            )""")
        connect.commit()
        print("se creo la tabla articulos de notificacion")                        
    except sqlite3.OperationalError:
        print("La tabla articulos 'notificacion' ya existe")      
        connect.commit()
        connect.close()
    connect.close()
    
        
tabla1()
tabla2()
tabla3()

