#Control 3, app para una cafeteria para gestionar platos y pedidos 
#Irene Beatriz Diaz Aguilar 20255844

#1. Confifuracion inicial 

agente="encargado" 
platillo=[]
precios=[] #estas son mis variables globales, donde guardare valores 


#2. Ingreso a la aplicacion 

usuario=input("Ingrese el nombre del agente: ") 
while usuario.lower() != agente.lower(): #para que no importe si es mayusucla o no
    print("Agente no registrado")
    usuario=input("Favor ingrese el nombre del agente: ") 

#3. Gestion del menu principal 

menu=True #variable 

while menu:
    opcion=int(input("1.Creación de platillos, 2.Consulta de platillos y precios, 3.Colocar un pedido, 4. Salir: "))

#7. Salir 

    if opcion==4:
        menu=False
       
#4. Creacion de platillos 
  
    elif opcion==1:
        platillo.append(input("Ingrese el nombre del platillo a crear: "))
        precios.append(float(input("Ingrese el precio del platillo a crear: ")))

    #5. Consulta de platillos 

    elif opcion==2:
        if len(platillo)==0:
            print("Actualmente no hay platillos ingresados") 
        else: 
            for p in range(len(platillo)): #le puse "p" por platillos 
                print(f"{platillo[p]}:${precios[p]}")

    #6. Colocar un pedido

    elif opcion==3:
        eleccion=input("Indique el nombre del platillo para su orden: ") 
        if len(platillo)==0:
            print("No hay platillos registrados")
        encontrado=False 
        for p in range(len(platillo)): 
            if eleccion[p].lower()==platillo[p].lower():
                print(f"Usted ha elegido {platillo[p]} con un precio de ${precios[p]}")
                encontrado=True 
                
        if encontrado==False:
            print("El platillo no se encontro, por favor regresar al menu")

print("Gracias por usar nuestra applicacion, ten un lindo dia")

#Espero esten bien, Alvin y ayudantes :)




        

       
        
