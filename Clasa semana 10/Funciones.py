#Este modulo contendra funciones

def ordenar_pizza(size,masa,*ingredientes): 
    """Vamos a imprimir su orden"""
    print(f"Usted a ordenado una pizza {size} de masa {masa} de: ")
    for i in ingredientes:
        print(f"\t- {i}")
        
def registro_profesores(nombre, apellido,**materias):
    """Crear un registro de profesor, utilizando kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias}")
        
def saludar_usuarios(nombres):
    """Saludara al usuario"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")
        
saludar_usuarios(["Anna", "Carla", "Josue"])