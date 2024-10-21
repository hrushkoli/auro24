import mysql.connector

def connect_to_db():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydb"
    )
        return mydb
    except mysql.connector.Error as err:
        print("Error connecting to databse: ",err)
        return None

def create_student_table(mydb,cursor):
    query= """
    CREATE TABLE IF NOT EXISTS student(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        grade VARCHAR(10),
        email VARCHAR(100)
    )
    """
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("ERROR Creating Table: ", err)

def insert_student_dta(mydb,cursor):
    name = input("Enter Student Name:")
    age = input("Enter Student Age:")
    grade = input("Enter Student Grade")
    email = input("Enter Student Email")

    query= ("INSERT INTO STUDENT (name,age,grade,email) VALUES (%s,%s,%s,%s)")
    values = (name,age,grade,email)

    try:
        cursor.execute(query,values)
        mydb.commit()
        print("Student Data Inserted Successfully")

    except mysql.connector.Error as err:
        print("Error Inserting Data: ",err)

def read_student_data(mydb,cursor):
    
