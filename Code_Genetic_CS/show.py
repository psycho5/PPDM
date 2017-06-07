import sqlite3
c = sqlite3.connect('test.db')
cursor = c.execute("SELECT * FROM ADULT")
for row in cursor:
   print ("SNO = ",row[0] )
   print ("ZIPCODE = ", row[1])

c.close()
