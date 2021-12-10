from typing import List, Optional, Tuple
from pymongo import *


ip = "localhost"
puerto = 27017
cliente = MongoClient(ip, puerto)
db = cliente["icfes"]

DEPARTAMENTOS = {}
COLEGIOS = {}
ESTUDIANTES = {}


class Departamento:
    """Clase referente a un departamento"""
    id_dept: str
    departamento_name: str

    def __init__(
        self,
        id_dept: str,
        departamento_name: str,
    ):
        self.id_dept = id_dept
        self.departamento_name = departamento_name

        self.prom_puntaje_area_urbano = 0
        self.prom_puntaje_global = 0
        self.prom_puntaje_area_rural = 0

        self.lista_puntajes_urbanos = []
        self.lista_puntajes_rurales = []

    def procesar_promedio_urbano(self) -> None:
        """Este metodo toma la lista de puntajes urbanos y calcula el promedio en esta area"""
        puntajes_urbano_sum = sum(self.lista_puntajes_urbanos)
        print(
            f"Obteniendo de la sumatoria de los puntajes urbanos ... ",
            f"la sumatoria de {self.departamento_name} es {puntajes_urbano_sum} de "
            "{len(self.lista_puntajes_urbanos)} puntajes"
        )
        if self.lista_puntajes_urbanos:
            print("Obteniendo el promedio urbano ...")
            promedio_urbano = puntajes_urbano_sum / len(self.lista_puntajes_urbanos)
            self.prom_puntaje_area_urbano = promedio_urbano
        else:
            self.prom_puntaje_area_urbano = 0
        print(f"El promedio urbano de {self.departamento_name} es {self.prom_puntaje_area_urbano}")

    def procesar_promedio_rural(self) -> None:
        """Este metodo toma la lista de puntajes rurales y calcula el promedio en esta area"""
        puntajes_rural_sum = sum(self.lista_puntajes_rurales)
        print(
            f"Obteniendo de la sumatoria de los puntajes rurales ... ",
            f"la sumatoria de {self.departamento_name} es {puntajes_rural_sum} de "
            "{len(self.lista_puntajes_urbanos)} puntajes"
        )
        if self.lista_puntajes_rurales:
            print("Obteniendo el promedio rural ...")
            promedio_rural = puntajes_rural_sum / len(self.lista_puntajes_rurales)
            self.prom_puntaje_area_rural = promedio_rural
        else:
            self.prom_puntaje_area_rural = 0
        print(f"El promedio rural de {self.departamento_name} es {self.prom_puntaje_area_rural}")

    def procesar_promedio_global(self) -> None:
        print("Sacando el promedio urbano ...")
        self.procesar_promedio_urbano()
        print("Sacando el promedio rural ...")
        self.procesar_promedio_rural()

        len_puntajes = len(self.lista_puntajes_urbanos) + len(self.lista_puntajes_rurales)
        if len_puntajes > 0:
            self.prom_puntaje_global = (
                sum(self.lista_puntajes_urbanos) + sum(self.lista_puntajes_rurales)
            ) / len_puntajes
        else:
            self.prom_puntaje_global = 0

        print(
            f"El promedio global de {self.departamento_name} es {self.prom_puntaje_global} de "
            f"{len_puntajes} puntajes."
        )


class Colegio:
    """Clase referente a un colegio"""
    id_colegio: str
    id_dept: str
    nombre_muni_cole: str
    naturaleza_cole: str
    area_ubicacion_cole: str

    def __init__(
        self,
        id_colegio: str,
        nombre_cole: str,
        id_dept: str,
        nombre_muni_cole: str,
        naturaleza_cole: str,
        area_ubicacion_cole: str,
    ):
        self.id_colegio = id_colegio
        self.nombre_cole = nombre_cole
        self.id_dept = id_dept
        self.nombre_muni_cole = nombre_muni_cole
        self.naturaleza_cole = naturaleza_cole
        self.area_ubicacion_cole = area_ubicacion_cole


class Estudiante:
    """Clase referente a un estudiante"""
    id_estut: str
    genero_estut: str
    puntaje_estunt: int
    id_cole: str

    def __init__(self, id_estut: str, genero_estut: str, puntaje_estunt: int, id_cole: str):
        self.id_estut = id_estut
        self.genero_estut = genero_estut
        self.puntaje_estunt = puntaje_estunt
        self.id_cole = id_cole


def registar_estut(id_estut: str, genero_estut: str, puntaje_estunt: int, id_cole: str):
    """Esta funcion registra un estudiante en el dict ESTUDIANTES"""
    global ESTUDIANTES

    print(f"Verificando si el estudiante {id_estut} ya existe ...")
    if not id_estut in ESTUDIANTES:
        estudiante = Estudiante(id_estut, genero_estut, puntaje_estunt, id_cole)
        ESTUDIANTES[id_estut] = estudiante
        print(f"Estudiante {estudiante.id_estut} registrado correctamente")
    else:
        print(f"Este estudiante {id_estut} ya se encuentra registrado")


def registar_cole(
    id_colegio: str,
    nombre_cole: str,
    id_dept: str,
    nombre_muni_cole: str,
    naturaleza_cole: str,
    area_ubicacion_cole: str,
):
    """Esta funcion registra un estudiante en el dict ESTUDIANTES"""

    global COLEGIOS

    print(f"Verificando si el colegio {id_colegio} ya existe ...")
    if not id_colegio in COLEGIOS:
        colegio = Colegio(
            id_colegio,
            nombre_cole,
            id_dept,
            nombre_muni_cole,
            naturaleza_cole,
            area_ubicacion_cole,
        )
        COLEGIOS[id_colegio] = colegio
        print(f"Colegio {colegio.nombre_cole} registrado correctamente")
    else:
        print(f"Este colegio {nombre_cole} ya se encuentra registrado")


def registar_dep(id_dept: str, departamento_name: str):
    """Esta funcion registra un departamento en el dict DEPARTAMENTOS"""

    global DEPARTAMENTOS

    print(f"Verificando si el departamento {id_dept} ya existe ...")
    if not id_dept in DEPARTAMENTOS:
        depto = Departamento(id_dept, departamento_name)
        DEPARTAMENTOS[id_dept] = depto
        print(f"Departamento {depto.departamento_name} registrado correctamente")
    else:
        print(f"Este departamento {departamento_name} ya se encuentra registrado")


def main() -> Tuple:
    """Funcion principal"""

    print("Trayendo todos los registros guardados en la bd icfes en la coleccion icfes_regs de mongodb")
    resgistros_icfes = db.icfes_regs.find()
    contador = 0
    for resgistro_icfes in resgistros_icfes:

        # obtenemos la infromación necesaría

        id_depto = resgistro_icfes.get("COLE_COD_DEPTO_UBICACION")
        nombre_depto = resgistro_icfes.get("COLE_DEPTO_UBICACION")

        id_cole = resgistro_icfes.get("COLE_COD_DANE_ESTABLECIMIENTO")
        nombre_cole = resgistro_icfes.get("COLE_NOMBRE_ESTABLECIMIENTO")
        nombre_muni_cole = resgistro_icfes.get("COLE_MCPIO_UBICACION")
        naturaleza_cole = resgistro_icfes.get("COLE_NATURALEZA")
        area_ubicacion_cole = resgistro_icfes.get("COLE_AREA_UBICACION")

        id_estut = resgistro_icfes.get("ESTU_CONSECUTIVO")
        genero_estut = resgistro_icfes.get("ESTU_GENERO")
        puntaje_estunt = resgistro_icfes.get("PUNT_GLOBAL")

        # registramos los datos en los diccionarios

        registar_dep(id_dept=id_depto, departamento_name=nombre_depto)

        if area_ubicacion_cole == "URBANO":
            DEPARTAMENTOS[id_depto].lista_puntajes_urbanos.append(puntaje_estunt)
        elif area_ubicacion_cole == "RURAL":
            DEPARTAMENTOS[id_depto].lista_puntajes_rurales.append(puntaje_estunt)
        else:
            print(f"Este registro no tiene un area definida {area_ubicacion_cole}")

        registar_cole(
            id_colegio=id_cole,
            nombre_cole=nombre_cole,
            id_dept=id_depto,
            nombre_muni_cole=nombre_muni_cole,
            naturaleza_cole=naturaleza_cole,
            area_ubicacion_cole=area_ubicacion_cole,
        )
        registar_estut(
            id_estut=id_estut,
            genero_estut=genero_estut,
            puntaje_estunt=puntaje_estunt,
            id_cole=id_cole,
        )

        contador += 1

    print("\n\n################################")
    print(f"Numero de registros procesados {contador}")
    print(f"Numero de departamentos guardados {len(DEPARTAMENTOS)}")
    print(f"Numero de colegios guardados {len(COLEGIOS)}")
    print(f"Numero de estudiantes guardados {len(ESTUDIANTES)}")
    print("################################")

    return (DEPARTAMENTOS, COLEGIOS, ESTUDIANTES)
    