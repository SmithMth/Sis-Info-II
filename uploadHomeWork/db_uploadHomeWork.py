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
    with get_connection() as con:
        with con.cursor() as cur:
            query = """
                INSERT INTO submission (idStudent, idHomeWork, comment, submission_date) VALUES (%s, %s, %s, %s) RETURNING submission_id;
            """
            cur.execute(query, (idStudent, idHomeWork, comment, submission_date))
            submission_id = cur.fetchone()[0]
        con.commit()
    return submission_id

def add_file(submission_id, fileContent, fileType):
    with get_connection() as con:
        with con.cursor() as cur:
            query = """
                INSERT INTO file (submission_id, fileContent, fileType) VALUES (%s, %s, %s);
            """
            cur.execute(query, (submission_id, fileContent, fileType))
        con.commit()

def get_assignment_details(assignment_id):
    """Obtener detalles de la tarea basándose en su ID."""
    with get_connection() as con:
        with con.cursor() as cur:
            query = """
                SELECT title, description, due_date FROM homework WHERE idHomeWork = %s;
            """
            cur.execute(query, (assignment_id,))
            result = cur.fetchone()
    if result:
        return {"title": result[0], "description": result[1], "due_date": result[2]}
    return None

def get_subject_name(assignment_id):
    """Obtener el nombre de la materia basándose en el ID de la tarea."""
    with get_connection() as con:
        with con.cursor() as cur:
            query = """
                SELECT name FROM subject WHERE idAssinament = %s;  -- Asume que la columna con el nombre de la materia es 'name'
            """
            cur.execute(query, (assignment_id,))
            result = cur.fetchone()
    if result:
        return result[0]
    return None

def get_student_grades(student_id):
    # Utiliza la conexión de la base de datos proporcionada en los métodos de conexión
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # Llama al procedimiento almacenado en la base de datos
            cursor.callproc("get_student_grades", (student_id,))
            
            # Recupera los resultados
            results = cursor.fetc
    return results

def set_student(student_id):
    #FUlll
    # Utiliza la conexión de la base de datos proporcionada en los métodos de conexión
    pass