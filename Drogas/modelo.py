import db
from sqlalchemy import Column, Integer, Text, Boolean, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Departamento(db.Base):
    __tablename__ = "departamento"
    id = Column(Integer, primary_key=True)
    departamento = Column("departamento", Text)
    municipio = relationship("Municipio")
class Municipio(db.Base):
    __tablename__ = "municipio"
    codigodane = Column("codigodane", Text, primary_key=True)
    municipio = Column("municipio", Text)
    id_dept = Column(Integer, ForeignKey("departamento.id"))
    incautacion = relationship("Incautacion")

class Incautacion(db.Base):
    __tablename__ = "incautacion"
    id = Column(Integer, primary_key=True)
    clasebien = Column("clasebien", Text)
    fecha = Column("fecha", Text)
    cantidad = Column("cantidad", Float)
    id_muni = Column(Text, ForeignKey("municipio.codigodane"))
