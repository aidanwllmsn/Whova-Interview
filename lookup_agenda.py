import sys
import sqlite3

def lookup_agenda(column, value):

    # Mapping of column names to their indexes
    column_indexes = {
        "date": 1,
        "time_start": 2,
        "time_end": 3,
        "title": 5,
        "location": 6,
        "description": 7,
        "speaker": 8
    }

   # Valid column names based on your database schema
    valid_columns = column_indexes.keys()

    # Validate the column name input
    if column not in valid_columns:
        print(f"Invalid column name. Valid columns are: {', '.join(valid_columns)}")
        return

    # Connect to the database
    conn = sqlite3.connect('interview_test.db')
    cursor = conn.cursor()

    # Get all agenda items sorted by their order in the database
    cursor.execute("SELECT * FROM agenda ORDER BY id")
    all_records = cursor.fetchall()

    # Flag for if a matching session was found
    session_found = False
    # Iterate over all records
    for i, record in enumerate(all_records):
        # Check if the session matches and handle None values safely
        if record[4] == 'Session' and record[column_indexes[column]] == value:
            session_found = True # Flag matching session was found
            print(f"Date: {record[1]}, Title: {record[5]}, Location: {record[6]}, Type: {record[4]}")
            # look for the subsessions that are directly below this session
            for j in range(i + 1, len(all_records)):
                next_record = all_records[j]
                if next_record[4] == 'Sub':  # If the next record is a subsession
                    print(f"Date: {next_record[1]}, Title: {next_record[5]}, Location: {next_record[6]}, Type: {next_record[4]}")
                else:
                    break  # Stop if the next record is another session

    if not session_found:
        print("No matching records found.")

    # Close connection with database
    cursor.close()
    conn.close()

if __name__ == "__main__":
    # Check for invalid command
    if len(sys.argv) < 3:
        print("Usage: ./lookup_agenda.py column value")
    else:
        column = sys.argv[1]
        value = " ".join(sys.argv[2:]) # Allow multi-word values
        lookup_agenda(column, value)
