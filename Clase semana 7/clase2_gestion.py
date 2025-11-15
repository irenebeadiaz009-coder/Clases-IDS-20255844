#sistema de gestion de alumnos 

#1. agregar 
#2. consultar
#3. modificar 
#4. borrar 
#5. salir

menu_iniciado= True 
alumnos=[]

while menu_iniciado: 
    opcion= int(input("1.Agregar, 2.Consultar, 3.Modificar, 4.Borrar, 5.Salir: "))
    if opcion == 5:
        menu_iniciado= False 
    elif opcion==1:
        alumnos.append(input("Digite el nombre del alumno: ")) 
    elif opcion== 2: 
        #print(alumnos) 
        for a in alumnos:
            print(a) 
    elif opcion==3: 
        indice= int(input("Digite el numero del alumno (1-3): ")) 
        nuevo=input("Digite el nombre nuevo: ") 
        alumnos[indice-1] = nuevo 
    elif opcion==4: 
        indice=int(input("Digite el numero del alumno (1-3) a popear: ")) #pop lo que borro
        alumno_borrar= alumnos.pop(indice-1)
        print(f"Hemos borrado a: {alumno_borrar}") 
    else: 
        print("Esa opcion no es valida.") 
        
    
print("Gracias por usar nuestro sistema.") 

#if si hay o no hay alumno. If len de esto

if len(alumnos)==0:
    print("No hay alumnos regustrados: ") 