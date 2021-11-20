import db
from sqlalchemy import Column, Integer, Text, Boolean, String, ForeignKey, Float


class Incautacion(db.Base):
    __tablename__ = "incautacion"
    id = Column(Integer, primary_key=True)
    departamento = Column("departamento", Text)
    municipio = Column("municipio", Text)
    codigodane = Column("codigodane", Text)
    clasebien = Column("clasebien", Text)
    fecha = Column("fecha", Text)
    cantidad = Column("cantidad", Float)

