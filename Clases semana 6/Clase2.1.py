#listas

nombres=["Ana", "Antonio", "Paulina", "Jose"] 
print(len(nombres))

#string y las listas son mutables y las tuplas inmutables
#la lista se le puede quitar y agregar

nombres[2]="Pablo" #le cambio el dato 2 a otro
print(nombres)

#agregar
#metodo 1: .append (agrega al final)

nombres.append("Hazel") 
print(nombres) 
#Se le puede pedir al usuario que ingrese lo que se le agregara a la lista
nombres.append(input("Ingrese el nuevo nombre: "))
print(nombres) 

#metodo 2: .insert (en la posicion en la que me diga) 
nombres.insert(3, "Fiore")# aqui se ponen dos argumentos, datos, el numero de la posicion donde lo quiero y lo que le quiero poner
nombres.insert(int(input("Ingrese el indice: "))-1, "Sebas") #se le pone -1 para que me le este desde 0
print(nombres) 

#borrar 
#metodo 1: .remove (va a removare el VALOR) 
nombres.remove("Hazel") 
print(nombres) 

#metodo2: .pop (posicion que voy a borrar y cual fue el valor borrado) 
nombre_borrado=nombres.pop(int(input("Indice a borrar: "))-1) 
print(nombres) 
print(nombre_borrado) 

"""nombres[1].pop(3)""" #no aplica en coleccion de string (no es una cadena de caracteres) 


