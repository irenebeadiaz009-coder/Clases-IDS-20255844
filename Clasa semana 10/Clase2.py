#Clase 2 

#Otro modulo para comprender las funciones 

def describir_mascota(nombre_mascota: str, tipo_animal:str="perro"): #parametra, aclara que sera de tipo string
   #si el ususario no pone que tipo de animal es asumira que es perro
    """Esta funcion describe una mascota"""
    print(f"Mi mascota se llama {nombre_mascota.capitalize()}")
    print(f"y es un tipo de animal: {tipo_animal.lower()}")
    
#Llamamos la funcion 
#describir_mascota(nombre_mascota="phoenix", tipo_animal="perro") 
#describir_mascota("Dolly", "gato")

def registro_usuario(nombre, apellido, inicial="", edad=0): #si no tengo incial asumira que no hay nada 
   #Los parametros que tienen un valor por defecto, como edad e inicial iran hasta el final
   #nombre y apellido son obligatorios y inicial y edad son opcionales  
    """Construir un nombre a partir de sus componentes"""
    if edad:
        texto_completo=f"La persona {nombre} {inicial} {apellido}, de {edad} años de edad."
    else:
        texto_completo=f"La persona {nombre} {inicial} {apellido}."
    return texto_completo

#print(registro_usuario("Daniel", "Winsecarver"))
#print(registro_usuario("Irene", "Diaz"))

#Definamos una funcion que es usada como una lista 

def saludar_usuarios(nombres):
    """Saludara al usuario"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")
    
usuarios=["Anna", "Luis", "JUAN"]
saludar_usuarios(usuarios)
    


