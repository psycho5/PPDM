import sqlite3
c = sqlite3.connect('test.db')
cursor = c.execute("SELECT * FROM MEDREC")
for row in cursor:
   print ("SNO = ",row[0], end= ' ')
   print ("ZIPCODE = ", row[1], end = ' ')
   print ("AGE = ", row[2],end = ' ')
   print ("SALARY = ", row[3],end = ' ')
   print ("DISEASE = ",row[4]), "\n"
c.close()
