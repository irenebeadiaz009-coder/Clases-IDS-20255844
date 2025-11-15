#Funciones
#Vamos a crear una funcion utilizando kwargs 

def registro_profesores(nombre, apellido,**materias):
    """Crear un registro de profesor, utilizando kwargs"""
    #**kwargs es para crear diccionarios 
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias}")
        
#LLamado 

registro_profesores(
    "Alvin",
    "Portillo",
    Ciclo1= ["BD1", "IIJ", "A&GD"],
    Ciclo2= ["DAI", "BD2", "SINE"],
    Ciclo3=["IDS", "FPEN", "PAD"]
)
    
    

