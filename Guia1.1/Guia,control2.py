#Guia 

#true y false 

#ejercicio 1 
"""enero=int(input(""))
febrero=int(input("")) 
marzo=int(input(""))  
#vamos a multiplicar el producto
costo_total=enero*1.25+febrero*1.38+marzo*1.14 
print(f"El costo total es de {costo_total} dolares")"""

#ejercicio 2 

#lista de los dias laborales

"""dias_laborales=["Lunes" , "Martes", "Miercoles" , "Jueves", "Viernes"] 
lunes=(input())
dias_laborales[0]=lunes 
print(f"El dia lunes se vendieron {lunes} productos")
martes=(input()) 
dias_laborales[1]=martes
print(f"El dia martes se vendieron {martes} productos")
miercoles=(input()) 
dias_laborales[2]=miercoles 
print(f"El dia miercoles se vendieron {miercoles} productos")
jueves=(input()) 
dias_laborales[3]=jueves
print(f"El dia jueves se vendieron {jueves} productos")
viernes=(input()) 
dias_laborales[4]=viernes
print(f"El dia lunes se vendieron {viernes} productos")

print(dias_laborales) #tienes que poner este para que imprima los dias_laborales 

cantidad_total= lunes+martes+miercoles+jueves+viernes 
print(cantidad_total)"""
 
 #Ejercicio 3  
 #manera correcta 
"""frutas=["1", "2", "3", "4","5", "6"] 
ninio1=int(input("Que numero sos:"))
Fruta=input("Mi fruta favorita es:") 
frutas[ninio1-1]=Fruta
print(frutas)

ninio2=int(input("Que numero sos:")) 
Fruta=input("Mi fruta favorita es:") 
frutas[ninio2-1]=Fruta
print(frutas)

ninio3=int(input("Que numero sos:")) 
Fruta=input("Mi fruta favorita es:") 
frutas[ninio3-1]=Fruta 
print(frutas)

ninio4=int(input("Que numero sos:")) 
Fruta=input("Mi fruta favorita es:") 
frutas[ninio4-1]=Fruta
print(frutas)

ninio5=int(input("Que numero sos:")) 
Fruta=input("Mi fruta favorita es:") 
frutas[ninio5-1]=Fruta
print(frutas)

ninio6=int(input("Que numero sos:")) 
Fruta=input("Mi fruta favorita es:") 
frutas[ninio6-1]=Fruta
print(frutas)"""

#mi codigo 
"""ninio2=input("Mi fruta favorita es:")
frutas[2]=ninio2
print(frutas) 
ninio3=input("Mi fruta favorita es:")
frutas[3]=ninio3
print(frutas) 
ninio4=input("Mi fruta favorita es:")
frutas[4]=ninio4
print(frutas) 
ninio5=input("Mi fruta favorita es:")
frutas[5]=ninio5
print(frutas) 
ninio6=input("Mi fruta favorita es:")
frutas[1]=ninio6
print(frutas)"""

#ejercicio 4

"""alumnos=("Fer" , "Regi", "Sofi", "Keit", "Carlos", "Eli", "Sara" ) 
orden=int(input("Dime, en que numero ingresaste (1-6):")) 
print(f"El alumno que entro en el orden {orden} se llama {alumnos[orden-1]}")

orden1=int(input("Dime, en que numero ingresaste (1-6):")) 
print(f"El alumno que entro en el orden {orden1} se llama {alumnos[orden1-1]}")"""

#ejericio 5 

"""nombre=input("Ingresa tu nombre:") 
apellido=input("Ingresa tu apellido:") 
print(f"{nombre.lower()}.{apellido.lower()}@ISND.com") #todos los metodos se escriben con parentesis 
print(f"{nombre.lower()[0]}.{apellido.lower()}@ISND.com")"""

#ejercicio 6 

"""salario=input("Ingrese su salario:")
print(salario[0]=="$") #[0] primera posicion, == para decir igual a "$" 
print(salario.count("$")==1) #en este se le pone salario.count para contar cuantas $ tengo igual a 1 porque solo debe de haber uno""" 

#ejercicio 7 

"""contrasena="dfgupccbjkaj"
print(contrasena[::3])"""


#AYUDANTIA EJERCICIO 

"""dias=["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES"]
lunes=int(input()) 
martes=int(input()) 
miercoles=int(input()) 
jueves=int(input()) 
viernes=int(input()) 
print(f"El dia {dias[0]} se vendieron {lunes} productos")
print(f"El dia {dias[1]} se vendieron {martes} productos")
print(f"El dia {dias[2]} se vendieron {miercoles} productos")
print(f"El dia {dias[3]} se vendieron {jueves} productos")
print(f"El dia {dias[4]} se vendieron {viernes} productos")"""

#Prueba 

"""dia1=int(input()) 
dia2=int(input()) 
dia3=int(input()) 

cantidad_total=dia1*0.45+dia2*0.50+dia3*0.48 
print(cantidad_total) 

entrada1=int(input()) 
entrada2=int(input())
entrada3=int(input())

total=entrada1*25+entrada2*30+entrada3*28.50
print(total)""" 

"""semana_mes=["Semana1", "Semana2", "Semana3", "Semana4"] 
semana1=int(input()) 
print(f"En {semana_mes[0]} se produjeron {semana1} artículos") 
semana2=int(input())
print(f"En {semana_mes[1]} se produjeron {semana2} artículos") 
semana3=int(input()) 
print(f"En {semana_mes[2]} se produjeron {semana3} artículos") 
semana4=int(input()) 
print(f"En {semana_mes[3]} se produjeron {semana4} artículos")"""

"""semestre=["Matematica", "Lenguaje", "Ciencias", "Historia", "Ingles"] 
nota_mate=float(input()) 
print(f"En {semestre[0]} obtuviste una nota de {nota_mate}") 
nota_len=float(input()) 
print(f"En {semestre[1]} obtuviste una nota de {nota_len}") 
nota_ciencias=float(input()) 
print(f"En {semestre[2]} obtuviste una nota de {nota_ciencias}") 
nota_historia=float(input()) 
print(f"En {semestre[3]} obtuviste una nota de {nota_historia}") 
nota_ingles=float(input()) 
print(f"En {semestre[4]} obtuviste una nota de {nota_ingles}")"""  

lista_mascotas =["1", "2", "3"] 

ninio1 = int(input())
mascota1 = input()
lista_mascotas[ninio1-1] = mascota1

ninio2 = int(input())
mascota2 = input()
lista_mascotas[ninio2-1] = mascota2


ninio3 = int(input())
mascota3 = input()
lista_mascotas[ninio3-1] = mascota3


print(lista_mascotas)




 


 
