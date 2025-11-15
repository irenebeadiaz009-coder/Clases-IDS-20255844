#Pregunta 4: Palindromo 

#Lee una palabra y muestra True si se lee igual al derecho y al revés.
#Independientemente de mayúsculas o minúsculas.

palabra=input() 
print(palabra[::-1]) #aqui si da la palabra radar 

revision=palabra==palabra[::-1]
print(revision) 

print(palabra=={palabra[0]}) 