import datetime
from importlib.metadata import metadata
import logging
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime, create_engine, Table
import pandas as pd #usamos la libreria de pandas para tratar los datos


engine= create_engine('postgresql://postgres:123456@localhost/proyecto_alkemy')
Base= declarative_base()


Session=sessionmaker(engine)
session=Session()

"""def creacion_primer_tabla():

    __tablename__ = 'proyecto_alkemy'
    

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    df=pd.read_csv('C:/proyectos Estadisticas/Proyecto alkemy/Trabajo practico 2/primera_tabla/python/archivo_final.csv')
    try:
        df.to_sql("primer_tabla", con=engine, if_exists="append") # con la funcion if_exists reemplazo las columnas creadas anteriomente para obtener las nuevas
    except Exception as ex:
        print(ex)"""













































def carga_datos(tabla_final:pd.DataFrame):
    engine= create_engine('postgresql://postgres:123456@localhost/proyecto_alkemy')
    meta = metadata(engine)
    insp = sqlalchemy.inspect(engine)
    if not insp.has_table('primer_tabla'):
        # Create the table
        sql_create_table = Table(
            'primer_tabla',
            meta,
            Column('Cod_localidad', Integer,nullable=False),
            Column('IdProvincia', Integer,nullable=False),
            Column('IdDepartamento', Integer,nullable=False),
            Column('Categoria', String,nullable=False),
            Column('Provincia', String,nullable=False),
            Column('Localidad', String,nullable=False),
            Column('Nombre', String,nullable=False),
            Column('Domicilio', String),
            Column('Codigo_postal', String),
            Column('Telefono', String),
            Column('Mail', String),
            Column('Web', String),
            Creado_el=Column(DateTime(), default=datetime.datetime.now())
        )

      
    meta.create_all()
    
    
    try:
        tabla_final.to_sql('primer_tabla', engine, index=False, if_exists='append')
    except:
        logging.info('Base de datos ya existe')

    logging.info('Close database successfully')
