#Excepciones

#Con las excepciones lo que hace es que no tengamos que tener cuidado con cosas que sabemos que no funcionan realmente

ejec=True
while ejec:
    try: #excepcion 
        monto= int(input("Monto a calcular: ")) #error de logica [texto], le agrego el int, error(excepcion) se genera aqui
    except:
        print("Este tipo de valores no es valido")   #es como un if else 
    else:   
        impuesto = monto + 25 #texto mas numero, no se puede 
        print(f"El valor del impuesto es de ${impuesto:,.2f}")
        ejec=False #en vez de poner todo esto del ejec simplemente podemos poner "break" 
    finally:
        print("Hemos terminado la ejecucion de esta pregunta")
        
#try-except 
#funciona similar al if (try, except)
#trye es el bloque siendo evaluado
#except la exepcion
#else se debe de pasar a esa linea si try no es excepcion
#fianlly siempre va a correr, cerrar archivo 

#otra forma

while True:
    try:
        monto1=int(input("Ingrese el monto a calcular: "))
    except TypeError as te:
        print("Se genera un error: ", te)
    except ValueError as ve:
        print("Es un error de valor.")
    else:
        impuesto1=monto1+ 25 
        print(f"El impuesto es de ${monto1:,.2f}")
        break
    finally:
        print("Hemos terminado la ejecucion")