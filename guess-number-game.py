import random

def guess_game():
	random_number=random.randint(0,10)
	chance=3

	print('#######_______guessing Random Number Game_______#########')
	print('\n')
	print('____________start game!__________')
	print('\n')

	while(chance>0):
		print('you have total 3 chance ')
		num=input("enter the your guess number ")
		print('\n')

		if num==random_number:
			print('your guess number and random number is same that is '+str(num))
			print("yes you guess the number ")
			print("________great job________")
			print('\n')
			print('\n')

		elif random_number+1==num or random_number-1==num:
			print('your guess is very near! ')
			print('it is '+str(random_number))
			print('your number is '+str(num))
			chance=chance-1
			print('left chance= '+str(chance))
			print('\n')
			print('\n')


		else:
			print("you guess wrong try again!")
			print('random number is '+str(random_number))
			chance=chance-1
			print('left chance= '+str(chance))
			print('\n')
			print('\n')

	print('------------game over!--------------')
	print('\n')	
i=1
while(i):
	guess_game()
	print("\nyou want to play again\n")
	print("press 1 or not press 0\n")
	i=int(input())

