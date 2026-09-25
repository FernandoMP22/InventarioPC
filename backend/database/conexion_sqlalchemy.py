import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

servidor = os.getenv("DB_SERVER")
base_datos = os.getenv("DB_DATABASE")
usuario = os.getenv("DB_USER")
contrasena = os.getenv("DB_PASSWORD")

url_conexion = URL.create(
    "mssql+pyodbc",
    username=usuario,
    password=contrasena,
    host=servidor,
    database=base_datos,
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes"
    }
)

engine = create_engine(url_conexion)