# Python 3 программа для
# вычислить сумму цифр в
# число.


# Функция для получения суммы цифр

def getSum(n):


	sum = 0

	while n:
			sum = sum + int(n % 10)
			n = int(n/10)



	return sum < 10 and sum or getSum(sum)



print(getSum(9998))