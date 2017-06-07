import sqlite3
c = sqlite3.connect('test.db')
'''
c.execute("CREATE TABLE QTABLE AS SELECT age, workclass,education,occupation, relationship,native_country, salary FROM ADULT")
c.commit()
'''
cursor = c.execute("SELECT * FROM QTABLE")
i = 0
for row in cursor:
	if(i == 100):
		break
	i = i+1
   	print ("AGE = ",row[0],"WORKCLASS = ", row[1],"EDUCATION = ",row[2],"OCCUPATION = ", row[3],"RELATIONSHIP = ",row[4],"NATIVE_COUNTRY = ", row[5],"SALARY = ",row[6] )
   


c.close()
c.close()
