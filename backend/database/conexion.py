import pyodbc


def obtener_conexion():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=DESKTOP-VTAJONH\\SQLEXPRESS;"
        "DATABASE=InventarioPC;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return conexion