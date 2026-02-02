import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',          # ✅ correct parameter name
        password='root',
        database='college1'
    )

    if conn.is_connected():
        print("✅ Database connected successfully!")

except Error as e:
    print("❌ Error:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔒 Connection closed.")
