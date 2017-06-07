from random import randint
from preCompute import * 
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))


parent1 = []
parent2 = []
PC = 50
PM = 10
K = 3
MIN = 0.0000000000001

findMin()

def crossOver(p1, p2):
	c = []
	for i in range(0,6):
		if randint(0,100)<PC:
			c.append(p1[i])
		else:
			c.append(p2[i])
	return c
	

def mutate(c):
	for i in range(0, 6):
		if randint(0, 100)<PM:
			if c[i] == '1':
				c[i] = '0'
			else:
				c[i] = '1'
	return c

def fitnessVal(l):
	fvv = 0
	for i in range(0,6):
		if l[i] == '1' :
			fvv = fvv + res[i]
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


p1 = parent1
p2 = parent2
i = 0
fvv = 3
while i < 1000:
	i = i+1
	c1 = crossOver(p1, p2)
	c2 = crossOver(p1, p2)
	while len(set(c1).intersection(c2)) == 6:
		c2 = crossOver(p1, p2)
	c1 = mutate(c1)
	c2 = mutate(c2)
	fv = []
	fv.append((fitnessVal(p1), p1))
	fv.append((fitnessVal(p2), p2))
	fv.append((fitnessVal(c1), c1))
	fv.append((fitnessVal(c2), c2))
	fv.sort()
	p1 = fv[3][1]
	p2 = fv[2][1]
	if abs(fv[3][0] - fvv) < MIN:
		break
	fvv = fv[3][0]
		
	
print p1
print p2

	
	




				





