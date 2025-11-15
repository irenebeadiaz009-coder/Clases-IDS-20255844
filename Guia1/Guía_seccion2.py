#input() y conversión de tipos (casting) 

nombre= input("Ingresa tu nombre:") 
saludo= (f"Holaaaaa {nombre}")
print(saludo)

edad= int(input("Ingresa tu edad:")) 
print(f"El doble de tu edad es {edad *2} años")

numero1= int(input("Ingresa el primer numero entero:")) 
numero2= int(input("Ingresa el segundo numero entero:"))
suma= numero1+numero2 
print("La suma de los dos numeros enteros es:" , suma) 

decimal= float(input("Ingresa un numero decimal")) 
mitad= decimal/2 
print("La mitad del decimal es:" , mitad) 

año_nacimiento= int(input("Ingrese su año de nacimiento:")) 
calculo_edad= 2025- año_nacimiento 
print("Tu edad es de:" , calculo_edad) 

precio=float(input("Ingrese el precio de las manzanas:")) #el producto es manzanas (:)
manzanas= int(input("Ingrese la cantidad de manzanas:")) 
total= precio*manzanas 
print("El total a pagar es de:" , total) 

numero= int(input("Ingrese un numero entero:"))
cuadrado= numero**2
print("El cuadrado del numero es de:" , cuadrado) 

numero_1= int(input("Ingrese un numero entero:"))
numero_2= int(input("Ingrese otro numero entero:")) 
suma= numero_1+ numero_2 
promedio= suma/2 
print("El promedio de esos dos numeros enteros es de:" , promedio) 

nombre_completo= input("Ingrese su nombre completo:") 
edad_usuario= int(input("Ingrese su edad:")) 
print(f"Hola,{nombre_completo}.Tienes {edad_usuario} años") 



 