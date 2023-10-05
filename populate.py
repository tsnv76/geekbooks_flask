from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Book

engine = create_engine('sqlite:///books-collection.db')
# Свяжем engine с метаданными класса Base,
# чтобы декларативы могли получить доступ через экземпляры DBSession
Base.metadata.bind = engine

DBSesssion = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSesssion()

bookOne = Book(title="Чистый Python", author="Дэн Бейдер", genre="компьютерная литература", link="")
session.add(bookOne)
session.commit()
