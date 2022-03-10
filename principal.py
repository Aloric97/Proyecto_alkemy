
from tratar_mes import mover_archivo
import logging
from primera_tabla.python.tratar import tratar_primera_tabla
from creacion_tabla import creacion_primer_tabla
import requests as req



# inicializacion del logger
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)

if __name__ == '__main__':

    archivo='museo.csv'

    with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv') as rq:
        with open(archivo, 'wb') as file:
            file.write(rq.content)

    mover_archivo(dato_archivo=archivo)


    archivo='cine.csv'


    with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv') as rq:
        with open(archivo, 'wb') as file:
            file.write(rq.content)

    mover_archivo(dato_archivo=archivo)



    archivo='biblioteca_popular.csv'

    with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv') as rq:
        with open(archivo, 'wb') as file:
            file.write(rq.content)



    mover_archivo(dato_archivo=archivo)



        # proceso de transformacion en las tablas

    logging.info('Tratando la primera tabla...')
    tabla_final=tratar_primera_tabla()
    logging.info('TRATAMIENTO EXITOSO')


    logging.info('Incorporando los datos creado a la base de datos...')
    creacion_primer_tabla(tabla_final)
    logging.info('CREACION EXITOSA')


        #logging.info('Tratando la segunda tabla...')
        #tabla_final2=tratamiento_2da_tabla()


        #logging.info('Incorporando los datos creado a la base de datos...')
        #creacion_segunda_tabla(tabla_final2)
        #logging.info('TRATAMIENTO EXITOSO')

        #logging.info('Tratando la tercera tabla...')
        #tabla_final3=tratamiento_3da_tabla()


        #logging.info('Incorporando los datos creado a la base de datos...')
        #creacion_tercera_tabla(tabla_final3)
        #logging.info('TRATAMIENTO EXITOSO')