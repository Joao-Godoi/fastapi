from sqlalchemy import Column, Integer, String

from src.utils.database import Base


class BlogModel(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
