import sqlite3
c = sqlite3.connect('test.db')
cursor =  c.execute("SELECT *  FROM ANONY_MEDREC ORDER BY ZIPCODE, AGE")
'''for row in cursor:
   print ("ZIPCODE = ", row[1], end = ' ')
   print ("AGE = ", row[2],end = ' ')
   print ("SALARY = ", row[3],end = ' ')
   print ("DISEASE = ",row[4]), "\n"
'''
x = 0;
k = 0;
low = [-1]*20
high = [-1]*20
cursor =  c.execute("SELECT *  FROM ANONY_MEDREC ORDER BY ZIPCODE, AGE")

for row in cursor:
    if x == 0:
        low[k] = row[2];
    elif x == 1:
        low[k] = low[k-1];
        high[k-1] = row[2];
    elif x == 2:
        high[k-1] = row[2];
        low[k] = high[k-2];
        high[k] = row[2];
    
    
    x = (x+1)%3;
    k = k+1;

k = 0;

cursor =  c.execute("SELECT *  FROM ANONY_MEDREC ORDER BY ZIPCODE, AGE")

for row in cursor:
    x = row[2];
    y = low[k] + " <= " + high[k]
    c.execute("UPDATE ANONY_MEDREC SET AGE = ? WHERE AGE = ?" ,(y,x))
    k = k+1;
    
cursor =  c.execute("SELECT *  FROM ANONY_MEDREC ORDER BY ZIPCODE, AGE")
for row in cursor:
   print ("ZIPCODE = ", row[1], end = ' ')
   print ("AGE = ", row[2],end = ' ')
   print ("SALARY = ", row[3],end = ' ')
   print ("DISEASE = ",row[4]), "\n"
