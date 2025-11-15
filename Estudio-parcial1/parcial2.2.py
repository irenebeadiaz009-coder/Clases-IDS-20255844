#Password de OOF

X=int(input()) #3
A=input() #Lapiz
B=input() #Mochila

xa=int(len(A)//X) #longitud, //division, entero 
xb=int(len(B)//X) #// significa division y que el resultado sea entero

"""print(A[:X:]) #del inicio, para que de la palabra al revez le ponemos (0 al 3 tomo LAPI) y luego debo de darle vuelta con (::-1) 
print(B[-X:])"""# porque menos, es la manera normal de hacer referencias a los indices de menos X al final
 
print(A[:xa:]+B[-xb:]) #dice del divisor por ello se debe de dividir la A con X 
#0:xa :final,  posicion 