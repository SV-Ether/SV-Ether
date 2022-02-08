import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='Saraswathi', database='test')
cursor = conn.cursor()
cursor.autocommit = True
def clean_db():
    # CLEAN THE DATA
    cursor.execute("DROP DATABASE Vaccination")
def create_db():
    cursor.execute("CREATE DATABASE Vaccination")
    cursor.execute("USE Vaccination")
    # Table students (Sno, Name, Age, No. of Vaccinations, Date of last Vaccination)
    cursor.execute("CREATE TABLE students (Sno INT, Name VARCHAR(20), Age INT, No_of_Vaccinations INT, Date_of_last_Vaccination DATE)")
def insert_db():
    # INSRT RANDOM DATA WITH MYSQL VARIABLE SUBSTITUITION
    cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s)", (1, 'Saraswathi', 20, 2, '2020-01-01'))
    cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s)", (2, 'Sandur', 18, 2, '2020-01-01'))
    cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s)", (3, 'MSK', 40, 2, '2020-01-01'))
    cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s)", (4, 'Karthik', 25, 2, '2020-01-01'))
    conn.commit()
def update_db():
    # UPDATE THE DATA
    cursor.execute("UPDATE students SET Age = %s WHERE Sno = %s", (30, 1))
    cursor.execute("UPDATE students SET Name = %s WHERE Sno = %s", ('Saraswathi', 2))
    cursor.execute("UPDATE students SET No_of_Vaccinations = %s WHERE Sno = %s", (3, 3))
    cursor.execute("UPDATE students SET Date_of_last_Vaccination = %s WHERE Sno = %s", ('2020-01-01', 4))
    conn.commit()
def delete_db():
    # DELETE THE DATA
    cursor.execute("DELETE FROM students WHERE Sno = %s", (1,))
    conn.commit()
def display_db():
    # DISPLAY THE DATA
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

clean_db()
create_db()
insert_db()
update_db()
delete_db()
display_db()