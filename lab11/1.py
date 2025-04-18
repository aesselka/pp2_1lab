import psycopg2

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
#1
def search(surname_pattern, first_name_pattern, phone_pattern):
    surname_pattern = '%' + surname_pattern + '%'
    first_name_pattern = '%' + first_name_pattern + '%'
    phone_pattern = '%' + phone_pattern + '%'
    
    cur.execute("""SELECT * FROM phonebook 
            WHERE surname ILIKE %s AND first_name ILIKE %s AND phone::TEXT LIKE %s
        """, (surname_pattern, first_name_pattern, phone_pattern))
    
    results = cur.fetchall()
    return results
#4
def query(limit,offset):
    limit=int(limit)
    offset=int(offset)

    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit,offset))
    results=cur.fetchall()
    return results
#5
def delete_usr_pho(choice, value,phone=None):
        if choice == 1:  #phone
            cur.execute("CALL delete_user_by_criteria(%s, %s, %s)", (choice, None, phone))
        else:  #surname
            cur.execute("CALL delete_user_by_criteria(%s, %s, %s)", (choice, value, None))
        conn.commit()  
        print("Запись удалена.")

delete_usr_pho(2,'Eraliyeva')

delete_usr_pho(1,None,87759426573)
#EX for search
surname_pattern = 'Ergaliyeva'
first_name_pattern = 'Dariya'
phone_pattern = '8775'
search_results = search(surname_pattern, first_name_pattern, phone_pattern)
print("Search results:", search_results)
#ex query
limit=5
offset=0
query_results=query(limit,offset)
cur.close()
conn.close()
# CREATE OR REPLACE PROCEDURE delete_user_by_criteria(p_choice INT, p_value TEXT, p_phone BIGINT)
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     IF p_choice = 1 THEN
#         -- Удаление по телефону
#         DELETE FROM phonebook WHERE phone = p_phone;
#     ELSIF p_choice = 2 THEN
#         -- Удаление по фамилии
#         DELETE FROM phonebook WHERE surname = p_value;
#     END IF;
# END;
# $$;
