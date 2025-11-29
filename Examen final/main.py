#Main 

#Este modulo sera el inicio de mi sistema (menu)
#Importamos los modulos necesarios

import modulo_funciones as mf

while True: 
    #rompenos el bulce o con break o con un false
    print("""
    Bienvenido a nuestro sistema.
    1. Registrar estudiante 
    2. Inscribir en curso
    3. Generar reportes 
    4. Salir
        """)  
    opcion=input("Elija una opcion (1-4): ") 
    
    if opcion=="1":
        mf.registrar_estudiante() #reconocemos las funciones print("Esta es la opcion 1")
    elif opcion=="2": 
        mf.inscribir_curso()   
    elif opcion=="3":
        mf.generar_reporte()  
    elif opcion=="4":
        print("Gracias por visitarnos 💖🎉") 
        break
    else:
        print("La opcion que fue seleccionada no es valida")

