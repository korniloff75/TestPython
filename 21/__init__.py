# koloda = range(6,11) * 10
koloda = [6,7,8,9,10,2,3,4,11] * 10

import random
random.shuffle(koloda)

print('Поиграем в очко?')
userCount = 0
bankCount = 0

while True:
	choice = input('Будете брать карту? y/n\n')
	if (choice == 'y') or (choice == 'н'):
		current = koloda.pop()
		bankStep = koloda.pop()
		print('Вам попалась карта достоинством %d' %current)
		userCount += current
		bankCount += bankStep
		print('У банкира %d очков' %bankCount)
		if bankCount > 21:
			print('Банкир проиграл, набрав %d очков' %bankCount)
			break

		if userCount > 21:
			print('Извините, но вы проиграли, набрав %d очков' %userCount)
			break
		elif userCount == 21:
			print('Поздравляю, вы набрали 21!')
			break
		else:
			print('У вас %d очков.' %userCount)
	elif choice == 'n':
		print('У вас %d очков и вы закончили игру.' %userCount)
		print('У банкира %d .' %bankCount)
		if userCount > bankCount:
			print('Вы победили.')
		else:
			print('Вы проиграли')
		break

print('До новых встреч!')
