from pymongo import *
import luigi

ip = "localhost"
port = 27017

nom_db = "cultivos"

cliente = MongoClient(ip, port)

db = cliente[nom_db]

# python3 luigi_mongo.py Extraer --local-scheduler

class Extraer(luigi.Task):
    def requires(self):
        return ()

    def output(self):
        return []

    def run(self):
        consulta = {"DEPARTAMENTO":"AMAZONAS"}
        registro = db.Cacao.find_one(consulta)
        print(registro)

if __name__ == '__main__':
    e = Extraer()
    e.run()
