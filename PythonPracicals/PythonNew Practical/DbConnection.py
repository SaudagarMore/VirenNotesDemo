import mysql.connector
class StudentDatabase:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",   # replace with your MySQL password
            database="student_db"
        )
        self.cursor = self.conn.cursor()

    def create_student(self, name, age):
        sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
        values = (name, age)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Student added successfully.")

    def read_students(self):
        self.cursor.execute("SELECT * FROM students")
        records = self.cursor.fetchall()
        if not records:
            print(" No student records found.")
        else:
            print("\n Student Records:")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

    def update_student(self, student_id, new_name, new_age):
        sql = "UPDATE students SET name = %s, age = %s WHERE id = %s"
        values = (new_name, new_age, student_id)
        self.cursor.execute(sql, values)
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(" Student record updated.")
        else:
            print(" Student not found.")

    def delete_student(self, student_id):
        sql = "DELETE FROM students WHERE id = %s"
        values = (student_id,)
        self.cursor.execute(sql, values)
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(" Student record deleted.")
        else:
            print(" Student not found.")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

#  Menu-Driven Application
def menu():
    db = StudentDatabase()
    while True:
        print("\n===== Student Management System (MySQL) =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            db.create_student(name, age)

        elif choice == '2':
            db.read_students()

        elif choice == '3':
            try:
                student_id = int(input("Enter student ID to update: "))
                name = input("Enter new name: ")
                age = input("Enter new age: ")
                db.update_student(student_id, name, age)
            except ValueError:
                print(" Invalid input. ID must be a number.")

        elif choice == '4':
            try:
                student_id = int(input("Enter student ID to delete: "))
                db.delete_student(student_id)
            except ValueError:
                print(" Invalid input. ID must be a number.")

        elif choice == '5':
            db.close_connection()
            print(" Exiting program.")
            break

        else:
            print(" Invalid choice. Try again.")
menu()