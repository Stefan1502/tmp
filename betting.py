import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="root")

cursor = conn.cursor()

query = """ INSERT INTO tab (tab1, tab2) VALUES (%s,%s)"""
value = ("yes", 5)
cursor.execute(query, value)
conn.commit()

