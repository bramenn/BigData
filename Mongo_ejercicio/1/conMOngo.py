from pymongo import *

if __name__ == '__main__':
    ip = "localhost"
    puerto = 27017

    cliente = MongoClient(ip,puerto)

    db = cliente["cultivos"]

    consulta = {"DEPARTAMENTO":"AMAZONAS"}
    registros = db.Cacao.find(consulta)

    for registro in registros:
        print(f"{registro.get('MUNICIPIO')} \t {registro.get('CULTIVO')} \t {type(registro)}")