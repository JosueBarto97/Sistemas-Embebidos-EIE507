import decimal
from decimal import *

getcontext().prec = 500

sum=0

for i in range(0,1000000):
	sum += 4*(Decimal((-1)**i)/Decimal(2*i+1))
	b = Decimal(sum)
print (b)

