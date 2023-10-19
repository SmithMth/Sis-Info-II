import psycopg2
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_meet_link():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            host="b0zyrecsgde9whh1dmka-postgresql.services.clever-cloud.com",
            database="b0zyrecsgde9whh1dmka",
            user="uehhymdo1hkrhqcxc3qz",
            password="WCWL5On4oVwb5AOnWjDYGi5KCvyiAY"
        )
        cursor = connection.cursor()

        # Get the current date and time
        current_date = datetime.now().date()
        current_time = datetime.now().time()

        # SQL query to fetch "name" and "link" based on the specified conditions
        query = """
            SELECT m.idassinament ,m.link, s.name
            FROM meet AS m
            INNER JOIN subject AS s ON m.idassinament = s.idassinament
            WHERE m.start_date <= %s AND m.end_date >= %s AND m.hour = %s
        """
        cursor.execute(query, (current_date, current_date, current_time))
        fetched_records = cursor.fetchall()

        # Initialize variables to store the name and link
        id_subject = ""
        link = ""
        name_subject = ""

        # Loop through the fetched records and store the name and link
        for record in fetched_records:
            id_subject, link, name_subject = record  
            query_student = """
                SELECT e.name, e.email
                FROM student AS e 
                INNER JOIN student_assignament ON e.idstudent = idstudent
                where idassignament = %s
            """
            cursor.execute(query_student,(id_subject,))
            email_student = cursor.fetchall()
            email_to_send = ""
            name_student = ""
            for datas in email_student:
                name_student, email_to_send = datas
                send_meet(name_student,name_subject,link,email_to_send)
            

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while fetching and sending meet links:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

def send_meet(name, name_subject, link, email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'fantasticos705@gmail.com' 
    password = 'wdoy xmzx zcwt recw'
    sender = 'fantasticos705@gmail.com'  # Replace with your Gmail address

    addressee = email

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = addressee
    message['Subject'] = name_subject
    body = f"Hola {name}, aquí está el enlace de la reunión: {link}"
    message.attach(MIMEText(body, 'plain'))

    try:
        server_smtp = smtplib.SMTP(smtp_server, smtp_port)
        server_smtp.starttls()
        server_smtp.login(username, password)
        server_smtp.sendmail(sender, addressee, message.as_string())
        server_smtp.quit()
        print("Correo enviado con éxito")
    except Exception as e:
        print("Error al enviar el correo:", str(e))

send_meet("jose","Fisica","https://meet.google.com/cez-rpvx-oun","jacaceresc12@gmail.com")