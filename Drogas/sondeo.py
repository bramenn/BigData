import sys
import csv
import db
from modelo import *

# python3 sondeo.py inacutacion.csv 10
DEPARTAMENTOS = []
MUNICIPIOS = []


def insert_data(data):
    """Inserta una fila"""
    db.session.add(data)
    db.session.commit()

def serach_departamento_id(departamento):
    dept = db.session.query(Departamento).where(Departamento.departamento==departamento).first()
    return dept.id

def serach_municipio_id(municipio):
    muni = db.session.query(Municipio).where(Municipio.municipio==municipio).first()
    return muni.codigodane

def incautacion_model(codigodane, clasebien, fecha, cantidad):
    inca = Incautacion(
        clasebien=clasebien,
        fecha=fecha,
        cantidad=cantidad,
        id_muni=codigodane
    )
    return inca

def departamento_model(departamento):
    dept = Departamento(
        departamento=departamento
    )
    return dept

def municipio_model(codigodane, municipio, id_dept):
    muni = Municipio(
        codigodane=codigodane,
        municipio=municipio,
        id_dept=id_dept
    )
    return muni

if __name__ == "__main__":

    db.Base.metadata.create_all(db.conn)
    arg = sys.argv

    if len(arg) == 3:
        file_name = arg[1]
        element_len = arg[2]

        file = open(file_name, mode="r")
        list_data = {}
        limit_data = int(element_len)
        counter = 0
        ignorar = True
        for line in file:
            line = line.strip()
            fields = line.split(",")
            if ignorar:
                ignorar = False
            else:
                # Obrenemos la infromacion
                departamento = fields[0]
                municipio = fields[1]
                codigodane = fields[2]
                clasebien = fields[3]
                fecha = fields[4]
                cantidad = float(fields[5])

                if not departamento in DEPARTAMENTOS:
                    DEPARTAMENTOS.append(departamento)
                    dept_model = departamento_model(departamento)
                    insert_data(dept_model)


                if not municipio in MUNICIPIOS:
                    MUNICIPIOS.append(municipio)
                    id_dept = serach_departamento_id(departamento)
                    if id_dept:
                        muni_model = municipio_model(codigodane, municipio, id_dept)
                        insert_data(muni_model)
                    else:
                        print(f"No se inserto el registro municipio, no se encontro {departamento}")


                id_muni = serach_municipio_id(municipio)
                if id_muni:
                    inca_model = incautacion_model(id_muni, clasebien, fecha, cantidad)
                    insert_data(inca_model)
                else:
                    print(f"No se inserto el registro incautacion, no se encontro {municipio}")

            if counter >= limit_data:
                break

            counter += 1

    else:
        print("### Argumentos incorrectos")

    print("\nAll ready!! (∩｀-´)⊃━☆ﾟ.*･｡ﾟ")