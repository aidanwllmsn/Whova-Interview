import sqlite3

def is_table_empty():
    db_connection = sqlite3.connect('interview_test.db')
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM agenda")
    count = cursor.fetchone()[0]

    if count == 0:
        print("The agenda table is empty.")
    else:
        print(f"The agenda table contains {count} records.")

    db_connection.close()

def print_table_schema(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()

    print("Column Index | Column Name")
    print("-" * 30)
    for column in columns:
        index = column[0] 
        name = column[1] 
        print(f"{index:<14} | {name}")

    cursor.close()
    conn.close()

def print_all_data():
    conn = sqlite3.connect('interview_test.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM agenda;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    is_table_empty()
    print_table_schema('interview_test.db', 'agenda')
    print_all_data()