import mysql.connector
import os


DATABASE_USR = os.environ.get("DATABASE_USR")

database_connection = mysql.connector.connect(
    host="localhost",
    user=DATABASE_USR,
    password= "",
    database="contacts"
)

def create_contact(name, email, phone):
    if not name or not email:
        print("Name and Email are required")
        return
    cursor = database_connection.cursor()
    query = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"
    values = (name, email, phone)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close

# create_contact("James", "james@gmail.com", "260972983537")  

#retries all contacts
def get_all_contacts():
    cursor = database_connection.cursor()
    query = "SELECT * FROM contacts"
    cursor.execute(query)
    contacts = []
    for row in cursor.fetchall():
        contact = {
            "name": row[1],
            "email": row[2],
            "phone": row[3],
        }
        contacts.append(contact)
    cursor.close()
    return contacts

#update the contacts
def update_contact(contact_id, name, email, phone):
    if not name or not email:
        print("Name and Email are required")
        return
    cursor = database_connection.cursor()
    query = "UPDATE contacts SET name=%s, email=%s, phone=%s WHERE id=%s"
    values = (name, email, phone, contact_id)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

#update_contact(2, "Cassious", "james@yahoo.com", "+260967672737")


def delete_contact(contact_id):
    cursor = database_connection.cursor()
    query = "DELETE FROM contacts WHERE id=%s"
    values =(contact_id,)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

delete_contact(1)
contacts = get_all_contacts()
for contact in contacts:
    print(contact)

def get_single_user(contact_id):
    cursor = database_connection.cursor()
    query = "SELECT * FROM contacts WHERE id=%s"
    values = (contact_id,)
    cursor.execute(query, values)
    rows = cursor.fetchone()
    cursor.close()
    return rows

contact = get_single_user(1)
print(contact)