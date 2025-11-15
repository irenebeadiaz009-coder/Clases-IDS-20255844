#Pregunta 5: Contiene letra 
 

#print(palabra.index(letra)==letra) #HUBIERAS PROBADO OTRO SIGNO

#print(palabra.count(letra)==letra) 

#condicion=(palabra.index(letra)) 
#print(palabra.index(letra)==condicion) 

palabra1=input()
letra1=input() 
revision=palabra1.count(letra1)
print(palabra1==letra1) 

#Revision 

revision1=letra1 in palabra1
print(revision1) #asi se hacia, Irene 
#o asi:
print(palabra1.count(letra1)>0) 

