#Modulo de libros 

#Ejercicio 1. Registar libros

def registrar_libro(lista_libros):
    """Vamos a registrar libros""" #:)
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    codigo = f"L{len(lista_libros)+1:03d}"
    disponible = True
    
    libro = {"Codigo": codigo,
        "Titulo": titulo,
        "Autor": autor,
        "Disponible": True}
    lista_libros.append(libro)

#Ejercicio 4: Mostrar libros

def mostrar_libros(lista_libros):
    print(lista_libros) 
    

"""#llamar 

lista_libros=[]
registar_libro(lista_libros)
print(lista_libros)"""