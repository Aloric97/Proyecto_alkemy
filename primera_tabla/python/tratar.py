import pandas as pd #usamos la libreria de pandas para tratar las columnas
import numpy as np #para tratar los valores de la columna que no aportan informacion
from datetime import datetime
import os

def tratar_primera_tabla():
    #RUTA DIRECTORIO
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


    # TRATAR RUTA 1
    Rutarelativa = (mes_anio+ '\\' + formato+ '_'+ 'museo.csv') # guardo el trozo de ruta que me falta para llegar a donde esta ubicado mi csv
    Rutasolicitada = os.path.join(Rutabase, Rutarelativa) #uno las dos rutas
    Rutasolicitada = os.path.abspath(Rutasolicitada) #resultado final es la ruta de mi directorio donde esta ubicado este scripts


    #TRATAMIENTO DE LA PRIMERA TABLA

    df1=pd.read_csv(Rutasolicitada) #leemos el csv que vamos a trabajar
    #me doy cuenta que hay columnans que deben ser renombradas para obtener mejor una coincidencia con las demas tablas
    df1=df1.rename(columns={'Cod_Loc':'Cod_localidad','nombre':'Nombre', 'categoria':'Categoría', 'provincia':'Provincia','CP':'Codigo_postal','telefono':'Teléfono', 'direccion':'Domicilio', 'localidad':'Localidad'})
    #Aparte de renombrar, ahora necesitamos eliminar columnas que no vamos a necesitar, en este caso uso la funcion drop y me fijo las posiciones de las columnas
    df1.drop(df1.columns[[3,5,16,12,10,17,18,19,20,21,22,23]], axis=1, inplace=True)

    #---------------------------------------------------------------------

    #TRATAMIENTO DE LA SEGUNDA TABLA

    # TRATAR RUTA 2
    Rutarelativa =(mes_anio+ '\\' + formato+ '_'+ 'cine.csv' )# guardo el trozo de ruta que me falta para llegar a donde esta ubicado mi csv
    Rutasolicitada = os.path.join(Rutabase, Rutarelativa) #uno las dos rutas
    Rutasolicitada = os.path.abspath(Rutasolicitada) #resultado final es la ruta de mi directorio donde esta ubicado este scripts

    df2=pd.read_csv(Rutasolicitada)
    df2 = df2.rename(columns={'Cod_Loc':'Cod_localidad','CP':'Codigo_postal', 'Dirección':'Domicilio'})
    df2['Codigo_postal'] = df2['Codigo_postal'].astype('object') #convertir a tipo object debido a que nuestros otros archivos trabajar con este tipo
    df2.drop(df2.columns[[3,6,16,12,10,17,18,19,20,21,22,23,24,25]], axis=1, inplace=True)
    
    #---------------------------------------------------------------------

    #TRATAMIENTO DE LA TERCERA TABLA

    # TRATAR RUTA 2
    Rutarelativa =(mes_anio+ '\\' + formato+ '_'+ 'biblioteca_popular.csv') # guardo el trozo de ruta que me falta para llegar a donde esta ubicado mi csv
    Rutasolicitada = os.path.join(Rutabase, Rutarelativa) #uno las dos rutas
    Rutasolicitada = os.path.abspath(Rutasolicitada) #resultado final es la ruta de mi directorio donde esta ubicado este scripts

    df3=pd.read_csv(Rutasolicitada)
    df3 = df3.rename(columns={'Cod_Loc':'Cod_localidad','CP':'Codigo_postal'}) #renombro las columnas para faclitar la comprension de la consigna
    df3['Web'] = df3['Web'].astype('object') #convertir a tipo object debido a que nuestros otros archivos trabajar con este tipo
    df3.drop(df3.columns[[3,5,7,11,13,17,18,19,20,21,22,23,24]], axis=1, inplace=True) #necesitamos eliminar columnas que no vamos a necesitar, en este caso uso la funcion drop y me fijo las posiciones de las columnas
    
    #TRATAMIENTO DE LA DE LAS 3 TABLAS CREADAS Y TRANSFORMARLA EN UNA

    df2 = df2.rename(columns={'Dirección':'Domicilio'})


    fusion = [df1,df2,df3]
    archivo_final = pd.concat(fusion)   
    #Me he dado cuenta que hay contenidos de las columnas, mail y telefono contiene valores "s/d" que no aporta informacion, por lo tanto he decidido pasarlos a nulo
    archivo_final['Teléfono']=archivo_final['Teléfono'].replace(['s/d'], np.nan)
    archivo_final['Mail']=archivo_final['Mail'].replace(['s/d'], np.nan)
    
    archivo_final=archivo_final.assign(fecha_carga = pd.to_datetime("today")) #agregamos la fecha de hoy para saber cuando hicimos la ultima carga
    
    return archivo_final
