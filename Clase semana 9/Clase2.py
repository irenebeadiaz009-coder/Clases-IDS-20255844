#Estructuras de datos 

posicion=0
usuarios=["Ana", "Carlos","Luis", "Maria", "Lorenzo"] #iterable es usuarios y el iterador los valores dentro de usuario 
edades=[20, 19, 21, 22, 18]
fruta=["uva", "piña", "jocote"] 

#una forma 
"""for usuario in usuarios: #en vez de usar usuario usare una pareja de valores 
     print(f"{posicion} {usuario}")
     posicion+= 1"""
   
    
#nueva forma 
for i, usuario in enumerate(usuarios, start=1):#el start me dice que comience a contar desde el 1 y no desde el 0 
    print(f"{i} {usuario}") 
    
#ahora juntando a las edades 

for posicion,usuario in zip(usuarios, edades): #zip es una funcion que junta mas de dos iterables
    print(f"{posicion} {usuario}") 