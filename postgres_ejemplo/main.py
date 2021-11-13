import db_test
from modules import *

if __name__ == '__main__':
    db_test.Base.metadata.create_all(db_test.conn)


