import sys
import pandas as pd
from db_table import db_table

def import_agenda(file_path):
    # Load the agenda data from the Excel file
    agenda_data = pd.read_excel(file_path, skiprows=14)

    # Define the schema
    agenda_schema = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "date": "TEXT",
        "time_start": "TEXT",
        "time_end": "TEXT",
        "type": "TEXT",
        "title": "TEXT",
        "location": "TEXT",
        "description": "TEXT",
        "speaker": "TEXT"
    }

    # Create the agenda table
    agenda_table = db_table("agenda", agenda_schema)

    # Insert the agenda data into the database
    for _, row in agenda_data.iterrows():
        agenda_record = {
            "date": row['*Date'],
            "time_start": row['*Time Start'],
            "time_end": row['*Time End'],
            "type": row['*Session or \nSub-session(Sub)'],
            "title": row['*Session Title'],
            "location": row['Room/Location'],
            "description": row['Description'],
            "speaker": row['Speakers']
        }
        agenda_table.insert(agenda_record)

    # Close the database connection
    agenda_table.close()
    print("Data successfully imported into database.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./import_agenda.py agenda.xls")
    else:
        import_agenda(sys.argv[1])
