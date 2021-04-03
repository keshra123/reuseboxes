from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime import sqlite3 from sqlite3 import Error

def create_connection(db_file):
    connection = None;
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
     
    return conn
create_connection("name_and_stuff.db") 
app = Flask(__name__)
def create_table(conn, guests):
     
    sql = """ INSERT INTO guests(name, email,uname,paswrd)
              VALUES(?,?,?,?) """ 
 
    c = conn.cursor()
    c.execute(sql,guests)
    return cur.lastrowid
def main():
    database = r"gast.db"
 
    sql_create_guests_table = """ CREATE TABLE IF NOT EXISTS guests (
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        uname text NOT NULL,
                                        pswrd text NOT NULL
 
                                    ); """
 
    conn = create_connection(database)
 
    if conn is not None:
        # maak gast table
        create_table(conn, sql_create_guests_table)
 
    else:
        print("Error! cannot create the database connection.")
 
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/xz4yamgs/acc_creation',methods=['POST'])
def acc_creation():
    return render_template('acc_creation.html')

    if request.method == 'POST':
        c = conn.cursor()
        guest_name = request.form.get('name')
        guest_email = request.form.get('email')
        guest_uname = request.form.get('uname')
        guest_pswrd = request.form.get('pswrd')
         try: sql = ("INSERT INTO databasename.tablename(columnName,columnName,columnName,columnName Ci) VALUES (%s,%s, %s, %s)")
            c.execute(sql,(name,email,uname,pswrd))
            connection.commit() #or "conn.commit()" (one of the two)
            return redirect('/')
        except:
            return 'Something is not right'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

