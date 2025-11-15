#Vamos a crear nuestro primer set (esto es un  docstring)

my_set= ["rojo", "verde", "negro", "azul", "rojo", "azul"]
print(type(my_set)) #type, tipo de dato 
print(len(my_set)) 
print(my_set) 

#Nuestro primer diccionario 
#los indices para los diccionarios son llamados "claves", y una clave asociada a un valor es denominada por "Clave-valor"
#se crea por llaves {}


mi_mascota={
        "tipo": "perro", #clave : valor 
        "nombre": "Phoenix",
        "edad":4, 
        "personalidad": "amigable"}

print(type(mi_mascota))
print(mi_mascota) #las claves pueden tener numeros, son etiquetas  

# {tipo, nombre, edad, personalidad} 

regys_mascota= {
    "edad": 4, 
    "nombre": "Phoenix" ,
    "personalidad":"amigable", 
    "tipo": "perro"}

print(mi_mascota==regys_mascota) #no le importa que los datos esten en posiciones diferentes 

#Otro ejemplo

birthdays={
    "Alice":"Abril 1", 
    "Bob":"Diciembre 2", 
    "Carol":"Marzo 4"
}

birthdays["Carol"]= "Septiembre 2" 
print(birthdays["Carol"]) #los diccionarios no se trabajn con indices pero con claves 
print(birthdays)
birthdays["Pau"]= "Julio 31" 
del birthdays["Bob"] #del is delete 
print(birthdays)

#for f in birthdays.values 
#print(f)

for person, date in birthdays.items():
    print(f"el cumpleaños de {person} es el dia {date}.")
    
#
    