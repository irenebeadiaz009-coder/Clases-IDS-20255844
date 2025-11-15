#Una aplicacion para guardar el nombre de los alumnos 

alumnos=[] #variable global 

"""alumno= input("Digite el nombre: ") 
alumnos.append(alumno) #agregue 
alumno= input("Digite el nombre: ") 
alumnos.append(alumno)  
alumno= input("Digite el nombre: ") 
alumnos.append(alumno) 

print(alumnos)"""

for a in range(int(input("Digite la cantidad de alumnos a registar: "))):  
    alumno=input("Digite el nombree: ") 
    alumnos.append(alumno) 

print(alumnos)  



