from sys import exit

yes =   ['yes', 'yea', 'ya', 'sure', 'okay', 'ok', 'yup', 'yeah', 'y']
no = ['no', 'nah', 'na', 'n']
up = ["up", "climb"]
help = ["help", "clue", "hint"]
escape = ["back", "run", "leave", "escape"]
attack = ["attack", "hit", "punch", "kick", "destroy", "fight", "fuck", "chop"]

hp = 50




def lifebar():
	if hp < 1:
		print "\n0 hit points remaining."
		print "\n\tThe Voice: Noooooooooooooo!"
		#hero_upper = hero.upper()
		print "\n%s is dead. %s IS DEAD!" % (hero, hero.upper())
		print "\n\n\n                          GAME OVER\n\n\n"
		exit(0)

def monster_fight(monster, monster_hp):
		
		while monster_hp > 1:
			print "A %s jumps at you" % monster
			print "The %s has %d hit points remaining." % (monster, monster_hp)
			global hp
			hp = (hp - 5)
			lifebar()
			print "\nIt bites you and deals 5 damage."
			print "%d hit points remaining" % (hp)
			monster_move = raw_input("\n\n\t> ").lower()
			for i in attack:
				if i in monster_move:
					print"You %s the monster." % i
					monster_hp - 5
					return monster_hp
					print monster_hp
					monster_fight(monster, monster_hp)
				else:
					print "Do something!"
					monster_fight(monster, monster_hp)

def treasure_1_option():
	treasure_1_move = raw_input("\n\tWhat now?\n\n\t > ").lower()
	if "open" in treasure_1_move:
		print "You open the chest and..."
		monster_fight("One-Eyed Monster", 15)
	elif i in escape:
		if i in treasure_1_move:
			print "You run away!"
			left_fork()
		else:
			DIE
	else:
		print "You can't do that!"
		treasure_1_option()

def treasure_1():
	print "\nYou walk down the dark corridor and come to a dead end."
	print "There is a treasure chest here!"
	treasure_1_option()

def left_fork():
	print "You come to another fork with a path to the left and right."
	left_fork_move = raw_input("\n\tWhich way? > ").lower()
	if "left" in left_fork_move:
		print "\nYou venture through a hole in cave wall to your left."
		print "The ground beneath you SHAKES!"
		print "\n\n\t%s: OH SHIT!" % hero
		print "\n\n\nYou're f\n        a\n        l\n         l\n          i\n        n\n       n\n      n\n       n\n       n\n      n\n    n\n       n\n           n\n     g\n        g\n         !\n      !\n       !\n      !\n       !\n"
		the_pit()
	elif "right" in left_fork_move:
		treasure_1()
	elif "back" in left_fork_move:
		print "You turn around and walk.\n\n\n\n\n\n"
		main_fork_alt()
	else:
		print "Try again."
		left_fork()

def the_pit():
	print "You crash to the ground and knock yourself unconscious."
	global hp
	hp = (hp - 5)
	lifebar()
	print "You lose 5 hit points, %d hit points remaining." % hp
	print "\n\tThe Voice: You're okay wake up!"
	print "You can't see anything."
	print "A small amount of light leaks in from the darkness above and you see the ladder."
	the_pit_option()

def the_pit_option():
	the_pit_move = raw_input("Which way? > ").lower()
	if the_pit_move in up:
		print "You use the ladder to climb through the darkness."
		main_fork_alt()
	else:
		print "You can't go there!"
		the_pit_option()

def main_fork():
	print "\n\n\nThe cave is very dark but you notice paths to your left, right, and straight ahead."
	print "There is also a hole in the ground which appears have a wooden ladder in it."
	main_fork_option()

def main_fork_alt():
	print "You're back where you started."
	main_fork_option()

def main_fork_option():
	main_fork_move = raw_input("\n\t Which way? > ").lower()
	help
	for i in help:
		if i in main_fork_move:
			print "\nYou can go left, right, straight, or down. Careful if you go down, the ladder looks light enough that you could pick it up."
			main_fork_option()
		elif "left" in main_fork_move:
			print "\n%s avoids the hole in the ground and ventures down the path on the left side of the cave." % hero
			left_fork()
		elif "right" in main_fork_move:
			print "\n%s avoids the hole in the ground, and ventures down the path on the right side of the cave." % hero
		elif "straight" in main_fork_move:
			print "\n%s avoids the hole in the ground, and ventures down the path in the middle of the cave." % hero
		else:
			print "\n\t Think again."
			main_fork_option()

#PART 1
print "\n\n\n\n\n\n\n\n\n\n\n\n"
print "---------------------THE GREAT CAVE ESCAPE---------------------"
print "\n\n\n\n\n\n\n\n\n\n\n\n"
print "\n\n\nThe hero is lying alone in a dark cave. Water drips on his\nhead from the darkness above."
print "\nA distant voice echos through the cave."
print "\n\tThe Voice: Wake Up."
print "\tThe Voice: WAKE UP!"
print "\tThe Voice: Please! You're my only hope!"
answer = raw_input ("\tThe Voice: Will you help me?!?! \n\n\t> ").lower()
for i in yes:
	if i in answer:
		hero = raw_input ("\n\tThe Voice: What's your name? \n\n\t> ")
		print "\nThe Voice: You must find me, %s." % hero
		print "The Voice: I can help you out of this cave, but I am trapped."
		print "The Voice: You MUST find me, but be careful."
		print "The voice: Oh no! He's coming back!"
		main_fork()
else:
	print "\nThe Voice: Well fuck you. WE'LL DIE HERE!."
	print "\n\n\n                          GAME OVER\n\n\n"
	exit(0)


