#Listas!

"""numeros=["uno", "dos", "tres", "cuatro"] 
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3]) 

#Coleccion de caracteres 

nombre="Antonio" 
print(nombre.count("n")) 
print(nombre.count("o")) 
print(nombre.lower().count("a")) #cuente la "a" como minuscula
#no se puede poner nombre.count["a"].lower() porque estaria diciendo haga lower el numero no la palabra, nombre


print(numeros.count("dos"))"""

#Otro

nombres=["Ana", "Antonio", "Ana", "Jose"]  #hay cinco colecciones 
print(len(nombres[0])) #aqui me esta dando la longitud de la coleccion "Ana" 

#Cuentas "Anna's" hay? 
"""print(nombres.count("Ana")) """
"""print(nombres[0].count("a")) """ #no aplican metodos como lower, la palabra si puede ser lower

"""print(nombres[0].lower().count("a")) 
#Aqui estamos poniendo que .lower, un metodo, afecta a la coneecion 0 dentro de nombres 
#la lista no tiene lower, sino el string

repeticiones_a= 0 #ayuda visual, lo uso como un contador
repeticiones_a=repeticiones_a + nombres[0].lower().count("a")  
repeticiones_a=repeticiones_a + nombres[1].lower().count("a")  
repeticiones_a=repeticiones_a + nombres[2].lower().count("a")  
repeticiones_a=repeticiones_a + nombres[3].lower().count("a")  
print(repeticiones_a) """






