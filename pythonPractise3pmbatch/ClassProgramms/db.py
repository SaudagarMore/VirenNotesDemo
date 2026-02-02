import mysql.connector

# ----------------------------
# Database Connection
# ----------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change as needed
        password="root",  # change as needed
        database="college1"
    )

# ----------------------------
# CREATE
# ----------------------------
def add_employee():
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)",
                (name, department, salary))
    conn.commit()
    print(" Employee added successfully!")

    cur.close()
    conn.close()

# ----------------------------
# READ
# ----------------------------
def view_employees():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()

    print("\n--- Employee Records ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Dept: {row[2]} | Salary: {row[3]}")
    print("-------------------------")

    cur.close()
    conn.close()

# ----------------------------
# UPDATE
# ----------------------------
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    name = input("Enter new name: ")
    department = input("Enter new department: ")
    salary = float(input("Enter new salary: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE employees SET name=%s, department=%s, salary=%s WHERE id=%s",
        (name, department, salary, emp_id)
    )
    conn.commit()

    if cur.rowcount > 0:
        print(" Employee updated successfully!")
    else:
        print(" Employee ID not found.")

    cur.close()
    conn.close()

# ----------------------------
# DELETE
# ----------------------------
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    conn.commit()

    if cur.rowcount > 0:
        print(" Employee deleted successfully!")
    else:
        print(" Employee ID not found.")

    cur.close()
    conn.close()

# ----------------------------
# MENU
# ----------------------------
def menu():
    while True:
        print("\n=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

# ----------------------------
# Run Program
# ----------------------------
if __name__ == "__main__":
    menu()
