#Martes 21 del 2025 

#TRABAJANDO CON LISTAS

#string             
#tupla   ()           indice 
#lista   []

lista=[1, 2, "tres"] 
print(len(lista)) 
print(lista) 

#para encontrar un valor dentro de una lista y dentro de un valor de la lista 
#hay una coneccion chiquita dentro de ella, esta es "tres"
print(lista[2][2]) 
#"tres" se comporta como un string? 
print(lista[2][2:].upper()) #si es un string 

lista2=[1, 2, "tres", ["enero", "febrero", "marzo"]]
#como obtengo a de marzo 

print(lista2[3][2][1]) #es una lista dentro de una lista la cual tiene sus valores y sus valores tiene sus valores

#Tambien se puede concatenar listas (unirlas) 

numeros=["uno", "dos", "tres"] #tengo 4 colecciones, la primera es "numeros" y las demas son las cadenas de texto que tambien son colecciones
print(numeros) 
numeros= numeros+["cuatro", "cinco", "seis"]
print(numeros) 

numeros[2]="trois" #french
print(numeros) 