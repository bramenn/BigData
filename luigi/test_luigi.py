import luigi

# python3 -m luigi --module test_luigi Cuadrados --n 15 --local-scheduler
# python3 test_luigi.py Cuadrados --local-scheduler --n 30
class SalidaNumeros(luigi.Task):
    """Creamos un archivo y le asiganos numeros del 1 al 11"""
    n = luigi.IntParameter()
    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget(f"numeros_{self.n}.txt")

    def run(self):
        with self.output().open("w") as f:
            for i in range(1,self.n+1):
                f.write(f"{i}\n")

class Cuadrados(luigi.Task):
    """
    Toma el proceso anterior y saca los numeros y los eleva al cuadrado
    Los resultados los guarda en un archivo diferente
    """

    n = luigi.IntParameter(default=10)

    def requires(self):
        return [SalidaNumeros(n = self.n)]

    def output(self):
        return luigi.LocalTarget(f"cuadrados_{self.n}.txt")

    def run(self):
        with self.input()[0].open() as fin, self.output().open("w") as fout:
            for linea in fin:
                n = int(linea.strip())
                val = n**2
                fout.write(f"{n}:{val}\n")

if __name__ == '__main__':
    luigi.run()
