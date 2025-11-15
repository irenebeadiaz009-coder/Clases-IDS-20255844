#Funciones 

print("Hola, mundo")

#Este modulo va a contener funciones 
#UNa funcion tiene 2 tiempos, una definicion y una llamada 
#Vamos a definir una funcion, esto se logra con "def"

def mi_funcion(): #parametro  
    """Esta funcion imprime un saludo""" #se pone que hace la funcion 
    print("Hola, mundo") 
    print("Amigo usuario")
    print("Gracias por usar nuestro sistema!")
    
#Vamos a llemar a la funcion 
"""mi_funcion() #argumentos 
mi_funcion()
mi_funcion()"""

#Vamos a recibir informacion desde afuera de la funcion 
def capturar_nombre():
    """Esta funcion recibe valores por medio de input"""
    nombre_input=input("Escriba su nombre: ") #guardo el valor en un input
    apellido_input=input("Digite su apellido: ")
    """nombre_completo= nombre_input + " " + apellido_input"""
    nombre_completo=f"{nombre_input.capitalize()} {apellido_input.capitalize()}"
    print(nombre_completo)
    
def capturar_usuario(nombre, edad): #definir parametros () para poner argumentos 
    """Esta funcion recibe valores por medio de argumentos"""
    nombre_usuario= nombre
    edad_usuario= edad
    texto=f"El usuario {nombre_usuario.title()} tiene {edad_usuario} años de edad"
    print(texto)
    
#Llamando la funcion llamada capturar_usuario()
#capturar_usuario("Irene Diaz", 19) #argumentos

capturar_usuario(input("Ingrese su nombre: "), input("Ingrese su edad: ")) 

#Funcion que devuelve un valor 
def calculo_impuesto(ventas): #parametro
    """Esta funcion calcula el valor del impuesto"""
    if ventas < 500:
        tasa_impuesto=0.1
    else:
        tasa_impuesto=0.25
        
    return tasa_impuesto #nos devuelve el valor 

ventas=100
tasa_calculada=calculo_impuesto(ventas)
monto_impuesto=calculo_impuesto(ventas)*ventas 

print(f"""El valor de la venta fue de ${ventas:,.2f},
      la tasa de impuesto es {tasa_calculada:.2f}, 
      y el monto es de {monto_impuesto:,.2f}""")
#print(f"""El valor de la venta fue de ${ventas:,.2f},  
      #la tasa de impuesto es {calculo_impuesto(ventas)}, 
      #y el monto por tanto es ${calculo_impuesto(ventas)*ventas:,.2f}""") #:,.2f para que quede dos decimales 