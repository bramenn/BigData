from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


conn = create_engine("postgres://bigdata:bigdata@localhost/repoejemplo")

Session = sessionmaker(bind=conn)

session = Session()
Base = declarative_base()



