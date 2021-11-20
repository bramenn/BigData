import db
from modelo import *


def insert_user(departamento, munucipio, codigodane, clasebien, fecha, cantidad):
    """Inserta una fila en user_test dado los argumentos"""
    inca = Incautacion(
        departamento=departamento,
        munucipio=munucipio,
        codigodane=codigodane,
        clasebien=clasebien,
        fecha=fecha,
        cantidad=cantidad,
    )
    db.session.add(inca)
    db.session.commit()


if __name__ == "__main__":
    # Crea todas as tablas respectivas a los modelos
    db.Base.metadata.create_all(db.conn)
