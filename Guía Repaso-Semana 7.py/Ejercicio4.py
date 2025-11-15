#Problema 4: Escoger Números 7 y 5  

x=int(input()) 
contador5= 0
contador7=0 

for i in range(x): 
    numeros=int(input()) 
    if numeros==5: 
        contador5=contador5+1
    elif numeros==7:
        contador7=contador7+1  
        
print(contador7)
print(contador5) 
    