#Herramientas de control de flujo 

#iterar=repetir la ejecucion de bloque de codigo mas de una vez 

#FOR se utiliza para iterar sobre una secuencia (lista,tupla,diccionario,cadena) 
# Ejecutar un bloque de codigo

#iterable: objeto capaz de devolver sus componentes uno a la vez
#iterador: objeto que representa un flujo de datos

nombres= ["Ana", "Sebas", "Mario", "Carla"] #son 5 colecciones 
#un iterable con cuatro iteradores, las cadenas son iterables
"Encontremos a Sebas"
nombres_buscar= input("Nombre a buscar: ") 
for n in nombres:
    #if n == "Sebas": puedo buscarlo
    if n == nombres_buscar:
        print("Ya lo encontre!!")  
    else: 
        print("Aqui no esta") 

"print(len(nombres))" 

numeros=[1, 2, 3] 
for numerito in numeros: #numerito: iterador (los valores de la lista), numeros:iterable (la lista en si)
    print(numerito) #es como entrar a cada cuertito y gritar el nombre del numerito que encuntre
    
#for= para cada 




