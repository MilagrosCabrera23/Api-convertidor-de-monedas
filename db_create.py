from app.database.db import Base, engine
from app.models.user import User 

print("Creando las tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas con éxito!")