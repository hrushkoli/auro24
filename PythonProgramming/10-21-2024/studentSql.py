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
        age VARCHAR(3),
        name VARCHAR(100),
        grade VARCHAR(10),
        email VARCHAR(100)
    )
    """
    try:
        cursor.execute(query)
        mydb.commit()
        print("Created Student Table")
    except mysql.connector.Error as err:
        print("ERROR Creating Table: ", err)

def insert_student_data(mydb,cursor):
    name = input("Enter Student Name:")
    age = input("Enter Student Age:")
    grade = input("Enter Student Grade: ")
    email = input("Enter Student Email: ")

    query= ("INSERT INTO STUDENT (name,age,grade,email) VALUES (%s,%s,%s,%s)")
    values = (name,age,grade,email)

    try:
        cursor.execute(query,values)
        mydb.commit()
        print("Student Data Inserted Successfully")

    except mysql.connector.Error as err:
        print("Error Inserting Data: ",err)

def read_student_data(mydb,cursor):
    query = "SELECT * FROM student"
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print("Error Reading Data: ",err)

def update_student_data(mydb,cursor):
    student_id = input("Enter Student ID to Update: ")
    set_clause = input("Enter SET Clause (e.g.,(name = John, age = 20) :")
    query = f"UPDATE student SET {set_clause} WHERE id = {student_id}"

    try:
        cursor.execute(query)
        mydb.commit()
        print("Student Data Updated Successfully")

    except mysql.connector.Error as err:
        print("Error Updating Data: ",err)

def delete_student_data(mydb,cursor):
    student_id = input("Enter Student ID to Update: ")
    query= f"DELETE FROM student WHERE id = {student_id}"

    try:
        cursor.execute(query)
        mydb.commit()
        print("Student Data Deleted Successfully")

    except mysql.connector.Error as err:
        print("Error deleting Data: ",err)


def main():
    mydb = connect_to_db()
    if mydb is None:
        return

    cursor = mydb.cursor()
    print(cursor)
    
    while True:
        print("\n Menu: ")
        print("1. Create Student Table: ")
        print("2. Insert Student Data: ")
        print("3. Read Student Data: ")
        print("4. Update Student Data: ")
        print("5. Delete Student Data: ")
        print("6. Exit: ")
    
        choice = input("Enter your choice: ")
        
        if choice =="1":
            create_student_table(mydb,cursor)

        if choice =="2":
            insert_student_data(mydb,cursor)
    
        if choice =="3":
            read_student_data(mydb,cursor)

        if choice =="4":
            update_student_data(mydb,cursor)

        if choice =="5":
            delete_student_data(mydb,cursor)

        if choice =="6":
            break

        cursor.close()
        mydb.close()

if __name__ == "__main__":
    main()
