from fastapi import FastAPI
import db
from modelos import *

app = FastAPI()


@app.get("/puntaje_globla_dep/{departamento}")
def read_root(departamento: str):
    departamento_dict = obtener_departamento_por_nombre(departamento)
    return departamento_dict

@app.get("/obtener_departamentos")
def read_root():
    departamentos_dict = obtener_departamentos()
    return departamentos_dict

def obtener_departamentos():
    departamentos_db =db.session.query(Departamento).all()
    deptos_dic = {}
    for departamento in departamentos_db:
        deptos_dic[departamento.id_dept] = {
        "departamento_name": departamento.departamento_name,
        "prom_puntaje_area_urbano": departamento.prom_puntaje_area_urbano,
        "prom_puntaje_area_rural": departamento.prom_puntaje_area_rural,
        "prom_puntaje_global": departamento.prom_puntaje_global,
    }

    return deptos_dic
def obtener_departamento_por_nombre(departamento: str):

    depto = (
        db.session.query(Departamento)
        .where(Departamento.departamento_name == departamento)
        .first()
    )

    departamento_db = {
        "id_dept": depto.id_dept,
        "departamento_name": depto.departamento_name,
        "prom_puntaje_area_urbano": depto.prom_puntaje_area_urbano,
        "prom_puntaje_area_rural": depto.prom_puntaje_area_rural,
        "prom_puntaje_global": depto.prom_puntaje_global,
    }

    return departamento_db
