#guia 1, en esta guia solo sera un modulo el que se hara 

print("Bienvenido a Contratame")

DUI=[]
clientes=[]
contrataciones=[]

servicios={
    "WD": "Desarrollo Web",
    "DS": "Ciencia de Datos",
    "ML": "Machine Learning Aplicado", 
    "API": "Desarrollode API's Empresariales"
}

def menu():
    while True:
        opcion=input("""
                            1. Crear cliente
                            2. Contratar servicio
                            3. Listar clientes por servicios
                            4. Salir: """)
            
        if opcion=="1":
            crear_cliente()
        elif opcion=="2":
            contratar_servicio() 
        elif opcion=="3":
            cliente_servicio() 
        elif opcion=="4":
            print("Gracias por usar Contratame")
            break 
        else:
            print("La opcion no es existente")
                
def crear_cliente():
#Validacion del DUI
    while True: 
        Dui_in=input("Ingrese el numero del DUI: ")
        if len(Dui_in)!=10:
            print("El DUI debe de tener 10 caracteres")
            continue #pone esto siempre para que el usuario vuelva a poner las cosas
        if Dui_in[8]!= "-":
            print("El DUI debe inlcuir un guion (-)")
            continue 
        existe=False
        for dui in clientes:
            if dui["DUI"]==Dui_in:
                existe=True
        if existe:
            print("El numero del DUI ya existe, ingrese otra vez")
            continue 
        break 
    #Validar nombre
    while True:
        nombre=input("Ingrese su nombre: ").capitalize()
        if len(nombre)<1:
            print("Nombre tiene que tener mas que dos caracteres") 
            continue 
        else:
            break #seguimos, va al siguiente punto que es el apellido
    #Validar apellido
    while True:
        apellido=input("Ingrese su apellido: ").capitalize()
        if len(apellido)<1:
            print("Apellido debe de tener mas de dos caracteres")
            continue
        else:
            break 
    #Datos
    cliente= {
            "DUI": Dui_in, 
            "Nombre": nombre, 
            "Apellido": apellido
                }
    
    clientes.append(cliente)
    print("Cliente agregado")
    
#Contratar servicio 

def contratar_servicio():
    while True:
        #Solicitar DUI
        pedir_dui=input("Ingresa tu DUI: ").lower()
        if pedir_dui=="salir":
            break  
        #Verificar si existe el carnet
        existe=False 
        for iden in clientes:
            if iden["DUI"]==pedir_dui:
                existe=True 
                break 
        if existe:
            print(servicios)
            eleccion=input("Seleccione el codigo del servicio (ej. WB para Desarrollo Web): ").upper()
            #Verificar si servicio existe 
            if eleccion not in servicios:
                print("No existe ese servicio") 
                continue
            
            contrato=False 
            for con in contrataciones:
                if con[0]==pedir_dui and con[1]==eleccion:
                    contrato=True
                    break 
            if contrato:
                print("Ya contrato este servicio")
            else:
                contrataciones.append((
                    pedir_dui, eleccion
                ))
                print("La inscripcion fue un exito")
                print(contrataciones)
        else: 
            print("Debes registrar tu DUI")     
            
def cliente_servicio():
    while True: 
        if len(contrataciones)==0:
            print("No hay contrataciones")
            break 
        print("""
              Submenu:
              1. WD
              2. DS
              3. ML
              4. API
              5. No contratados
              6. Salir
              """) 
        opcion=input("Elige una opcion (1-6): ")
        
        if opcion=="1":
            eleccion_WD=[]
            
            for pedir_dui, eleccion in contrataciones:
                if eleccion=="WD":
                    eleccion_WD.append(pedir_dui)
                if len(eleccion_WD)==0:
                    print("No hay contrataciones")
                else:
                    print("Las contrataciones del Desarrollo Web:")
                    for dui in eleccion_WD:
                        print("-", dui) 
        if opcion=="2":
            eleccion_ds=[]
            
            for pedir_dui, eleccion in contrataciones:
                if eleccion=="DS":
                    eleccion_ds.append(pedir_dui)
                if len(eleccion_ds)==0:
                        print("No hay contrataciones")
                else:
                    print("Las contrataciones para Ciencia de Datos:")
                    for dui in eleccion_ds:
                        print("-", dui)
        if opcion=="3":
            eleccion_ml=[]
            
            for pedir_dui, eleccion in contrataciones:
                if eleccion=="ML":
                    eleccion_ml.append(pedir_dui)
                if len(eleccion_ml)==0:
                        print("No hay contrataciones")
                else:
                    print("Las contrataciones para Machine Learning Aplicado:")
                    for dui in eleccion_ml:
                        print("-", dui)
        
        if opcion=="4":
            eleccion_api=[]
            
            for pedir_dui, eleccion in contrataciones:
                if eleccion=="API":
                    eleccion_api.append(pedir_dui)
                if len(eleccion_api)==0:
                        print("No hay contrataciones")
                else:
                    print("Las contrataciones para Desarrollo de API's Empresariales:")
                    for dui in eleccion_api:
                        print("-", dui)
                        
        if opcion=="5":
            no_contrato=[] 
            for dui_in in clientes:
                if len(clientes)==0:
                    print("Todos han contratado")
                else:
                    print("No han contratado")
                    for pers in no_contrato:
                        print("-", pers)
                        
        if opcion=="6":
            print("Volviendo al menu principal")
            break 
                    
        
menu()


        
        