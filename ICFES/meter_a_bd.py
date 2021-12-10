import db
from modelos import *
from ordenamiento_de_info import main


def insert_data(data):
    """Inserta una fila"""
    db.session.add(data)
    db.session.commit()


if __name__ == "__main__":

    print("Creando las tablas necesarias")
    db.Base.metadata.create_all(db.conn)

    print("Obteniendo la infromación ya ordenada")
    DEPARTAMENTOS, COLEGIOS, ESTUDIANTES = main()

    print("Registrando todos los departamentos en la bd")
    for departamento in DEPARTAMENTOS:
        dept = Departamento(
            id_dept=DEPARTAMENTOS[departamento].id_dept,
            departamento_name=DEPARTAMENTOS[departamento].departamento_name,
            prom_puntaje_area_urbano=DEPARTAMENTOS[departamento].prom_puntaje_area_urbano,
            prom_puntaje_area_rural=DEPARTAMENTOS[departamento].prom_puntaje_area_rural,
            prom_puntaje_global=DEPARTAMENTOS[departamento].prom_puntaje_global,
        )
        print(
            "Registrando el departamento: ",
            f"{dept.id_dept} {dept.departamento_name} {dept.prom_puntaje_area_urbano}"
            f"{dept.prom_puntaje_area_rural} {dept.prom_puntaje_global}"
        )

        insert_data(dept)

    print("Registrando todos los colegios en la bd")
    for id_colegio in COLEGIOS:
        cole = Colegio(
            id_colegio=COLEGIOS[id_colegio].id_colegio,
            id_dept=COLEGIOS[id_colegio].id_dept,
            nombre_muni_cole=COLEGIOS[id_colegio].nombre_muni_cole,
            naturaleza_cole=COLEGIOS[id_colegio].naturaleza_cole,
            area_ubicacion_cole=COLEGIOS[id_colegio].area_ubicacion_cole,
        )
        print(
            "Registrando el colegio: ",
            f"{cole.id_colegio} {cole.id_dept} {cole.nombre_muni_cole}"
            f"{cole.naturaleza_cole} {cole.area_ubicacion_cole}"
        )
        insert_data(cole)

    print("Registrando todos los estudiantes en la bd")
    for id_estut in ESTUDIANTES:
        estudiante = Estudiante(
            id_estut=ESTUDIANTES[id_estut].id_estut,
            genero_estut=ESTUDIANTES[id_estut].genero_estut,
            puntaje_estunt=ESTUDIANTES[id_estut].puntaje_estunt,
            id_cole=ESTUDIANTES[id_estut].id_cole,
        )
        print(
            "Registrando al estudiante: ",
            f"{estudiante.id_estut} {estudiante.genero_estut} {estudiante.puntaje_estunt}"
            f"{estudiante.id_cole}"
        )
        insert_data(estudiante)

