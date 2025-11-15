#Vamos a proceder a atender pedidos de pizza 

#Definiendo la funcion
def ordenar_pizza(size,masa,*ingredientes): #parametro #ahorra con args, este parametro es tratado como una lista
    #en lugar de poner ingrediente1, etc. Se utiliza *ingredientes para decir que tendremos un conjunto de elementos
    """Vamos a imprimir su orden"""
    print(f"Usted a ordenado una pizza {size} de masa {masa} de: ")
    for i in ingredientes:
        print(f"\t- {i}") #\t reconoce una tabulacion, ingredientes es tratado como una lista

   
#Llamando la funcion 
ordenar_pizza("extra grande","delgada", "queso", "tocino", "jamon","chile")
ordenar_pizza("grande","delgada","queso","carne","peperoni") 

#El parametro de tipo args (actua como lista) se ponen hasta el final 