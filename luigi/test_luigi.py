import luigi

# --local-scheduler
class SalidaNumeros(luigi.Task):
    """Creamos un archivo y le asiganos numeros del 1 al 11"""
    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("numeros.txt")

    def run(self):
        with self.output().open("w") as f:
            for i in range(1,11):
                f.write(f"{i}\n")

class Cuadrados(luigi.Task):
    """
    Toma el proceso anterior y saca los numeros y los eleva al cuadrado
    Los resultados los guarda en un archivo diferente
    """
    def requires(self):
        return [SalidaNumeros()]

    def output(self):
        return luigi.LocalTarget("cuadrados.txt")

    def run(self):
        with self.input()[0].open() as fin, self.output().open("w") as fout:
            for linea in fin:
                n = int(linea.strip())
                val = n**2
                fout.write(f"{n}:{val}\n")

if __name__ == '__main__':
    luigi.run()
