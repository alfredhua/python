import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="manage",
  passwd="manage",
  database="m_public"
)

mycursor = mydb.cursor()

mycursor.execute("insert into m_public.test(id,comment,del) values('aaaa','kkkkkkkkkkkkkk',0)")

mydb.commit()

mycursor.execute("SHOW DATABASES")
 
for x in mycursor:
  print(x)

# mycursor.execute("select * from m_public.test")
