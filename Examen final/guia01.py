"""semana={}

semana["uno"] = "lunes"
semana["dos"] = "martes"
semana["tres"] = "mierc"
semana["cuatro"] = "juev"
print(semana)

print(semana.keys())
print(semana.values())
print(semana.items())

for i in semana.items():
    print(i)  # solo para separar visualmente"""

#Cliente (diccionario)
# Numero de DUi: unique, 10 caracteres incluido el -
# Nombre: al menos dos caracteres, es decir 2 o mas
# Apellido: al menos dos caracteres, es decir 2 o mas

# Lista Servicios dispo (diccionario)
#Tupla por que sus valores no son modificables (Es una lista de valores constantes)

#Lista de contrataciones (diccionario)
# un diccionario que almacenara (DUI, Cod. Servicio)


#Menú principal del sistema
#El sistema debe tener el siguiente menú:
#•	Crear cliente
#•	Contratar servicio
#•	Listar clientes por servicio
#•	Salir

#Dui, nombre, apellido
clientes = {}
#Dui, Codigo del Servicios
listContrataciones = {}
ServiciosDispo ={"WD": "Desarrollo Web",
                "DS":"Ciencia de Datos",
                "ML": "Machine Learning Aplicado",
                "API":"Desarrollo de API's Empresariales"}
print("Bienvenido al sistema.")

#Validaciones:

def cantDui (dui):
    return len(dui) == 10 #Retonan TRUE si se cumple

def duiUnique(dui):
    return dui not in clientes # usamos not in para que retorne TRUE si no existe el cliente, si el cliente si esta, retorna FALSE

def cantDatos (nombre, apellido):
    return len(nombre) > 2 and len(apellido) > 2 #Retona true si ambas son mayores que dos
#Validaciones para contratar servicio
def clientExist(dui):
    return dui in clientes #Retornara verdadero si el cliente esta registrado(existe)
def clientinService(dui):
    return dui in listContrataciones #Retornara TRUE si ya contrato, FALSE si no a contratado

def crearCliente(varDui, varNombre, varApellido):
    clientes[varDui] = { #El DUI HACE DE CLAVE DEL DICCIONARIO
                "nombre": varNombre, 
                "apellido": varApellido
            }
    print("Cliente agregado con exito")



# SERVICIOS
# Me dicen que debo crear una funcion que ingrese la contratacion de un serivicio
#Esta funcion debe recibir el dui del cliente que va a contratar el servicio y que servicio va a contratar
# Sin embargo me dice que debo tener algunas cosas en cuenta
# 1ro debo con la misma variable, aceptar dos valores, el dui o el mensaje de "Salir" y que este mensaje lo regrese al menu principal, es decir al while inicial
# Ademas, si ingresa el dui. Tengo que validar que exista en el diccionario de clientes, puedo buscar la clave/dui con diccionario.keys().values().items()). Porque la llave de cada cliente es el DUI.
# ADEMASSSS, Debo validar que el cliente no este en el diccionari de contrataciones, porque si el DUI existe ahi, quiere decir que ya contrato un servicio. Logica similar al punto anterior. Y como extra aqui debo mandarlo de regreso al while inicial, quiza aqui pueda hacer un while chiquito y para cerralo uso break y eso lo mandaria de regreso al main principal.

#Bueno, los valores de entrada serian: El dui y el codigo a contratar.
# Para llegar al codigo, el dui debe pasar las validaciones. Si las pasa, se mostraran los servicios existentes. Y para poder consolidar la contratacion, se deben pasasr las validaciones de que el servicio no este contratado por nadie mas y que el codigo ingresado coincida con los que estan ingresados.

# Si todo sale bien, el dui y el codigo se guardaran en listado de contrataciones.
def contratarService(dui):
    while True:    
        if cantDui(dui) == False:
                print("La cantidad de digitos del DUI es incorrecta. Intente de nuevo")
                break
        elif clientExist(dui) != True:
            print("El cliente no esta registrado.")
            break
        elif clientinService(dui) != False:
            print("El cliente ya tiene un servicio contratado.")
            break
        else:
            for servicio in ServiciosDispo.items():
                print(f"\n{servicio}")
            opc = input("Selecciona uno de los servicios o escribe 'Salir' para volver al menu: ").upper()
            if opc == "SALIR":
                print("Volviendo al menú...")
                break
            elif opc not in ServiciosDispo.keys():
                print("El código ingresado no existe en nuestra lista de servicios.")
            else:
                Dui = dui                
                listContrataciones[Dui] = opc                
                print(f"El cliente {Dui} a contratado su servicio {opc} con exito.")
                print(listContrataciones)
                break

def listClient4Service(contraSelect):
    contraSelect = contraSelect.upper()
    if contraSelect in ("WD", "DS", "ML" , "API"):
        print(f"\nClientes que contrataron {contraSelect}:")
        # Tengo mi diccionario clientes que tiene: dui y nombre y apellido
        # Y tengo mi diccionario contrataciones en donde esta : dui del cliente y servicio contratado.
        # Por lo tanto, es un for para buscar en la lista contraria con el dui
        #Este for busca cada par de valores y los servicios encontrados los probamos con el servicio ingresado que se busca, si coinciden, el dui de ese servicio que coincidio se impriem, cada uno de ellos.
        for dui, servicio in listContrataciones.items(): # listContrataciones{"DUI","Servicio"} saco cada par C-V del diccionario y guardo su info en orden, dui y servicio
            if servicio == contraSelect: # Todos los servicios que coincidan con el ingresado haran que se imprima su DUI correspondiente
                print(f"- {dui}")
            else:#Si no hay ninguna coincidencia, se regresa el mensaje
                print("Ningun cliente contrato este servicio.")
    elif contraSelect == "NO CONTRATADOS":
        print("\nClientes que NO han contratado ningún servicio:")
        #Aqui lo que hacemos es que para encontrar los que no han contratado, sacamos todos los dui's de clientes y comparamos cada uno con el que esta en lista de contrataciones, si el dui no esta(not in) en lista contrataciones, se imprimira por cumplir la condicion.
        for dui in clientes.keys():
            if dui not in listContrataciones:
                print(f"- {dui}")
            else:
                print("No hay clientes que no hayan contratado un servicio!!!!")
    else:
        print("Opcion no encontrada")

        

while True:
    """print(f"Lista de clientes: \n{clientes}")
    print(f"Lista de contrataciones: \n{listContrataciones}")"""
    try:
        print("\nMenú:" \
        "\n1) Crear cliente" \
        "\n2) Contratar servicio" \
        "\n3) Listar clientes por servicio"\
        "\n4) Salir")
        op = input("Elegí una opcion: ")

        if op == "1":
                varDui = input("\nIngresa el número de DUI (XXXXXXXX-X): ")
                if cantDui(varDui) == False:
                    print("El valor o cantidad de digitos del DUI es incorrecta. Intente de nuevo")
                elif duiUnique(varDui) == False:
                    print("El DUI ya esta registrado")
                else:
                    #Se deben guardar los resultados de cada funcion en una variable
                    varNombre = input("\nIngresa el nombre: ")
                    varApellido = input("\nIngresa el apellido: ")
                    if cantDatos (varNombre, varApellido) == False:
                        print("La cantidad de digitos en el nombre o apellido debe ser mayor o igual a 2.")
                    else:
                        crearCliente(varDui, varNombre, varApellido)
                        print (clientes)

        if op == "2":
            print("Escogiste Contratar servicio")
            print(clientes)
            if len(clientes) == 0:
                print("No hay clientes registrados aún. Registra un cliente primero.")
            else:
                DuiClient = input("Ingresa el número de DUI del cliente: ")
                contratarService(DuiClient)

        if op == "3":
            print("Listar clientes por servicio")
            if len(listContrataciones) == 0:
                print("No hay contrataciones registradas aún.")
            else:
                print("Selelecciona los servicios para ver quien los contrato: ")
                print("\nWD \nDS \nML \nAPI \nNo contratados")
                contraSelect = input("Selecciona cual listado quieres ver: ").upper()
                listClient4Service(contraSelect)
        if op == "4":
            print("Escogiste salir... Gracias.")
            break
    except ValueError:
        print("El valor ingresado no esta contemplado.")
    except TypeError:
        print("El valor ingresado no esta contemplado.")

