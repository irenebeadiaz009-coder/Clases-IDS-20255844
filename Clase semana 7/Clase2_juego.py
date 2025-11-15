#Vamos a jugar un juego 

aprobacion= True

while aprobacion:
    eleccion=input("Quieres jugar un juego? Y/N ") 
    if eleccion.lower() == "n": #podemos poner upper o lower 
        aprobacion= False #se detiene 
    elif eleccion.lower()=="y": 
        print("Me alegra que quieras seguir jugando!") #continua hasta decir N 
    else:
        print("La opcion elegida no es valida") #continua hasta que la respuesta sea Y o N 
        


