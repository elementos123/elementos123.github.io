import os
from time import sleep
import vlc
from datetime import date
import shutil
import getpass
import platform
   
   
class colores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
   
   
class variables:
    correcto = False # False en caso de querer que se puedan loguear más de 1 usuario
    usuarioin = ""
        


def Add_Date():
    informacion = input("Escriba lo que desea hacer: ")
    today = date.today()
    fechainscrito = today.strftime("%d/%m/%Y") # Fecha en formato español
    fechalimite = input("Escriba la fecha límite: ")
    cuandoavisar = input("Escriba la fecha para que se le avise: ")
    archivo = open("calendario.txt", 'a') # Abrimos el archivo en modo lectura y escritura pero esto no borra el contenido
    archivo.write(informacion+";"+fechainscrito+";"+fechalimite+";"+cuandoavisar+"\n")
    archivo.close()
    
    print("\n\n1 -> Añadir una fecha\n\n2 -> Ver calendario" + "\n\n")

    opcion = input("Elige una opción, 1 o 2: ")

    if opcion == "1":
        Add_Date()
    elif opcion == "2":
        Cargar_Fechas()
    else:
        DecisionDespuesDeIniciarSesion()



def Cargar_Fechas():

    variables.correcto = False

    # Abrimos el archivo en modo lectura
    archivo = open("calendario.txt", 'r')
            
    os.system("cls")
    for linea in archivo:
        informaciongeneral, fechainscrito, fechalimite, cuandoavisar = linea.split(";")
        print("<======================INFO=========================>\n")
        dia, mes, anio = cuandoavisar.split("/")
        today = date.today()
        today = today.strftime("%d/%m/%Y")
        diat, mest, aniot = today.split("/")
        fechalimitesdia, fechalimitesmes, fechalimitesanio = fechalimite.split("/")
                
        if int(diat) > int(fechalimitesdia):
            operaciondias = int(int(diat) - int(fechalimitesdia))
        else:
            operaciondias = int(int(fechalimitesdia) - int(diat))

        operacionmes = int(int(mest) - int(fechalimitesmes))
        operacionanio = int(int(aniot) - int(fechalimitesanio))
        operaciontotal = str(operaciondias)
        
        if not operacionmes == 0 and not operacionmes == 00:
            operaciontotal += str(operacionmes)

        if not operacionanio == 0 and not operacionanio == 00 and not operacionanio == 0000:
            operaciontotal += str(operacionanio)
            
        print(f"{colores.BOLD}" + " · " + informaciongeneral + f"{colores.ENDC}")
        print(" · " + " Fue inscrito en " + fechainscrito)
        print(" · " + "Te avisamos el " + cuandoavisar.replace("\n", ""))
        print(f"{colores.BOLD}" + " · " + "Fecha limite: " + fechalimite + f"{colores.ENDC}")

        fechahoy = diat+mest+aniot
        fechalimitesuma = fechalimitesdia+fechalimitesmes+fechalimitesanio
                
        if operaciontotal <= "0":
            print(f"{colores.RED}" + " · CUIDADO QUE YA ESTÁS CERCA DE LA FECHA LIMITE" + f"{colores.ENDC}")
            if not os.path.isfile("alarma.mp3"):
                print("\n\n" + "Debes poner el sonido alarma.mp3 en la carpeta del usuario" + "\n\n")
                os.system("pause")
            p = vlc.MediaPlayer("alarma.mp3")
            p.play()
            
            
            if int(fechahoy) > int(fechalimitesuma):
                if int(fechahoy) - int(fechalimitesuma) == 1:
                    print(f"{colores.RED}" + " · Te queda 1 día para llegar a la fecha límite" f"{colores.ENDC}")
                else:
                    print(f"{colores.RED}" + " · Te queda " + str(int(fechahoy) - int(fechalimitesuma)) +  " días para llegar a la fecha límite" f"{colores.ENDC}")
            else:
                if int(fechahoy) - int(fechalimitesuma) == 1:
                    print(f"{colores.RED}" + " · Te queda 1 día para llegar a la fecha límite" f"{colores.ENDC}")
                elif int(fechahoy) - int(fechalimitesuma) > 0:
                    operacion2 = int(int(fechalimitesuma) - int(fechahoy))
                    print(f"{colores.RED}" + " · Te queda " + str(operacion2) +  " días para llegar a la fecha límite" f"{colores.ENDC}")
                else:
                    print(f"{colores.RED}" + " · ¡Ya estás en la fecha límite!" f"{colores.ENDC}")
        
        else:
            

            if int(diat) > int(dia):
                operaciondias = int(int(diat) - int(dia))
            else:
                operaciondias = int(int(dia) - int(diat))

            operacionmes = int(int(mest) - int(mes))
            operacionanio = int(int(aniot) - int(anio))
            operaciontotal2 = str(operaciondias)
        
            if not operacionmes == 0 and not operacionmes == 00:
                operaciontotal2 += str(operacionmes)

            if not operacionanio == 0 and not operacionanio == 00 and not operacionanio == 0000:
                operaciontotal2 += str(operacionanio)
            
            
            
            if int(operaciontotal2) == 1:
                print(f"{colores.WARNING}" + " · Te queda 1 día para avisarte" f"{colores.ENDC}")
            elif int(operaciontotal2) > 1 and int(operaciontotal2) <= 3:
                print(f"{colores.WARNING}" + " · Te quedan " + str(operaciontotal2) + " días para avisarte" f"{colores.ENDC}") 
            elif int(operaciontotal2) > 3:
                print(f"{colores.OKGREEN}" + " · Te quedan " + str(operaciontotal2) + " días para avisarte" f"{colores.ENDC}")  
            else:
                print(f"{colores.RED}" + " · Estás en este día, hazlo antes del día: " + fechalimite +
                          "\n" + " · Te quedan " + f"{operaciontotal}" + " para que llegue ese día" + f"{colores.ENDC}")
                
                

        print("\n" + "<====================== FIN INFO =======================>\n\n")
                

        input("Presiona Enter para continuar...\n\n")

    archivo.close()
    
    archivo = open("calendario.txt", 'r')
    
    with open("calendario2.txt", "w") as f:
        for linea in archivo:
            informaciongeneral, fechainscrito, fechalimite, cuandoavisar = linea.split(";")
            today = date.today()
            today = today.strftime("%d/%m/%Y")
            diat, mest, aniot = today.split("/")
            fechalimitesdia, fechalimitesmes, fechalimitesanio = fechalimite.split("/")

            if int(diat) > int(fechalimitesdia):
                operaciondias = int(int(diat) - int(fechalimitesdia))
            else:
                operaciondias = int(int(fechalimitesdia) - int(diat))

            operaciontotal = str(operaciondias)
                

            if not operaciondias == 0:
                f.write(linea)
        
        
        f.close()
            
    archivo.close()
    os.replace("calendario.txt", "calendario2.txt")
    os.rename("calendario2.txt", "calendario.txt")
        
    print("\n\n1 -> Añadir una fecha\n\n2 -> Ver calendario" + "\n\n")

    opcion = input("Elige una opción, 1 o 2: ")
        
            
    if opcion == "1":
        Add_Date()
    elif opcion == "2":
        Cargar_Fechas()
    else:
        DecisionDespuesDeIniciarSesion()

                


    
def Registro():
    
    print("\n\n" + f"{colores.OKGREEN}" + "Te estás registrando" + f"{colores.ENDC}" + "\n\n")
    # Vemos si el archivo existe (True o False)
    if os.path.isfile("usuarios.txt"):
        # Abrimos el archivo en modo lectura y escritura pero esto no borra el contenido
        archivo = open("usuarios.txt", 'a')
    else:
        # Abrimos el archivo en modo escritura pero esto borra el contenido en caso de haber sido creado anteriormente
        archivo = open("usuarios.txt", 'w')
        print("Recuerda, que debes cambiar los permisos de usuarios.txt")

    usuario = input("Usuario: ") # Le preguntamos al usuario sobre el usuario que va a utilizar
    password = str(getpass.getpass()) # Le preguntamos al usuario sobre la contraseña
    # Escribimos los datos dados por el usuario
    archivo.writelines(usuario)
    archivo.writelines("\n")
    archivo.close()  # Cerramos el archivo

    if not os.path.isdir(usuario):
        os.mkdir(usuario)  # Creamos la carpeta del usuario
        # Creamos el archivo para almacenar las fechas
        if  platform.system() == "Linux":
            archivo = open(usuario + "/calendario.txt", 'w')
            archivo.close()
            archivo = open(usuario + "/credenciales.txt", "w")
            archivo.writelines(usuario+":"+password)
            os.system("sudo chown " + usuario+":"+usuario + usuario + "/credenciales.txt")
        elif platform.system() == "Windows":
            archivo = open(usuario + "\\calendario.txt", 'w')
            archivo.close()
            archivo = open(usuario + "\\credenciales.txt", "w")
            archivo.writelines(usuario+":"+password)

    archivo.close() # Cerramos el archivo
    # Imprimimos un mensaje de información
    print(f"{colores.OKGREEN}" + "Usuario creado con exito. Redirigiendo" + f"{colores.ENDC}")
    shutil.copy("alarma.mp3", usuario)
    sleep(2)
    os.system("cls")
    main()
        
    
    
def IniciarSesion():    
    # Vemos si el archivo existe (True o False)
    if not os.path.isfile("usuarios.txt"):
        # Enviamos un error para que lo coja el except
        Registro()

    archivo = open("usuarios.txt", "r")

    usuarioin = input("Usuario: ")

    passin = str(getpass.getpass())

    while archivo.readline():

        archivo.close()

        
        try:
            if platform.system() == "Linux":
                archivo = open(usuarioin + "/credenciales.txt", "r")
            else:
                archivo = open(usuarioin + "\\credenciales.txt", "r")
        except:
            main()
        usuario, password = archivo.readline().split(":")

        if usuarioin == usuario and passin == password.replace("\n", ""):
            variables.correcto = True
            break



    if not variables.correcto:  # Comprobamos si son cierto

        variables.correcto = False
        print("Contraseña no es correcta o usuario no existe")
        sleep(2)
        os.system("cls")
        IniciarSesion()

    else:
        variables.usuarioin = usuarioin

        # usuarioin en caso de querer que se puedan loguear más de 1 usuario
        os.chdir(variables.usuarioin)

        print("\n\n1 -> Añadir una fecha\n\n2 -> Ver calendario" + "\n\n")

        opcion = input("Elige una opción, 1 o 2: ")

        if opcion == "1":
            Add_Date()
        elif opcion == "2":
            Cargar_Fechas()
        else:
            DecisionDespuesDeIniciarSesion()
    
    
def DecisionDespuesDeIniciarSesion():
    
    print("\n\n1 -> Añadir una fecha\n\n2 -> Ver calendario" + "\n\n")

    opcion = input("Elige una opción, 1 o 2: ")
    
    if opcion == "1":
        Add_Date()
    elif opcion == "2":
        Cargar_Fechas()
    else:
        main()

def main():
    os.system("cls")
    print("\n\n1 -> Iniciar Sesión \n\n2 -> Registrarse" + "\n\n")
            
    opcion = input("Elige una opción, 1 o 2: ")
            
    if opcion == "1":
        IniciarSesion()
    elif opcion == "2":
        Registro()
    
    
    
    
main()
