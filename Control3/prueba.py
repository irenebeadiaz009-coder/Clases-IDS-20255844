#control 3 

#1. Configuracion inicial
agente="encargado" 
platillo=[]
precios=[] 
ingreso=True

#2.	Ingreso a la aplicacion 
if ingreso==False: 
    nombre=input("Ingrese el nombre del agente: ") 
    while nombre!="encargado":
        print("Agente no registrado")
        print(input("Favor ingrese el nombre del agente: "))