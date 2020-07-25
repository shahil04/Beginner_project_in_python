import random


def game_function():

	print('Dice Roll Game!')
	dice=random.randint(1,6)

	if dice==1:
		print(dice)
		print('@-----@')
		print('|     |')
		print('|  *  |')
		print('|     |')
		print('@-----@')
	elif dice==2:
		print('@-----@')
		print('|     |')
		print('| *  *|')
		print('|     |')
		print('@-----@')
		print(dice)

	elif dice==3:
		print('@-----@')
		print('|*    |')
		print('|  *  |')
		print('|    *|')
		print('@-----@')
		print(dice)

	elif dice==4:
		print('@-----@')
		print('|*   *|')
		print('|     |')
		print('|*   *|')
		print('@-----@')
		print(dice)

	elif dice==5:
		print('@-----@')
		print('|*   *|')
		print('|  *  |')
		print('|*   *|')
		print('@-----@')
		print(dice)

	else:
		print('@-----@')
		print('|*   *|')
		print('|*   *|')
		print('|*   *|')
		print('@-----@')
		print(dice)

i=1
while (i):
	game_function()
	print("\n you want to roll again \n press 1 or exit 0\n")
	i=int(input())