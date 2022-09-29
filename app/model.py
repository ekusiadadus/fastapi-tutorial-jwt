from urllib.parse import scheme_chars
from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel
from db import Base
from db import ENGINE

class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    refresh_token = Column(nullable=True)

class User(BaseModel):
  id: int
  name: str
  password: str
  refresh_token: str

class Token(BaseModel):
    access_token: str
    token_type: str


def main():
  Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
  main()