#Validacion de DUI

#Recibe un supuesto número de DUI, el cual debe validar que se cumplan las siguientes condiciones:
#El largo debe de ser exactamente de 10 caracteres
#El noveno carácter debe ser “-“
#Validar únicamente que el último carácter es número entero.

DUI=(input())

condicion1=len(DUI)==10 
#print(condicion1) 
condicion2=DUI[8]=="-" 
#print(condicion2) 
condicion3=DUI[9]!= str #(is not) para TIPOS; los signos son para VALORES 
#print(condicion3) 

print(f"{str(condicion1 and condicion2 and condicion3)}") #Respuesta de la pregunta 7 

#Alvin's way 

cond1= len(DUI)==18 
cond2=DUI[8]=="-" 
print(type(int(DUI[-1])) is int) 