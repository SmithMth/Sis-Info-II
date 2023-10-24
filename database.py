import psycopg2

# Configuración de conexión
DB_NAME = "sis"
DB_USER = "smith"
DB_PASS = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
