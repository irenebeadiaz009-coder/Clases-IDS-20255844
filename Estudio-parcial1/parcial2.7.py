#La cena de Alvin 

Plato_principal=["Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog"]
Complementos=("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña") 

Eleccion1=int(input())
Plato=Plato_principal[Eleccion1-1]
Eleccion2=int(input())
Complemento=Complementos[Eleccion2-1] 
print(f"El pedido de Alvin es: {Plato} con {Complemento}") 

cambio_menu=int(input()) 
nuevo=(input())
Plato_principal[cambio_menu-1]=nuevo 
print(Plato_principal) 
