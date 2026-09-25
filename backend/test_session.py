from backend.database.session import get_db


generador = get_db()

session = next(generador)

print("Sesión creada correctamente:")
print(session)

session.close()

print("Sesión cerrada correctamente.")