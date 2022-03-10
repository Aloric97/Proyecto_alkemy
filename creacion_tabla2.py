from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import pandas as pd #usamos la libreria de pandas para tratar los datos
from dotenv import load_dotenv
import os



load_dotenv() #recupero la variable de entorno para la conexion
CONEXION_DATABASE = os.getenv('CONEXION_DATABASE')


def creacion_segunda_tabla(tabla_final2:pd.DataFrame):
    
    engine= create_engine(CONEXION_DATABASE)
    try:
        #Como pasé una lista de parametros, fui accediendo a ellos por los indices y tratando de forma separada 
        tabla_final2[0].to_sql("cantidad_por_categoria", con=engine, if_exists="replace") # con la funcion if_exists reemplazo las columnas creadas anteriomente para obtener las nuevas
        tabla_final2[1].to_sql("cantidad_por_fuente", con=engine, if_exists="replace") # con la funcion if_exists reemplazo las columnas creadas anteriomente para obtener las nuevas
        tabla_final2[2].to_sql("cantidad_por_categoriayprovincia", con=engine, if_exists="replace") # con la funcion if_exists reemplazo las columnas creadas anteriomente para obtener las nuevas

    except Exception as ex:
        print(ex)
