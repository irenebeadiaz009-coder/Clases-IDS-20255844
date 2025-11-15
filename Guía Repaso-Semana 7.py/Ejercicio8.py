#Problema 8: Entrada al cine 

a=int(input()) 
entro=0 # variable global 

for edades in range(a): 
    edades=int(input()) 
    if edades>=15:
       entro=entro+1 
       
print(entro)
