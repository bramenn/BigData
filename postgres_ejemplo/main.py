import db_test
from modules import *

def insert_user(description, state, age):
    """Inserta una fila en user_test dado los argumentos"""
    user = User(
        description=description,
        state=state,
        age=age
        )
    db_test.session.add(user)
    db_test.session.commit()

def insert_comment(body, id_u):
    """Inserta una fila en comment_test dado los argumentos"""
    comment = Comment(
        body=body,
        id_u=id_u
        )
    db_test.session.add(comment)
    db_test.session.commit()

def select_all_users_by_age(age):
    # Obtener todos los registros de la tabla user por edad
    cs_user = db_test.session.query(User).filter(User.age==age).all()
    for user in cs_user:
        print(f"id: {user.id} \t description: {user.description} \t state: {user.state} \t age: {user.age}")

def select_all_users_by_state(state):
    # Obtener todos los registros de la tabla user por estado
    cs_user = db_test.session.query(User).filter(User.state==state).all()
    for user in cs_user:
        print(f"id: {user.id} \t description: {user.description} \t state: {user.state} \t age: {user.age}")

def select_all_users():
    # Obtener todos los registros de la tabla user
    cs_user = db_test.session.query(User).all()
    for user in cs_user:
        print(f"id: {user.id} \t description: {user.description} \t state: {user.state} \t age: {user.age}")

def select_user_by_id(id):
    # Obtener un usuario por id
    cs_user = db_test.session.query(User).where(User.id==id).first()
    print(f"id: {cs_user.id} \t description: {cs_user.description} \t state: {cs_user.state} \t age: {cs_user.age}")
    return cs_user



def select_first_user():
    # Obtener el primer registro de la tabla user
    # Esto es un select sobre la tabla user_test
    cs_user = db_test.session.query(User).first()
    print(f"id: {cs_user.id} \t description: {cs_user.description} \t state: {cs_user.state} \t age: {cs_user.age}")

if __name__ == '__main__':
    # Crea todas as tablas respectivas a los modelos
    db_test.Base.metadata.create_all(db_test.conn)

    # Insertar una fila en la tabla user_test
    # insert_user(description="Informacion de prueba", state=1, age=22)




    # Mostrar un usuario
    # select_first_user()

    # Mostrar todos los usuarios
    # select_all_users()

    # Mostrar todos los usuarios por estado (True or False)
    # select_all_users_by_state(True)

    # Mostrar todos los usuarios por edad
    # select_all_users_by_age(22)

    # Mostrar usuario por id
    # select_user_by_id(1)


