import mysql.connector
connection = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = connection.cursor()

cur.execute('use fsds_db')

cur.execute('select * from fsds_db.fsds1')

for i in cur :
    print(i) 