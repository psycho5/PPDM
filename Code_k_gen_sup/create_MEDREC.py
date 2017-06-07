import sqlite3
conn = sqlite3.connect('test.db')
# print "Opened database successfully";

conn.execute('''CREATE TABLE MEDREC
       (SNO INT PRIMARY KEY     NOT NULL,
       ZIPCODE           CHAR(50)     NOT NULL,
       AGE               CHAR(50)     NOT NULL,
       SALARY         REAL,
       DISEASE        CHAR(50));
       ''')
#print ("Table created successfully");

conn.close()

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (1, '47677', '29', 3000, 'Gastric ulcer')");
conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (2, '47602', '22', 4000, 'Gastritis')");
conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (3, '47678', '27', 5000, 'stomach cancer' )");
conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (4, '47905', '43', 6000, 'Gastritis')");
conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (5, '47909', '52', 11000, 'Flu')");
conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (6, '47906', '47', 8000, 'Bronchitis')");
conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (7, '47605', '30', 7000, 'Bronchitis' )");
conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (8, '47673', '36', 9000, 'Pneumonia' )");
conn.execute("INSERT INTO MEDREC (SNO,ZIPCODE,AGE,SALARY,DISEASE) \
      VALUES (9, '47607', '32', 10000, 'stomach cancer')");

conn.commit()
print ("Records created successfully");
conn.close()


    

