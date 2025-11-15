# Ejercicio Integrador: Cafetería ESEN Brew 



"""cliente={"Codigo": input("Ingrese su codigo: "),
         "Nombre": input("Ingrese su nombre: "),
         "Correo": input("Ingrese su correo: "),
         "Telefono": input("Ingrese su numero de telefono: ")}""" 


"""productos={"Codigo del producto": input("Ingrese el codigo del producto:"),
           "Nombre del producto": input("Ingrese el nombre del producto: "),
           "Categoria": input("Ingrese la categoria del prodcuto: "),
           "Precio": input("Ingrese el precio del producto: ")}"""

print("Bienvenido/a a la cafeteria ESEN Brew")
restaurante=True 
productos=[]
clientes=[]
opcion=0

while restaurante:
    opcion=(int(input("""1. Mostrar productos"
                "2. Agregar producto"
                "3. Registar nuevo cliente"
                "4. Mostrar clientes"
                "5. Registrar pedidos"
                "6. Mostrar pedidos del dia"
                "7. Mostrar categorías disponibles"
                "8. Salir: """))) 
    if opcion==8:
        restaurante=False   
        print("Gracias por usar nuestra app")
    elif opcion==3:
        cliente={"Codigo": input("Ingrese su codigo: "),
         "Nombre": input("Ingrese su nombre: "),
         "Correo": input("Ingrese su correo: "),
         "Telefono": input("Ingrese su numero de telefono: ")}
        
    elif opcion==2:
        productos={"Codigo del producto": input("Ingrese el codigo del producto:"),
           "Nombre del producto": input("Ingrese el nombre del producto: "),
           "Categoria": input("Ingrese la categoria del prodcuto: "),
           "Precio": input("Ingrese el precio del producto: ")}
    elif opcion==1:
        if len(productos)==0:
            print("No se encuntra ningun producto por el momento") 
        else:
            for p in range(len(productos)):
                print(f"{productos[p]}")
            
        

  
    
        
 
