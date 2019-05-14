"""x = input("ingresa un 1: ")
y = 3
while x <= y:
	print(x)
	x += 1
"""
"""
x = 0
y = 3
while x <= y:
	print(x)
	x +=  1
	if  x == 2:
		break
	else:
		print("x es igual a 2")"""

for i in range(1, 10):
	if i % 2 != 0:
		continue
	print(i)