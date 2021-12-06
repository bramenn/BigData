from pymongo.message import query
import db
from modelos import *
from ordenamiento_de_info import main

query_dept = []


def departamento_model(departamento):
    dept = Departamento(
        id_dept=departamento.id_dept
        departamento_name=departamento.id_dept
        prom_puntaje_area_urbano=departamento.id_dept
        prom_puntaje_area_rural=departamento.id_dept
        prom_puntaje_global=departamento.id_dept
    )
    return dept

if __name__ == '__main__':
    db.Base.metadata.create_all(db.conn)

    DEPARTAMENTOS, COLEGIOS, ESTUDIANTES = main()

    contador_dept = 0
    contador_cole = 0
    contador_estut = 0

    for departamento in DEPARTAMENTOS:
        if contador_dept <= 100:



