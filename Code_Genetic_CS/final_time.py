from cuckoo_time import *
from GA_time import *
from random import randint
import matplotlib.pyplot as plt

itr = []

for i in range(0,50):
	x = randint(0,10)
	print i
	itr.append(i)
	calTime(x)
	gaTime(x)

print gItr
print gTime
print cTime
'''
plt.plot(itr,cItr,'--')
plt.plot(itr, gItr, 'b')
plt.axis([0,50,0,20])
'''

plt.plot(gItr, gTime, 'ro')
plt.axis([1,20,0,0.5])

plt.show()
