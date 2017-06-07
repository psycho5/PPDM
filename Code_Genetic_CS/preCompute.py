import sqlite3
c = sqlite3.connect('test.db')
cursor = c.execute("SELECT * FROM QTABLE")

age = []
workclass = []
education = []
occupation = []
relationship = []
country = []
salary = []
res = []

def func(ls):
	c = 1000
	k = 1
	for i in range(1, 100):
		if ls[i] == ls[i-1]:
			k = k+1;
		else:
			c = min(c, k);
			k = 1
	c = min(c, k)
	res.append(c)
	

def findMin():
	i = 0
	for row in cursor:
		age.append(row[0])
		workclass.append(row[1])
		education.append(row[2])
		occupation.append(row[3])
		relationship.append(row[4])
		country.append(row[5])
		salary.append(row[6])
		i = i+1
		if i == 100:
			break



	age.sort()
	workclass.sort()
	education.sort()
	occupation.sort()
	relationship.sort()
	country.sort()
	salary.sort()





	func(age)
	func(workclass)
	func(education)
	func(occupation)
	func(relationship)
	func(country)
	func(salary)



	

