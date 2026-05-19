import mysql.connector

def get_cat_facts():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cat_facts_db"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT fact FROM cat_facts")

    facts = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return facts