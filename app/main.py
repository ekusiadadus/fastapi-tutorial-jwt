from fastapi import FastAPI
from db import session
from model import UserTable, User


app = FastAPI()

@app.get("/users")
def get_user_list():
    users = session.query(UserTable).all()
    return users

# get user by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user

# create user
@app.post("/users/create")
def create_user(user: User):
    new_user = UserTable(
        name=user.name,
        password=user.password,
        refresh_token=user.refresh_token
    )
    session.add(new_user)
    session.commit()
    return new_user

# update user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    session.query(UserTable).filter(UserTable.id == user_id).update(
        {
            "name": user.name,
            "password": user.password,
            "refresh_token": user.refresh_token
        }
    )
    session.commit()
    return "update success"

# delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()
    return "delete success"

# login
@app.post("/login")
def login (username: str, password: str):
    user = session.query(UserTable).filter(UserTable.name == username).first()
    if not user:
        return False
    if not user.password == password:
        return False
    return user
