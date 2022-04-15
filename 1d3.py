#!/usr/bin/python3

from random import shuffle
from time import sleep

dieSides = ['A', 'B', 'C']
dieOrientation = ['A', 'B', 'C']
rollsDone = 0
countRolls = {
	'A': 0,
	'B': 0,
	'C': 0
}
winner = {}
the_winner={}


def println(text):
	print('{}'.format(text), end='')

def prompt_for_choices():
	dieChoices = {}
	print("Designate 3 choices to roll for: ")
	for each in dieOrientation:
		choice = ""
		while (choice == ""):
			print('Specify choice {0}: '.format(each), end='')
			choice = input()
		dieChoices[each] = choice
	return dieChoices

def shuffle_list(aList):
	return shuffle(aList)

def roll_die(aList, times=1):
	done=0
	global rollsDone
	global the_winner
	while (done < times):
		rollsDone += 1
		done+=1
		shuffle_list(aList)
		draw_die(aList)
		countRolls[aList[0]] +=1

def draw_die(sides):
	print('     ^')
	print('    / \\')
	print('   / {0} \\'.format(sides[0]))
	print('  /     \\')
	print(' / {0}   {1} \\'.format(sides[2],sides[1]))
	print('/_________\\')

def find_winner():
	winners = {}
	for c in countRolls:
		if len(winners) == 0:
			winners[c] = countRolls[c]
		else:
			for w in list(winners.keys()):
				if countRolls[c] > winners[w]:
					del winners[w]
					winners[c] = countRolls[c]
				else:
					if countRolls[c] == winners[w]:
						winners[c] = countRolls[c]
	return winners

def list_choices():
	for each in dieChoices:
		print('    {} :: {}'.format(each,dieChoices[each]))

def prompt_times_to_roll():
	print("Let's roll less than 10 times so we're not here all day")
	rollsToDo=""
	while not rollsToDo.isnumeric():
		rollsToDo=input("How many times should I roll? ")
	print('')
	print("Great, I'll roll {} times".format(rollsToDo))
	print('')
	return int(rollsToDo)

def print_stats():
	print('Results of {} rolls:'.format(rollsDone))
	for each in dieSides:
		print('    Rolled {0} {1:>5} times ({2})'.\
			format(each,countRolls[each],dieChoices[each]))


print("Let the Fates decide for you")
dieChoices=prompt_for_choices()
rollsToDo=prompt_times_to_roll()
print('Consulting the great Oracle \"1d3\" ', end='')
if rollsToDo != 1:
	print('(really, \"{}d3\") '.format(rollsToDo), end='')
print('to choose between:')
list_choices()

print('Rolling...')
print('')

roll_die(dieOrientation, rollsToDo)
the_winner=find_winner()
while (len(the_winner) > 1):
	print_stats()
	print('There are {} winners: {}'.format(len(the_winner),the_winner))
	print('Continuing to roll to break the tie')
	roll_die(dieOrientation)
	the_winner=find_winner()
print('')

print_stats()
print('')
print('Your choice is made; the winner is {}: {}'.format(list(the_winner.keys())[0],dieChoices[list(the_winner.keys())[0]]))


