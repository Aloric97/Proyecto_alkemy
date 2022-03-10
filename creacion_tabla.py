from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import pandas as pd #usamos la libreria de pandas para tratar los datos
from dotenv import load_dotenv
import os



load_dotenv() #recupero la variable de entorno para la conexion
CONEXION_DATABASE = os.getenv('CONEXION_DATABASE')


def creacion_primer_tabla(tabla_final:pd.DataFrame):
    
    engine= create_engine(CONEXION_DATABASE)
    try:
        tabla_final.to_sql("primer_tabla", con=engine, if_exists="replace") # con la funcion if_exists reemplazo las columnas creadas anteriomente para obtener las nuevas
    except Exception as ex:
        print(ex)
