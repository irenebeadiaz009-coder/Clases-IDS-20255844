#Modulo de prestamos 

#3. Registar prestamo 

def registrar_prestamo(lista_libros,lista_estudiantes,lista_prestamo):
    #Pide el carnet del estudiante
    carnet_estudiante=input("Ingrese su carnet: ").capitalize() #por si el usuario lo pone en minuscula
    #Verificar que existe 
    estudiante_encontrado=None #no hay ningun estudiante, va revisandolo
    for estudiante in lista_estudiantes:
        if estudiante["Carnet"]==carnet_estudiante:
            estudiante_encontrado= estudiante
            break
    if estudiante_encontrado is None:
            print("No esta registrado")
            return #se sale 
    #Pide codigo del libro      
    codigo_libro=input("Ingrese el codigo del libro: ").capitalize()
    #Verifica que exista el codigo
    libro_encontrado=None
    for libro in lista_libros:
        if libro["Codigo"]==codigo_libro:
            libro_encontrado=libro
      
    if libro_encontrado is None:
            print("No existe")
    #Verifica si esta disponible       
    if not libro_encontrado:
        print("El libro no esta disponible")
        return
    #Pide la fecha        
    fecha=input("Ingrese la fecha (A/M/D): ") #año/mes/dia 
    
    prestamo={"Carnet": carnet_estudiante,
              "Codigo": codigo_libro,
              "Fecha": fecha} 
    
    lista_prestamo.append(prestamo) 
    libro_encontrado["Disponible"]=False 

#Ejercicio 6. Mostrar prestamos 

def mostrar_prestamos(lista_prestamo):
    print(lista_prestamo)