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
def get_all_classrooms():
    """Retrieve all classrooms."""
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute("SELECT classroom_id, name, capacity FROM classrooms;")
            classrooms = cur.fetchall()
    return classrooms

def get_available_time_slots(classroom_id, date):
    """Get available time slots for a specific classroom and date."""
    with get_connection() as con:
        with con.cursor() as cur:
            query = """
            SELECT time_slot_id, start_time, end_time
            FROM time_slots
            WHERE time_slot_id NOT IN (
                SELECT time_slot_id
                FROM classroom_reservations
                WHERE classroom_id = %s AND reservation_date = %s
            );
            """
            cur.execute(query, (classroom_id, date))
            time_slots = cur.fetchall()
    return time_slots
def get_all_time_slots():
    """Retrieve all time slots."""
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute("SELECT time_slot_id, start_time, end_time FROM time_slots;")
            time_slots = cur.fetchall()
    return time_slots



def reserve_classroom(classroom_id, time_slot_id, student_id, date):
    """Reserve a classroom for a specific date and time."""
    with get_connection() as con:
        with con.cursor() as cur:
            query = """
            INSERT INTO classroom_reservations (classroom_id, time_slot_id, student_id, reservation_date)
            VALUES (%s, %s, %s, %s);
            """
            cur.execute(query, (classroom_id, time_slot_id, student_id, date))
        con.commit()

def get_student_reservations(student_id):
    """Retrieve all reservations for a specific student."""
    with get_connection() as con:
        with con.cursor() as cur:
            query = """
            SELECT c.name, c.capacity, t.start_time, t.end_time
            FROM classroom_reservations as r
            JOIN classrooms as c ON r.classroom_id = c.classroom_id
            JOIN time_slots as t ON r.time_slot_id = t.time_slot_id
            WHERE r.student_id = %s;
            """
            cur.execute(query, (student_id,))
            reservations = cur.fetchall()
    return reservations


#Fin reserva aulas ---------------------------------------------------------------

def get_student_grades(student_id):
    # Utiliza la conexión de la base de datos proporcionada en los métodos de conexión
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # Llama al procedimiento almacenado en la base de datos
            cursor.callproc("get_student_grades", (student_id,))
            
            # Recupera los resultados
            results = cursor.fetchall()  # Corregido aquí
    return results