from sqlalchemy.sql.expression import text
import db
from sqlalchemy import Column, Integer, Text, ForeignKey, Float
from sqlalchemy.orm import relationship

class Departamento(db.Base):
    __tablename__ = "departamento"
    id_dept = Column(Text, primary_key=True)
    departamento_name = Column("departamento_name", Text)
    prom_puntaje_area_urbano = Column("prom_puntaje_area_urbano", Float)
    prom_puntaje_area_rural = Column("prom_puntaje_area_rural", Float)
    prom_puntaje_global = Column("prom_puntaje_global", Integer)
    colegio = relationship("Colegio")


class Colegio(db.Base):
    __tablename__ = "colegio"
    id_colegio = Column("id_colegio", Text, primary_key=True)
    nombre_muni_cole = Column("nombre_muni_cole", Text)
    naturaleza_cole = Column("naturaleza_cole", Text)
    area_ubicacion_cole = Column("area_ubicacion_cole", Text)
    id_dept = Column(Text, ForeignKey("departamento.id_dept"))
    estudiante = relationship("Estudiante")

class Estudiante(db.Base):
    __tablename__ = "estudiante"
    id_estut = Column("id_estut", Text, primary_key=True)
    genero_estut = Column("genero_estut", Text)
    puntaje_estunt = Column("puntaje_estunt", Integer)
    id_cole = Column(Text, ForeignKey("colegio.id_colegio"))