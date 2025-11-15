#while: meintras que

#codigo a ejecutar mientras que la condicion sea verdadera
#se puede repetir infinitas veces 

#inicio=0 
#maximo=5

#while inicio< maximo: 
    #print("Saludo") 
    #inicio= inicio+1
    
presupuesto=1000
gasto=0

while gasto <= presupuesto:
    compra=float(input("Digite el valor de compra: ")) 
    """gasto=gasto+compra""" 
    gasto+= compra #es lo mismo de arriba lo mismo para la resta -=
gasto-=compra #con eso se va del bucle para  no hacer ese gasto
print(gasto) 

