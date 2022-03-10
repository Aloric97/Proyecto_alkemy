import shutil
import datetime
from datetime import date
from pathlib import Path  
from datetime import datetime
import os

wd = os.getcwd()  #con esta funcion obtengo la ruta de donde estoy ejecutando mi archivo principal
Rutabase = wd



fecha_hoy = datetime.now() #obtengo la fecha de hoy en formato estandar: ejemplo "2022-03-09 23:33:34.410883"
anio=fecha_hoy.year #Obtengo solo el año

formato = fecha_hoy.strftime('%d-%m-%Y') #nuevo formato que representa el dia-mes-año

mes=fecha_hoy.month # obtengo el mes y luego me conviene crear un diccionario para transformarlo a string


tratar_mes= {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio',7:'julio',8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
mes_cadena=tratar_mes[mes]

def mover_archivo(dato_archivo):
    dato=dato_archivo #guardo el parametro obtenido del .csv


    nombre_carpeta = Rutabase # trato la carpeta donde estoy ubicado
    if not os.path.isdir(str(nombre_carpeta ) +'\\'+ str(anio)+'-'+(mes_cadena)): #agrego nueva carpeta y pongo el año-mes, ejemplo:01-febrero
        #no existe la carpeta, se crea
        os.mkdir(str(nombre_carpeta) +'\\'+ str(anio)+'-'+(mes_cadena))
    direccion=(str(nombre_carpeta ) +'\\'+ str(anio)+'-'+(mes_cadena))


    desde = Path(Rutabase +"\\" + dato) #guardamos el directorio donde nos dirigimos
    archivo = f"{str(formato)}_{desde.name}" # creamos el archivo solicitado con el formato (dia-mes-año)-archivo.csv
    hasta = Path(direccion).joinpath(archivo) # lo guardamos
    shutil.move(desde.resolve(), hasta.resolve()) # y finalmente lo movemos hacia las carpeta creadad en "direccion" y "archivo"
