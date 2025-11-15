#Identificadores C3 

Nombre_competidor=input() 
Apellido_competidor=input() 
Nick=Nombre_competidor[:5].lower()+Apellido_competidor[0].lower()
Pin=str((len(Nombre_competidor)* 1000 + len(Apellido_competidor))%10000)
I_d="C3-" + Nick + "-" + Pin

print(f"Nick: {Nick}")
print(f"Pin: {Pin}") 
print(f"ID: {I_d}") 

"""Proceso1=Nombre_competidor[:5].lower() 
Proceso2=Apellido_competidor[0].lower()
print(f"Nick: {Proceso1+Proceso2}") 

Proceso3=(len(Nombre_competidor)* 1000 + len(Apellido_competidor))%10000
print(f"Pin: {Proceso3}") 

Proceso4=(f"C3-{Proceso1+Proceso2}-{Proceso3}")
print(Proceso4)"""


"""print(f"Nick: {Nombre_competidor[:5].lower()+Apellido_competidor[0].lower()}")
print(f"Pin: {len(Nombre_competidor)* 1000 +len(Apellido_competidor)}")
print(f"C3-{Nombre_competidor[:5].lower()+Apellido_competidor[0].lower()}-{len(Nombre_competidor)* 1000 +len(Apellido_competidor)% 10000}")"""
