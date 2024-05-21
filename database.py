import sqlite3

#I use this function to create my tenant request database table everytime I want to start with a clean database

def create_properties_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('tenant_request.db')
    cursor = conn.cursor()

    # Create the properties table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tenant_request (
        id INTEGER PRIMARY KEY,
        tenant_name TEXT,
        tenant_email TEXT,
        location TEXT,
        property_type TEXT,
        agent_name TEXT
        
    )
    ''')

    conn.commit()
    conn.close()


create_properties_database()
