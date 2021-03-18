import psycopg2

con = psycopg2.connect(
    database="data_mining",
    user="postgres",
    password="80pufuda",
    host="127.0.0.1",
    port="5432"
)

data = {}
with open('data/result.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        temp_data = line.split(":")
        data[temp_data[0]] = temp_data[1]

cursor = con.cursor()
for k, v in data.items():
    cursor.execute(
        f"INSERT INTO first_home_work (word, count) VALUES ('{k}', {v})"
    )
con.commit()
con.close()