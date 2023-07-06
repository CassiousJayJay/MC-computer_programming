import mysql.connector

database_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "",
    database="contacts"
)

def create_contact(name, email, phone):
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
    rows = cursor.fetchall()
    cursor.close()
    return rows

#update the contacts
def update_contacts(contact_id, name, email, phone):
    cursor = database_connection.cursor()
    query = "UPDATE contacts SET name=%s, email=%s, phone=%s WHERE id=%s"
    values = (name, email, phone, contact_id)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

# update_contacts(1, "James", "james@yahoo.com", "+260967672737")

def delete_contacts(contact_id):
    cursor = database_connection.cursor()
    query = "DELETE FROM contacts WHERE id=%s"
    values =(contact_id,)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

delete_contacts(1)
contacts = get_all_contacts()
for contact in contacts:
    print(contact)

# def get_single_user(contact_id):
#     cursor = database_connection.cursor()
#     query = "SELECT * FROM contacts WHERE id=%s"
#     values = (contact_id)
#     cursor.execute(query, values)
#     rows = cursor.fetchone()
#     cursor.close()
#     return rows

# contact = get_single_user()
# print(contact)