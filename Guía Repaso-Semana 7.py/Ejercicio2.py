#Problema 2: anterior y posterior 

numero=int(input()) 

if numero%2==0: #aqui veo lo del residuo 
    print(numero+2, numero-1 )  # si es par
else: 
    print(numero+1, numero-2) #si es impar 