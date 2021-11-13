import db_test
from sqlalchemy import Column, Integer, Text, Boolean, String, ForeignKey, Float


class Usuario(db_test.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    description = Column("description", Text)
    state = Column("state", Boolean)
    age = Column("edagead", Integer)

class Comment(db_test.Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    body = Column("body", String(20))
    id_u = Column(Integer, ForeignKey("user.id"))

