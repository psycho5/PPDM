import sqlite3
c = sqlite3.connect('test.db')
c.execute("CREATE TABLE ANONY_MEDREC AS SELECT * FROM MEDREC ORDER BY ZIPCODE")
c.commit()
c.close()
