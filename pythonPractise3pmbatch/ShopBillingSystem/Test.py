import mysql.connector
# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="6pmdatabase"
)
cursor = conn.cursor()
print("Connected to MySQL!")

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        age INT
    )
""")
# ─────────────────────────────────────────────
# FUNCTIONS
# ─────────────────────────────────────────────
def insert_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
    cursor.execute(sql, (name, age))
    conn.commit()
    print("Student inserted successfully!\n")

def update_student():
    sid = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    sql = "UPDATE students SET name=%s, age=%s WHERE id=%s"
    cursor.execute(sql, (name, age, sid))
    conn.commit()
    print("Student updated successfully!\n")

def delete_student():
    sid = int(input("Enter student ID to delete: "))
    sql = "DELETE FROM students WHERE id=%s"
    cursor.execute(sql, (sid,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Student Not Found On This id")
    else:
        print("Student deleted successfully!\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in result:
        print(row)
    print()

def view_studentbyid():
    sid=int(input("Enter student ID to view: "))
    sql = "SELECT * FROM students WHERE id=%s"
    cursor.execute(sql, (sid,))
    result = cursor.fetchall()
    if cursor.rowcount==0:
        print("Student Not Found On This id")
    else:
        print("\n--- Student Records ---")
        for row in result:
            print(row)
        print()
# ─────────────────────────────────────────────
# MENU
# ─────────────────────────────────────────────
while True:
    print("""
===== STUDENT MANAGEMENT =====
1. Insert Student
2. Update Student
3. Delete Student
4. View All Students
5. View Student By id
6. Exit
""")

    choice = input("Enter your choice: ")
    if choice == "1":
        insert_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        view_students()
    elif choice == "5":
        view_studentbyid()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid option! Try again.\n")

cursor.close()
conn.close()