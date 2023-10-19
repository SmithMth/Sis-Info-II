import psycopg2
from datetime import datetime

import psycopg2
from datetime import datetime

def fetch_meet_links():
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

        # SQL query to fetch meeting assignments based on date range and hour
        query = """
            SELECT idassignment, link
            FROM meet
            WHERE start_date <= %s AND end_date >= %s AND hour = %s
        """
        cursor.execute(query, (current_date, current_date, current_time))
        fetched_records = cursor.fetchall()

        # Initialize variables to store the link and id
        meet_link = ""
        id_assignment = ""

        # Loop through the fetched records and store the link and id
        for record in fetched_records:
            id_assignment, meet_link = record  # Assign values to the variables
        
           

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while fetching and sending meet links:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    fetch_meet_links()
