import psycopg2
import csv

conn= psycopg2.connect(host="localhost", dbname="suppliers" , user="postgres" ,password="12345678" , port=5433)

cur= conn.cursor()

#do smt
#cur.execute("DROP TABLE IF EXISTS phonebook;")# удалить старую, чтобы не мешала

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook(
            id SERIAL PRIMARY KEY,
            surname VARCHAR(255),
            first_name VARCHAR(255),
            phone BIGINT
);
""")
conn.commit()
def insert_fr_input():
    surname=input("please enter surname: ")
    first_name= input("please enter name: ")
    phone= input("please enter number: ")

    cur.execute("""
        INSERT INTO phonebook(surname,first_name, phone)
        VALUES (%s, %s, %s)
""" ,(surname, first_name, phone))
    conn.commit()

def insert_fr_csv(path):
    with open(path,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            cur.execute("""
                INSERT INTO phonebook(surname, first_name,phone )
                VALUES (%s,%s,%s)
""", (row['surname'], row['first_name'], row['phone']))
    conn.commit()

#choice =input("1-manual insert, 2-csv: , 3-update data: ")

def update_user():
    name=input("input name where number have need to change: ")
    new_phone=input("new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name,))
    conn.commit()
    print("number updated")


def query_data():
    print("1 - show all")
    print("2 - search by surname")
    print("3 - search by first name")
    print("4 - search by first letter of surname")
    choice = input("Enter choice: ")
    
    if choice =="1":
        cur.execute("SELECT * FROM phonebook")
    elif choice=="2":
        surname = input("Enter surname: ")
        cur.execute("SELECT * FROM phonebook WHERE surname = %s", (surname,))
    elif choice=="3":
        first_name = input("Enter first name: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (first_name,))
    elif choice=="4":
        letter=input("please enter starting leter of surname: ")
        cur.execute("SELECT * FROM phonebook WHERE surname ILIKE %s", (letter+'%',))

    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user():
    print("delete: 1-first_name, 2-phone: ")
    choice=input("choose: ")

    if choice =="1":
        firstt_name=input("write name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name=%s",(firstt_name,))
        conn.commit()
        print("delete")
    elif choice=="2":
        phonee=input("write number: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s",(phonee,))
        conn.commit()
        print("delete")

choice =input("1-manual insert, 2-csv: , 3-update data: , 4- query data, 5-delete phone or name: ")
if choice == "1":
    insert_fr_input()
elif choice == "2":
    insert_fr_csv("lab10/contacts.csv")
elif choice == "3":
    update_user()
elif choice=="4":
    query_data()
elif choice=="5":
    delete_user()
    
cur.close()
conn.close()