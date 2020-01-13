#!/usr/bin/python3

import pymysql

db= pymysql.connect('localhost','manage','manage','m_public')

cursor=db.cursor()

cursor.execute("SELECT VERSION()")

data =cursor.fetchone()

print ("Database version : "+data[0])

db.close()
