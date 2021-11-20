import sys
import csv
import db
from modelo import *

# python3 sondeo.py inacutacion.csv 10


def insert_inca(departamento, municipio, codigodane, clasebien, fecha, cantidad):
    """Inserta una fila en incautacion dado los argumentos"""
    inca = Incautacion(
        departamento=departamento,
        municipio=municipio,
        codigodane=codigodane,
        clasebien=clasebien,
        fecha=fecha,
        cantidad=cantidad,
    )
    db.session.add(inca)
    db.session.commit()


if __name__ == "__main__":
    db.Base.metadata.create_all(db.conn)
    arg = sys.argv

    if len(arg) == 3:
        print("Cantidad de argumentos correctos!")
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
                # Insertamos la informacion
                insert_inca(
                    fields[0],
                    fields[1],
                    fields[2],
                    fields[3],
                    fields[4],
                    float(fields[5]),
                )
            if counter >= limit_data:
                break

            counter += 1

    else:
        print("### Argumentos incorrectos")
