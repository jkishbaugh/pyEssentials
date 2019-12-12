#!usr/bin/env python3

import sqlite3

def main():
    db = sqlite3.connect('sample.db')
    # Create a new table that will store
    # first name, last name, address, city, state, zip, and phone number.
    cursor = db.cursor()
    cursor.execute("DROP TABLE if exists someTable")
    cursor.execute("""
        CREATE TABLE someTable
        (id INTEGER PRIMARY_KEY, 
        first_name TEXT , 
        last_name TEXT,
        address TEXT, 
        city TEXT, 
        state TEXT,
        zip TEXT, 
        phone_number TEXT
        )        
    """)
    # Insert four rows worth of data into your database
    cursor.execute("""
           INSERT INTO someTable (first_name, last_name, address, city, state, zip, phone_number) 
           VALUES ('fred', 'flintsone', '1 slate st.', 'bedrock', 'prehistoria', '11111','0')
           """)
    cursor.execute("""
               INSERT INTO someTable (first_name, last_name, address, city, state, zip, phone_number) 
               VALUES ('fred', 'flintsone', '1 slate st.', 'bedrock', 'prehistoria','11111', '1')
               """)
    cursor.execute("""
               INSERT INTO someTable (first_name, last_name, address, city, state, zip, phone_number) 
               VALUES ('fred', 'flintsone', '1 slate st.', 'bedrock', 'prehistoria', '11111','2')
               """)
    cursor.execute("""
               INSERT INTO someTable (first_name, last_name, address, city, state, zip, phone_number) 
               VALUES ('fred', 'flintsone', '1 slate st.', 'bedrock', 'prehistoria', '11111','3')
               """)
    db.commit()
    # Retrieve and display the data from the database.
    data = cursor.execute("SELECT * FROM someTable")
    print(list(data))
    # Delete a row from the database
    cursor.execute("DELETE FROM someTable WHERE phone_number = 3")
    # Retrieve and display the data again.
    data = cursor.execute("SELECT * FROM someTable")
    print(list(data))


if __name__ == '__main__': main()