#Problema 6: bodoque el enamorado 

x=int(input())

for i in range(x):
     nombres=input() 
     if len(nombres)<=6: #se pone esto para el largo 
         print("No vale la pena") 
     elif len(nombres) >6 and len(nombres)<8 :
         print("Dios no creo aguantar esta vez") 
     else:  
         print("Si aguanto otro desarrollo de personaje")
        