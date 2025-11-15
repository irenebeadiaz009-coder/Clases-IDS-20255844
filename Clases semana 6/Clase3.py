#if 

nota= int(input("Ingrese la nota: "))

if nota== 10: 
    print("E")  #excelente
else: 
    if nota>7:
        print("MB") #muy bueno 
    else: 
        if nota> 5:  
            print("B") #bueno 
        else: 
            if nota > 3:
                print("R") #regular
            else: 
                print("M") #malo 

"""ventas= int(input("Ingrese el monto: "))
tipo= input("Ingrese el tipo de venta: ") """

"""if ventas > 500 and tipo=="local": 
    print("10%")
else: 
    print("14%") 
    if ventas> 200 and tipo=="local": 
        print("8%") 
    else: 
        print("12%")""" 

monto=int((input("Digite el monto: "))) 
tipo= input("Ingrese el tipo (Local/Exportacion): ") 
impuesto=0 

if tipo.lower()== "local": 
    if monto > 500: 
        impuesto=0.1 
    else:
        if monto > 200: 
            impuesto=0.08
        else: 
            if monto> 50:
                impuesto=0.06
            else: 
                impuesto=0 

elif tipo.lower()== "exportacion": 
    if monto > 500: 
        impuesto==0.14 
    else:
        if monto > 200: 
            impuesto=0.12
        else: 
            if monto> 50:
                impuesto=0.10
            else: 
                impuesto=0 
else: 
    print("No es valido") 
print(f"El impuesto a pagar de tipo {tipo} por venta de {monto:,.2f}") 
print(f"es de {monto*impuesto:,.2f}") 
    
#DRY: DON'T REPEAT YOURSELF

#elif nota > 7:     #es una combinacion de else y de if, evalua algo mas a la vez.

#otra manera 
"""if tipo.lower()== "local": 
    if monto > 500: 
        impuesto==0.1 
    elif monto > 200: 
        impuesto=0.08
    elif monto> 50:
        impuesto=0.06
    else: 
        impuesto=0 
elif tipo.lower()== "exportacion": 
    if monto > 500: 
        impuesto==0.14 
    else:
        if monto > 200: 
            impuesto=0.12
        else: 
            if monto> 50:
                impuesto=0.10
            else: 
                impuesto=0"""
                
                