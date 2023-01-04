import base64
import psycopg2

conn = psycopg2.connect(database="hbs",
                        host="hbs-postgresql",
                        user="hbs",
                        password="changeme",
                        port="5432")

cursor = conn.cursor()


cursor.execute("SELECT sync_id,image FROM tbl_receipt_image")
c = cursor.fetchall()
for row in c:
    f = open("output/"+str(row[0])+".jpg", "wb")
    photo = str(bytes(row[1]))
    cleaned = photo.lstrip("b'").rstrip("'")
    f.write(base64.b64decode(cleaned))
    f.close()
