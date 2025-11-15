#f-strings y formato de salida 

nombre="Ana" 
producto="laptop" 
precio=1200.00
print(f"Hola,{nombre},el producto {producto} cuesta ${precio} ")

nombre_usuario="Carlos" 
pais="El Salvador"
print(f"Hola,{nombre_usuario} de {pais},¡bienvenido!")

#Mini_formulario

nombre=input("Ingrese su nombre completo:") 
edad= int(input("Ingrese su edad:")) 
ciudad= input("Ingrese la ciudad donde usted reside:") 
print(f"Revisemos sus datos, su nombre es {nombre} y tiene {edad} años y reside en la ciudad de {ciudad}") 

base=float(input("Ingrese la base del triangulo:")) 
altura=float(input("Ingrese la altura del triangulo:")) 
area=base*altura 
print(f"El area del triangulo es: {area:.2f}") #aqui ponemos {area:.2f) . para que ponga el decimal y el 2f porque solo necesito dos decimales}

producto="pan" 
precio=1.50 
cantidad=4
total=6.00 
print(f"El producto es {producto} y el precio de este es de {precio} por lo que al comprar {cantidad} unidades me costara un total de ${total}") 


