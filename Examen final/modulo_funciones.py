#En este modulo crearemos las funciones del sistema

#Importamos el modulo de datos -
import modulo_datos as dat 

def registrar_estudiante(): 
    """Validara y registrara estudiantes"""
    while True:
        carnet_i=input("Ingrese su numero de carnet: ") #si un numero no se utilizara como numero, se mantiene como texto
        largo_carnet=len(carnet_i)
        existe= False 
        for estu in dat.estudiantes:
            if estu["carnet"]==carnet_i:
                existe=True      
        if largo_carnet>=6 and largo_carnet<=10 and existe==False:
            #if existe==False:
                break  
        else:
            print("El carnet no tiene el largo requerido o existe") 
        
    while True:         
        nombre_i=input("Ingrese su nombre: ").capitalize() 
        largo_nombre=len(nombre_i)
        if largo_nombre>1:
            break 
        else:
            print("El nombre no tienen el largo requerido")
                
    while True:   
        apellido_i=input("Ingrese su apellido: ").capitalize() 
        largo_apellido=len(apellido_i)
        if largo_apellido>1:
            break
        else:
            print("El apellido no tiene el largo requerido")
    
    dat.estudiantes.append({ 
        "carnet": carnet_i,
        "nombre": nombre_i,
        "apellido": apellido_i
    })

print(dat.estudiantes) 
    
def inscribir_curso():
    """Inscripcion"""
    while True:
        carnet_es=input("Ingrese su carnet: ").lower() 
        if carnet_es=="salir":
            break 
        #Verificar si existe el carnet
        existe=False 
        for estu in dat.estudiantes:
            if estu["carnet"]==carnet_es:
                existe=True  
                break
        if existe:
            print(dat.cursos) 
            
            #Validar la eleccion
            eleccion=input("Ingresa el codigo del curso que quieras realizar (ej. PY para Python): ").upper()
            
            if eleccion not in dat.cursos:
                print("Esa opcion no esta en los cursos disponibles")
                continue  
            
            #Validar la inscripcion 
            inscrito=False 
            for ins in dat.inscripciones:
                if ins[0]== carnet_es and ins[1]==eleccion:
                    inscrito=True 
                    break 
            if inscrito:
                print("Ya estas inscrito en este curso")
            else:
                dat.inscripciones.append((
                carnet_es,eleccion
            )) 
                print("La inscripcion fue un exito")
            print(dat.inscripciones)     
        else:
            print("Debes de registrarte ") 
            
def generar_reporte():
    """Reporte"""
    while True:
        if len(dat.inscripciones)==0:
            print("No hay inscripciones registradas") 
            break
        
        print("""
              Submenu:
              1. PY
              2. JS
              3. BD
              4. SE
              5. Estudiantes sin inscripcion
              6. Salir""") 
        opcion=input("Elija una seccion (1-6): ")
        
        if opcion=="1":
            inscritos_py=[] 
            
            for carnet_es, eleccion in dat.inscripciones:
                if eleccion=="PY":
                    inscritos_py.append(carnet_es) 
            if len(inscritos_py)==0:
                print("No hay ninguna inscripccion en este curso")
            else:
                print("Estudiantes inscritos en Python Basico: ")
                for carnet in inscritos_py:
                    print("-", carnet)
        
        if opcion=="2":
            inscritos_js=[]
            
            for carnet_es, eleccion in dat.inscripciones:
                if eleccion=="JS":
                    inscritos_js.append(carnet_es)
            if len(inscritos_js)==0:
                print("No hay estudiantes inscritos en este curso")
            else:
                print("Estudiantes inscritos en JavaScript para Principiantes:")
                for carnet in inscritos_js:
                    print("-", carnet) 
        
        if opcion=="3":
            inscritos_bd=[]
            
            for carnet_es, eleccion in dat.inscripciones:
                if eleccion=="BD":
                    inscritos_bd.append(carnet_es)
            if len(inscritos_bd)==0:
                print("No hay estudiantes inscritos en este curso ")
            else:
                print("Estudiantes inscritos en Base de Datos:")
                for carnet in inscritos_bd:
                    print("-", carnet)
        
        if opcion=="4":
            inscritos_se=[]
            
            for carnet_es, eleccion in dat.inscripciones:
                if eleccion=="SE":
                    inscritos_se.append(carnet_es)
            if len(inscritos_se)==0:
                 print("No hay estudiantes inscritos en este curso ")
            else:
                print("Estudiantes inscritos en Seguridad de Entornos Digitales:")
                for carnet in inscritos_se:
                    print("-", carnet)
        
        if opcion=="5":
            no_inscritos=[]
            
            for carnet_i in dat.estudiantes:
                no_inscritos.append(carnet_i) 
            if len(no_inscritos)==0:
                print("Todos los estudiantes se han inscrito a un curso")
            else:
                print("Estudiantes no inscritos: ")
                for estu in no_inscritos:
                    print("-", estu)
                    
        if opcion=="6":
            print("Volviendo al menu principal")
            break