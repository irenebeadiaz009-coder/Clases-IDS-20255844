#Operadores matemáticos y lógicos

"""a=10 
b=3
c=5 
suma= a+b 
print("La suma entre a y b es" , suma) 
resultado= a/b 
print("La division entre a y b es" , resultado) 
residuo= a%c 
print("El residuo de dividir a entre c es" , residuo) 

numero= 7 
resultado= numero>5 
print(resultado) 

x=10 
y=10 
print(x is y)
print (y is not x ) #en esta no se pone type, sino que solo el is o el is not con las variables a comparar 

request= int(input("Ingrese un numero:")) 
result=(numero % 2==0)  #el % se usa para sacar el residuo y el == para ver si es igual a 0 
print(resultado) 

registrado=True 
print("Registrado and true:" , registrado and True)  
print("Registrado and false:" , registrado and False)
print("Registrado and true:" , registrado or True)
print("Registrado and false:" , registrado or False)
print("Not registrado:" , not  registrado)"""

numero_1= int(input("Ingrese un numero entero:"))
numero_2= int(input("Ingrese otro numero entero:")) 
print(numero_1>=numero_2) 

edad=int(input("Ingrese su edad:"))
puede_votar= edad>=18 

"""votar= edad>=18 
legal="En unos momentos le diremos si puede votar. Si sale true, es que si puede, pero si sale false es que no" """
 #vamos a probar algo 
 
if puede_votar:
    print("Puede votar!")
else: 
    print("No puede votar aun :(") 
    
edad=19 
estudiante=True 
print(edad>=18 and estudiante)

cantidad_fresas= 76 
vendedora= True 
print(cantidad_fresas>=90) 

