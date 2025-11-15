#Correo

"""correo=input()
print(correo.count("@")==1) 
print(correo.index("@")>=3)
posicion_arroba=correo.index("@") #indice de la posicion 
print(len(correo)-posicion_arroba>3) 
print(correo.count(".")>=1)
print(correo.count(" ")==0)
print(correo[0]!=".") "." is not correo [0]
print(correo[-1]!=".")"""

correo=input()
posicion_arroba=correo.index("@") 
print(correo.count("@")==1 and correo.index("@")>=3 and len(correo)-posicion_arroba>3 and correo.count(".")>=1 and correo.count(" ")==0 and correo[0]!="." and correo[-1]!=".") 