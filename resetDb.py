import sqlite3

def reset_database():
    # Connect to the SQLite database
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Delete all records from the 'users' table
    try:
        cursor.execute("DELETE FROM users")
        connection.commit()
        print("All data has been wiped from the database.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    reset_database()
