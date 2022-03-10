
import pandas as pd #usamos la libreria de pandas para tratar las columnas
import numpy as np #para tratar los valores de la columna que no aportan informacion
import os


absolutepath = os.path.abspath('cine.csv')
print(absolutepath)

def tratamiento_3da_tabla():
    wd = os.getcwd()  #con esta funcion obtengo la ruta de donde estoy ejecutando mi archivo principal
    Rutabase = wd
    Rutarelativa = 'tercera_tabla/cine.csv' # guardo el trozo de ruta que me falta para llegar a donde esta ubicado mi csv
    Rutasolicitada = os.path.join(Rutabase, Rutarelativa) #uno las dos rutas
    Rutasolicitada = os.path.abspath(Rutasolicitada) #resultado final es la ruta de mi directorio donde esta ubicado este scripts

    df=pd.read_csv(Rutasolicitada)


    df['espacio_INCAA']=df['espacio_INCAA'].replace([np.nan], 0) # para poder tratar los espacio, reemplacé los nulos por 0
    df['espacio_INCAA']=df['espacio_INCAA'].replace(['si'], 1) #los que eran si, tome como 1 haciendo referencia a que existe el espacio y se toma como cantidad 1
    df['espacio_INCAA']=df['espacio_INCAA'].replace(['SI'], 1) # observé que hay "si" en mayúscula, por lo tanto lo tomé tambien como 1 dando a entender que existe

    df['espacio_INCAA'] = df['espacio_INCAA'].astype(int)  # transformé la columna a entero para poder tratarlo matématicamente

    Total=df.groupby(['Provincia'])[['Pantallas','Butacas', 'espacio_INCAA']].apply(sum) #los agrupé por provincia, entendiendo que pide la cantidad total por cada provincia y los acumulé en las 3 columnas solicitadas

    Total=Total.reset_index() # transforme el indice de mi provincia en una columna
    Total=Total.rename(columns={'Pantallas':'Cantidad pantallas','Butacas':'Cantidad butacas', 'espacio_INCAA': 'Cantidad espacio INCAA'}) #modifiqué los nombre de mis columnas para tener una mejor comprensión de los resultados
    return Total
