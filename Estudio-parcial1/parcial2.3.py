#Reporte de Alvin 

Dato1=float(input()) 
Dato2=float(input()) 
Dato3=float(input()) 
Dato4=float(input()) 
Dato5=float(input()) 
Dato6=float(input())

datos=[Dato1, Dato2, Dato3, Dato4, Dato5, Dato6] 
print(f"Maximo: {max(datos):.2f}") 
print(f"Minimo: {min(datos):.2f}") 
print(f"Diferencia: {((max(datos))-(min(datos))):.2f}") #{matematica} string 
print(f"Suma: {sum(datos):.2f}") 
print(f"Promedio: {(sum(datos)/len(datos)):.2f}") # en vez del len puedo poner el 6 
