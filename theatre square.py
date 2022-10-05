import math
m, n ,i= map(int, input().split(' '))
x= math.ceil(n/i)
y=math.ceil(m/i)
result=x*y
print(result)
