import psycopg2

# Configuración de conexión
DB_NAME = "b0zyrecsgde9whh1dmka"
DB_USER = "uehhymdo1hkrhqcxc3qz"
DB_PASS = "WCWL5On4oVwb5AOnWjDYGi5KCvyiAY"
DB_HOST = "b0zyrecsgde9whh1dmka-postgresql.services.clever-cloud.com"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

def add_submission(idStudent, idHomeWork, comment, submission_date):
    con = get_connection()
    cur = con.cursor()
    query = """
        INSERT INTO submission (idStudent, idHomeWork, comment, submission_date) VALUES (%s, %s, %s, %s) RETURNING submission_id;
    """
    cur.execute(query, (idStudent, idHomeWork, comment, submission_date))
    submission_id = cur.fetchone()[0]
    con.commit()
    cur.close()
    con.close()
    return submission_id

def add_file(submission_id, fileContent, fileType):
    con = get_connection()
    cur = con.cursor()
    query = """
        INSERT INTO file (submission_id, fileContent, fileType) VALUES (%s, %s, %s);
    """
    cur.execute(query, (submission_id, fileContent, fileType))
    con.commit()
    cur.close()
    con.close()

def get_assignment_details(assignment_id):
    """Obtener detalles de la tarea basándose en su ID."""
    con = get_connection()
    cur = con.cursor()
    query = """
        SELECT title, description, due_date FROM homework WHERE idHomeWork = %s;
    """
    cur.execute(query, (assignment_id,))
    result = cur.fetchone()
    cur.close()
    con.close()
    if result:
        return {"title": result[0], "description": result[1],"due_date": result[2]}
    return None

def get_subject_name(assignment_id):
    """Obtener el nombre de la materia basándose en el ID de la tarea."""
    con = get_connection()
    cur = con.cursor()
    query = """
        SELECT name FROM assignament WHERE idAssinament = %s;  -- Asume que la columna con el nombre de la materia es 'name'
    """
    cur.execute(query, (assignment_id,))
    result = cur.fetchone()
    cur.close()
    con.close()
    if result:
        return result[0]
    return None

