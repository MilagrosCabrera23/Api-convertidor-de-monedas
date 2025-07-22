from app.database.bd import Base, engine
from app.models.users import User 
from app.models.convert import Convert

print("Creando las tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas con éxito!")