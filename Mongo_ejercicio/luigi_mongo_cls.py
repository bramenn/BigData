from pymongo import *
import luigi
import os

ip = "localhost"
puerto = 27017

cliente = MongoClient(ip,puerto)

db = cliente["cultivos"]

# python3 luigi_mongo_cls.py ExtraerLuigi --local-scheduler

class SalidaConsulta(luigi.Task):
    def requires(self):
        pass

    def output(self):
        return luigi.LocalTarget("InfoAntioquia.csv")

    def run(self):
        os.system("mongo < cacaoAntioquia.js")
        os.system("mongoexport --db cultivos --collection Antioquia --type=csv --fields _id,value --out infoAntioquia.csv")

class ExtraerLuigi(luigi.Task):
    def requires(self):
        return [SalidaConsulta()]

    def output(self):
        return []

    def run(self):
        with self.input()[0].open() as fin:
            for linea in fin:
                cad = linea.split(",")
                reg = {cad[0]:cad[1]}
                print(reg)

if __name__ == '__main__':
    luigi.run()


