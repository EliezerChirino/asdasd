import sqlite3 

def tabla1():
    connect=sqlite3.connect("base_de_datos_ordenes.db")
    try:
        cursor= connect.cursor()
        cursor.execute(""" CREATE TABLE usuarios (
            Id integer PRIMARY KEY,
            usuario VARCHAR(20),
            contraseña VARCHAR(10),
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

def tabla2():
    connect=sqlite3.connect('base_de_datos_ordenes.db')
    try:
        cursor= connect.cursor()
        cursor.execute(""" CREATE TABLE ordenes (
            operaciones VARCHAR(10),
            puesto VARCHAR(10),
            texto text,
            seleccion_notificacion INTEGER,
            orden_a text
            )""")
        connect.commit()
        print("se creo la tabla articulos de ordenes")                        
    except sqlite3.OperationalError:
        print("La tabla articulos 'ordenes' ya existe")      
        connect.commit()
        connect.close()
        
def tabla3():
    connect=sqlite3.connect('base_de_datos_ordenes.db')
    try:
        cursor= connect.cursor()
        cursor.execute(""" CREATE TABLE notificacion (
            transaccion VARCHAR(10),
            ficha VARCHAR(10) UNIQUE,
            texto text,
            tiempo_real VARCHAR (10),
            tiempo_inicio VARCHAR(10),
            tiempo_final VARCHAR(10) 
            )""")
        print("se creo la tabla articulos de notificacion")                        
    except sqlite3.OperationalError:
        print("La tabla articulos 'notificacion' ya existe")      
        connect.commit()
        connect.close()
        
    
        
tabla1()
tabla2()
tabla3()
    