from dotenv import dotenv_values
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean


class DataBase:
    __engine = create_engine(dotenv_values().get('USER_DB_URL'))
    __Base = declarative_base()
    __Session = sessionmaker(bind=__engine)    
    
    class CurrentUser(__Base):
        __tablename__ = 'current_user'
        
        id = Column(Integer, primary_key=True)
        django_id = Column(String)
        username = Column(String, unique=True)
        csrf_token = Column(String)
        auth_token = Column(String)
        logged = Column(Boolean)
        
    class OrderList(__Base):
        __tablename__ = 'order_list'
        
        id = Column(Integer, primary_key=True)
        collection_id = Column(Integer, unique=True)
        order = Column(String)
    
    @classmethod
    def create_table(cls):
        cls.__Base.metadata.create_all(cls.__engine)
        
    @classmethod
    def get_session(cls):
        session = cls.__Session()
        return session
    
session = DataBase.get_session()
user_model = DataBase.CurrentUser
order_model = DataBase.OrderList


if __name__ == '__main__':
    DataBase.create_table()