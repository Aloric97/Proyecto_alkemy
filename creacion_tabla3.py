from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os



load_dotenv() #recupero la variable de entorno para la conexion
CONEXION_DATABASE = os.getenv('CONEXION_DATABASE')


def creacion_tercera_tabla(tabla_final3:pd.DataFrame):
    
    engine= create_engine(CONEXION_DATABASE)

    try:
        tabla_final3.to_sql("tercera_tabla", con=engine, if_exists="replace") # con la funcion if_exists reemplazo las columnas creadas anteriomente para obtener las nuevas

    except Exception as ex:
        print(ex)
