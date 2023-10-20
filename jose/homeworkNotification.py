import smtplib
import psycopg2  
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


data = None

def get_homeworks():
    global data

    hostname = "b0zyrecsgde9whh1dmka-postgresql.services.clever-cloud.com"
    database = "b0zyrecsgde9whh1dmka"
    username = "uehhymdo1hkrhqcxc3qz"
    password = "WCWL5On4oVwb5AOnWjDYGi5KCvyiAY"

    conn = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=password
    )
    cursor = conn.cursor()
    cursor.callproc('GetNextHomeworks')
    data = cursor.fetchall()
    cursor.close()
    conn.close()          

def send_notification():

    global data

    smtp_server = 'smtp.gmail.com'  
    smtp_port = 587  
    username = 'fantasticos705@gmail.com'
    password = 'wdoy xmzx zcwt recw'

    
    sender = ''

    for item in data:
        name = str(item[0])
        title = str(item[1])
        email = str(item[2])
        

        addressee = email

        
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = addressee
        message['Subject'] = title
        body = "Hola " + name + ", la tarea " + title + " se entrega pronto."
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

get_homeworks()
send_notification()