#Correo

"""correo=input()"""

#print(correo.count("@")==1)
#print(correo.count(".")>=1)

"""condicion1=correo.count("@")==1 
#print(condicion1)
posicion_arroba=correo.index("@") #me ayuda para ver las demas condiciones
condicion2_1=correo.index("@")>=3   #index me dice en que posicion se encuentra lo que estoy buscando 
#print(condicion2_1)
condicion2_2=(len(correo)-posicion_arroba)>3 #se le pone solo > porque esta contando desde el arroba 
#print(condicion2_2)
condicion3=correo.count(".")>=1 #se le puede poner el igual o no  
#print(condicion3)
condicion4=correo.count(" ")==0 #con el espacio pq estoy contando si tiene espacios
#print(condicion4)
condicion5_1=correo[0] != "." #!= : no sea igual a 
condicion5_2=correo[-1]!= "." #-1 para cuando quiero el final 
#print(condicion5_1) 
#print(condicion5_2) 

print(condicion1 and condicion2_1 and condicion2_2 and condicion3 and condicion4 and condicion5_1 and condicion5_2)""" 

#find se utiliza como index (bsuca donde esta la variable) 


#and que sucedan muchas cosas a la vez 
#busco evaluar true/false 


#dragon dormido

"""cadena=input() #le pido una palabra que tenga z 
#variable1=cadena.count("z")
#print(variable1)  

#variable2=(cadena.count("Z")) 
#print(variable1+variable2) 

print(cadena.lower().count("z"))""" 

#Password de OOF

"""X=int(input()) #3
A=input() #Lapiz
B=input() #Mochila

print(A[:X:]) #del inicio, para que de la palabra al revez le ponemos (0 al 3 tomo LAPI) y luego debo de darle vuelta con (::-1) 
print(B[-X:]) # porque menos, es la manera normal de hacer referencias a los indices de menos X al final
 
print(A[:X:]+B[-X:])"""


#Diferencia de productos 

"""A=int(input())
B=int(input())
C=int(input())
D=int(input())

print(A*B-C*D)"""


