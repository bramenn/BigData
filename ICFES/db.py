from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


conn = create_engine("postgresql://bigdata:bigdata@localhost/icfes202021")

Session = sessionmaker(bind=conn)

session = Session()
Base = declarative_base()



