import csv, sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

conn.execute('''CREATE TABLE ADULT
       (age INT ,
       workclass CHAR(50)     NOT NULL,
       fnwgt INT    NOT NULL,
      education CHAR(50),
       edu_num INT,
		marital_status CHAR(50),
		occupation CHAR(50),
		relationship CHAR(50),
		race CHAR(50),
		sex CHAR(50),
		capital_gain INT,
		capital_loss INT,
		hpw INT,
		native_country CHAR(50),
		salary CHAR(50));
       ''')


conn.commit()
