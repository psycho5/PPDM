from random import randint
from preCompute import * 
import math
import time

start = time.time()


features=['Age','Workclass','Education','Occupation','Relationship','Native_country']

def sigmoid(x):
  return 1 / (1 + math.exp(-x))


parent1 = []
parent2 = []
parent3 = []
parent4 = []

randomWalk = 50
PM = 25
K = 3
MIN = 0.0000000000001

findMin()

def levyFlight(c):
	for i in range(0, 6):
		if randint(0, 100)<randomWalk:
			if c[i] == '1':
				c[i] = '0'
			else:
				c[i] = '1'
	return c

def fitnessVal1(l):
	fvv = 0
	for i in range(0,6):
		if l[i] == '1' :
			fvv = fvv + res[i]
	x = sigmoid(fvv)
	return x

def fitnessVal(l):
	fvv = 0
	for i in range(0,6):
		if l[i] == '1' :
			x1 = sigmoid(res[i])
			fvv = fvv + x1
		else:
			if randint(1,100)<50:
				fvv = fvv + sigmoid(0)
			else:
				fvv = fvv + sigmoid(-0.0001)
	x = sigmoid(fvv)
	return x


for i in range(0,6):
	x = randint(1,100)
	if x < 50:
		parent1.append('1')
	else:
		parent1.append('0')

	x = randint(1,100)
	if x < 50:
		parent2.append('1')
	else:
		parent2.append('0')

	x = randint(1,100)
	if x < 50:
		parent3.append('1')
	else:
		parent3.append('0')

	x = randint(1,100)
	if x < 50:
		parent4.append('1')
	else:
		parent4.append('0')


p1 = parent1
p2 = parent2
p3 = parent3
p4 = parent4

i = 0
fvv = 3

while i < 1000:
	i = i+1
	c1 = levyFlight(p1)
	c2 = levyFlight(p2)
	c3 = levyFlight(p3)
	c4 = levyFlight(p4)
	max_fv = 0
	max_fv = max(max_fv,fitnessVal(p1),fitnessVal(p2),fitnessVal(p3),fitnessVal(p4))
	if fitnessVal(p1) < fitnessVal(c1):
		p1 = c1
	else:
		if randint(1,100) < PM:
			p1 = c1
	if fitnessVal(p2) < fitnessVal(c2):
		p2 = c2
	else:
		if randint(1,100) < PM:
			p2 = c2
	if fitnessVal(p3) < fitnessVal(c3):
		p3 = c3
	else:
		if randint(1,100) < PM:
			p3 = c3
	if fitnessVal(p4) < fitnessVal(c4):
		p4 = c4
	else:
		if randint(1,100) < PM:
			p4 = c4
	max_fv1 = max(fitnessVal(p1),fitnessVal(p2),fitnessVal(p3),fitnessVal(p4))
	if abs(max_fv1 - max_fv) < MIN:
		break

end = time.time()

print p1
print p2
print p3
print p4
print i
print end-start
	
print "From first individual feature set selected is::"
for i in range(0,6):
	if p1[i] == '1':
		print features[i]

print "From second individual feature set selected is::"
for i in range(0,6):
	if p2[i] == '1':
		print features[i]

print "From third individual feature set selected is::"
for i in range(0,6):
	if p3[i] == '1':
		print features[i]

print "From fourth individual feature set selected is::"
for i in range(0,6):
	if p4[i] == '1':
		print features[i]
	 




				





