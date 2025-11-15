nombre="Alvin"
print(f"El profesor se llama {nombre}") 
print(nombre[3:5]) #ALVIN tiene 5 letras, pero nosotros contamos desde 0 

palabra="RECONOCER" 
print(palabra[::-1]) 
palabra2="RATON" 
print(palabra2[::-1])

palabra3="KEITLYNNE"
print(palabra3[::-1])

prueba= "carreton"
print(prueba==prueba[::-1]) 

prueba2="BOB" 
print(prueba2==prueba2[::-1]) 

numero=1234 
"""print(len(numero)) #los numeros no tienen largo""" 

print(len(prueba2))
edad=int(input("Ingrese su edad:")) #con int no tuviera largo, ya que los numeros no lo poseen. 
"""print(len(edad))"""

print(palabra.lower()) # el punto nos hace acceder a sus dependencias para que sea mayuscula o minuscula 
print(palabra2.upper()) 
print(palabra2.capitalize()) #los metodos son funciones aplicables para un objeto. Lleva parentesis, ya que los metodos son funciones adheridas a un objeto.

print(edad.upp) #no me sale la opcion de upper porque es un numero (int) no es un string (letras) 

