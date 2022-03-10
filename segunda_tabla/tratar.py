import pandas as pd #usamos la libreria de pandas para tratar las columnas
import numpy as np #para tratar los valores de la columna que no aportan informacion
from datetime import datetime
import os


def tratamiento_2da_tabla():
    #RUTA 1
    wd = os.getcwd()  #con esta funcion obtengo la ruta de donde estoy ejecutando mi archivo principal
    Rutabase = wd
    fecha_hoy = datetime.now()
    formato = fecha_hoy.strftime('%d-%m-%Y') #trato el valor de la fecha para recuperar la infomacion
    # TRATAR RUTA 1
    Rutarelativa = 'segunda_tabla/cine.csv' # guardo el trozo de ruta que me falta para llegar a donde esta ubicado mi csv
    Rutasolicitada = os.path.join(Rutabase, Rutarelativa) #uno las dos rutas
    Rutasolicitada = os.path.abspath(Rutasolicitada) #resultado final es la ruta de mi directorio donde esta ubicado este scripts

    df1=pd.read_csv(Rutasolicitada)

    #TRATAR RUTA 2
    Rutarelativa = 'segunda_tabla/museo.csv'
    Rutasolicitada = os.path.join(Rutabase, Rutarelativa) 
    Rutasolicitada = os.path.abspath(Rutasolicitada)

    
    df2=pd.read_csv(Rutasolicitada)

    #TRATAR RUTA 3
    Rutarelativa = 'segunda_tabla/biblioteca_popular.csv' 
    Rutasolicitada = os.path.join(Rutabase, Rutarelativa)
    Rutasolicitada = os.path.abspath(Rutasolicitada)
    df3=pd.read_csv(Rutasolicitada)
    
    
    df2=df2.rename(columns={
       'categoria':'Categoría', 'subcategoria':'Subcategoria', 'provincia':'Provincia', 'localidad':'Localidad', 'nombre':'Nombre',
       'direccion':'Domicilio', 'piso':'Piso','telefono':'Teléfono','fuente':'Fuente'}) #cambiamos el nombre para tener todas las columnas equivalentes


    df1=df1.rename(columns={'Dirección':'Domicilio','año_actualizacion':'Año_actualizacion' }) #cambiamos el nombre para tener todas las columnas equivalentes

    fusion = [df1,df2,df3]
    archivo_final = pd.concat(fusion)
    
    
    #observo que tengo columnas nulos, por lo tanto las elimino colocando su posicion
    archivo_final.drop(archivo_final.columns[[3,16,31]], axis=1, inplace=True) 

    #CANTIDAD DE REGISTROS TOTALES POR FUENTE
    cantidad_fuente=archivo_final.groupby(['Fuente']) #con la funcion 'groupby' por podemos obtener los totales de cada columna por las categorias existentes
    cantidad_fuente=cantidad_fuente.size() #obtengo la cantidad total por fuente
    cantidad_fuente=pd.DataFrame(cantidad_fuente, columns=['total']) # con esta funcion me encargo de tranformar la serie en dataframe, llamo total a la columna transformada
    cantidad_fuente=cantidad_fuente.reset_index() #Con esta opcion me encargo de tranformar el indice como columna
    cantidad_fuente=cantidad_fuente.assign(fecha_carga = pd.to_datetime("today")) #agregamos la fecha de hoy para saber cuando hicimos la ultima carga




    #CANTIDAD DE REGISTROS TOTALES POR CATEGORIA
    cantidad_categoria=archivo_final.groupby(['Categoría']) #con la funcion 'groupby' por podemos obtener los totales de cada columna por las categorias existentes
    cantidad_categoria=cantidad_categoria.size() #obtengo la cantidad total por categoria
    cantidad_categoria=pd.DataFrame(cantidad_categoria, columns=['total']) # con esta funcion me encargo de tranformar la serie en dataframe, llamo total a la columna transformada
    cantidad_categoria=cantidad_categoria.reset_index() #Con esta opcion me encargo de tranformar el indice como columna
    cantidad_categoria=cantidad_categoria.assign(fecha_carga = pd.to_datetime("today")) #agregamos la fecha de hoy para saber cuando hicimos la ultima carga




    #CANTIDAD DE REGISTROS TOTALES POR PROVINCIA Y CATEGORIA
    cantidad_provincia_categoria=archivo_final.groupby(['Provincia', 'Categoría']) # los agrupo primero por provincia, luego por categoria
    cantidad_provincia_categoria=cantidad_provincia_categoria.size() #obtengo la cantidad total por categoria y provincia
    cantidad_provincia_categoria=pd.DataFrame(cantidad_provincia_categoria, columns=['total']) # con esta funcion me encargo de tranformar la serie en dataframe, llamo total a la columna transformada
    cantidad_provincia_categoria=cantidad_provincia_categoria.reset_index()   #Con esta opcion me encargo de tranformar el indice como columna
    cantidad_provincia_categoria=cantidad_provincia_categoria.assign(fecha_carga = pd.to_datetime("today")) #agregamos la fecha de hoy para saber cuando hicimos la ultima carga




    return ([cantidad_fuente,cantidad_categoria, cantidad_provincia_categoria])

