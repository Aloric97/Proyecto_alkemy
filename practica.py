import pandas as pd #usamos la libreria de pandas para tratar las columnas
import numpy as np #para tratar los valores de la columna que no aportan informacion
from datetime import datetime
import os

wd = os.getcwd()  #con esta funcion obtengo la ruta de donde estoy ejecutando mi archivo principal
Rutabase = wd


fecha_hoy = datetime.now() #obtengo la fecha de hoy en formato estandar: ejemplo "2022-03-09 23:33:34.410883"
anio=fecha_hoy.year #Obtengo solo el año

#fecha de hoy en formato estandar: ejemplo "2022-03-09 23:33:34.410883"
anio=fecha_hoy.year #Obtengo solo el año

formato = fecha_hoy.strftime('%d-%m-%Y') #nuevo formato que representa el dia-mes-año

mes=fecha_hoy.month # obtengo el mes y luego me conviene crear un diccionario para transformarlo a string
tratar_mes= {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio',7:'julio',8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
mes_cadena=tratar_mes[mes]

mes_anio=(str(anio)+ '-'+ mes_cadena)

print(mes_anio)


Rutarelativa = (mes_anio+ '\\' + formato+ '_'+ 'museo.csv')
print(Rutarelativa)
Rutasolicitada = os.path.join(Rutabase, Rutarelativa) #uno las dos rutas
Rutasolicitada = os.path.abspath(Rutasolicitada) #resultado final es la ruta de mi directorio donde esta ubicado este scripts

print(Rutasolicitada)