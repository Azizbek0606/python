import psycopg2

# Ma'lumotlar bazasiga ulanish
conn = psycopg2.connect(
    dbname="university",
    user="postgres",
    password="Azizbek.5474",
    host="localhost",  # Yoki server manzili
    port="5432",  # PostgreSQL standart porti
)

# Cursor obyektini yaratish
cursor = conn.cursor()

# SQL so'rovni bajarish
cursor.execute("SELECT * FROM students;")

# Natijalarni olish
rows = cursor.fetchall()

def showStudent():
    arr1 = []
    arr = []
    for row in rows:
        arr.append(row[0])
        arr.append(row[1])
        arr.append(row[2])
        arr1.append(arr)
        arr = []
    return arr1


cursor.close()
conn.close()
