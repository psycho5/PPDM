''' 
	S (Original dataset);
	I (Inducer);
	QI (The quasi-identifier);
	k 	(anonymity level);
	nGen (Maximum number of generations);
	nPop (Number of candidates in a population);
	Pcrossover (Probability of crossover);
	Pmutation (Probability of mutation);
	nFolds (Number of folds for wrapper procedure)
'''



import csv, sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()


#reader = csv.reader(open('tab.csv', 'r'), delimiter='.')

with open('tab.csv','rb') as fin: 
    dr = csv.DictReader(fin) 
    to_db = [(i['age'], i['workclass'], i['fnwgt'], i['education'],i['edu_num'],i['marital_status'],i['occupation'],i['relationship'],i['race'],i['sex'],i['capital_gain'],i['capital_loss'],i['hpw'],i['native_country'], i['salary']) for i in dr]

cur.executemany("INSERT INTO ADULT (age, workclass, fnwgt, education, edu_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hpw, native_country, salary) VALUES (?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)

'''

for row in reader:
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8"),unicode(row[4], "utf8"),unicode(row[5], "utf8"),unicode(row[6], "utf8"),unicode(row[7], "utf8"),unicode(row[8], "utf8"),unicode(row[9], "utf8"),unicode(row[10], "utf8"),unicode(row[11], "utf8"),unicode(row[12], "utf8"),unicode(row[13], "utf8"),unicode(row[14], "utf8"),]
    curs.execute("INSERT INTO ADULT (age, workclass, fnwgt, education, edu_num, marital_status, occupation, moving, relationship, race, sex, capital_gain, capital_loss, hpw, native_country) VALUES (?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
'''

conn.commit()


