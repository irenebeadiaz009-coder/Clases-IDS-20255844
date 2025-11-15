#Martes

#FOR se utiliza para iterar sobre una secuencia (lista,tupla,diccionario,cadena) 

#iterable: objeto capaz de devolver sus componentes uno a la vez
#iterador: objeto que representa un flujo de datos 

#numeros=[1,2,3,4] 
#print(len(numeros))
"""for x in numeros: 
    print("Hola") #una iteracion de base for toma una Q finita y me indica un limite donde terminara"""  

palabra="Aulas" #coleccion 
print(len(palabra)) 

for i in palabra: 
    print("Hello") 

dias=["Lunes", "Martes", "Miercoles", "Jueves",
      "Viernes", "Sabado", "Domingo"]

for d in dias: 
    print(d[:2]) #hago un recorrido por los valores de la coleccion.Dias es una coleccion de colecciones
# d[:2] es para que solo tome las dos primeras letras en toda la coleccion 

#para usar el bucle FOR debo de tener una coleccion

#RANGE (inicio,final)

"""print(range(10)) 
for i in range(10): #podemos usar slice for i in range(0,10,2)
    print(i)"""
    
for i in range(0,10,2,):
    print(i) 
    
personas=["Ana","Luis", "Luisa"] 
for p in personas: 
    for l in p:
        print(l) #entra a cada coleccion 
        
#ejercicio 

valores=[[1,3,6], [2,7,4],[6,5,9], [1,10,20]]
mayores=[] 
minimo=int(input("Ingrese el minimo: "))
for v in valores: 
    for valorcito in v: 
        if valorcito>minimo:
            mayores.append(valorcito) #.append agrega a la lista, al final, en la variable global

print(mayores) 

    
    