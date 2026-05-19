from flask import Blueprint, render_template,request,url_for,redirect
import mysql.connector
from businessLogic import ask_cat_bot

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cat_facts_db"
    )


views = Blueprint('views',__name__)
@views.route('/', methods=["GET","POST"])
def Default():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE email = %s",
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user is None:

            cursor.execute(
            """
            INSERT INTO users (firstname,lastname,email)
            VALUES(%s,%s,%s)
            """,
            (firstname, lastname,email)
        )

        #save changes
        conn.commit()
        conn.close()
        return redirect(url_for('views.dash')) 

    return render_template('home.html')

@views.route('/dash', methods=["POST","GET"])
def dash():
    response = None
    if request.method == "POST":
        user_input = request.form.get("message")
        if user_input:
            response = ask_cat_bot(user_input)
    return render_template('dash.html', response=response)