#Problema 5: los combos de David

x=int(input()) 
Pa,Pb,Pc=map(int, input().split())
#Pa=int(input())
#Pb=int(input()) 
#Pc=int(input()) 

for ataques in range(x): 
    Ataque =input() 
    Damage=(Ataque.count("A")*Pa)+(Ataque.count("B")*Pb)+(Ataque.count("C")*Pc)
    print(Damage)
    
"""a=int(input())
a1=input() 
print(len(a1)*a) """









    
    

