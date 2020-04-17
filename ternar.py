print("y = f(x):\n\t| y = x - 0.5, если x > 0\n\t| \
y = 0, если x = 0\n\t| y = |x|, если x < 0")

x = float(input("x = "))

""" if x > 0:
	y = x - 0.5
elif x == 0:
	y = 0
else:
	y = abs(x) """

y= (x - 0.5) if x > 0 else (0 if x == 0 else abs(x))
y1= x > 0 and (x - 0.5) or ( x == 0 and 0 or abs(x))

print('y = %.2f' % y)
print('y1 = %.2f' % y1)