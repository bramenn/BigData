from pymongo import *
from pymongo import collection

ip = "localhost"
puerto = 27017
cliente = MongoClient(ip, puerto)
db = cliente["drogas"]


DEPARTAMENTOS = {}
MUNICIPIOS = {}

def registrar_dept(registro):
    if not registro.get("DEPARTAMENTO") in DEPARTAMENTOS:
        dep_dict = {"incautaciones": 0, "cantidad": 0, "municipios": []}
        DEPARTAMENTOS[registro.get("DEPARTAMENTO")] = dep_dict


def registrar_inc(registro):
    global DEPARTAMENTOS
    dept_incautacion = registro.get("DEPARTAMENTO")
    data_dict = DEPARTAMENTOS.get(dept_incautacion)
    incautaciones = data_dict.get("incautaciones") + 1
    if isinstance(registro.get("CANTIDAD"), str):
        cantidad = data_dict.get("cantidad") + int(registro.get("CANTIDAD").replace(".", ""))
    else:
        cantidad = data_dict.get("cantidad") + registro.get("CANTIDAD")
    dep_dict = {
        "incautaciones": incautaciones,
        "cantidad": cantidad,
    }
    # get_inca_by_muni(dept_incautacion, registro.get("MUNICIPIO"))
    DEPARTAMENTOS[dept_incautacion] = dep_dict


def get_inca_by_muni(DEPARTAMENTO, MUNICIPIO):
    global MUNICIPIOS
    if not MUNICIPIO in MUNICIPIOS:
        incautaciones = registros = db.drogas_regs.find(
            {"$and":[{"DEPARTAMENTO": DEPARTAMENTO}, {"MUNICIPIO": MUNICIPIO}]}
        ).count()

        registros = db.drogas_regs.find(
            {"$and":[{"DEPARTAMENTO": DEPARTAMENTO}, {"MUNICIPIO": MUNICIPIO}]}
        )

        cantidad = 0
        for registro in registros:
            if isinstance(registro.get("CANTIDAD"), str):
                cantidad = cantidad + int(registro.get("CANTIDAD").replace(".", ""))
            else:
                cantidad = cantidad + registro.get("CANTIDAD")
        data_dic = {"incautaciones":incautaciones, "cantidad":cantidad}
        MUNICIPIOS[MUNICIPIO] = data_dic


if __name__ == "__main__":
    registros = db.drogas_regs.find()
    len_regs = db.drogas_regs.find().count()
    print(len_regs)
    for registro in registros:
        registrar_dept(registro)
        registrar_inc(registro)

    for dept in DEPARTAMENTOS:
        print(f"{dept} \t {DEPARTAMENTOS.get(dept)}")
        # creamos la coleccion
        coleccion = db[dept]
        data_dict = DEPARTAMENTOS.get(dept)
        coleccion.insert_one(data_dict)

    # print(db.list_collection_names())
