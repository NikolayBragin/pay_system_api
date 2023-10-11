from fastapi import FastAPI


from user.user_api import user_router

# Создать базу данных
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

# Регистрация компонента
app.include_router(user_router)

