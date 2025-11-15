#Modulo de estudiantes 

#2. Registar estudiante

def registrar_estudiante(lista_estudiantes):
    """Registro al estudiante""" #le puse esto como en la clase :) 
    nombre_estudiante=input("Ingrese su nombre: ")
    carnet=f"S{len(lista_estudiantes)+1:03d}" #De esta forma, se crea el "codigo" de un solo
    estudiante={"Nombre": nombre_estudiante,
                "Carnet": carnet} 
    lista_estudiantes.append(estudiante)
    
#5. Mostrar estudiantes 

def mostrar_estudiantes(lista_estudiantes):
    print(lista_estudiantes)

#LLamar 
"""lista_estudiante=[]
registar_estudiante(lista_estudiante)
print(lista_estudiante)""" 