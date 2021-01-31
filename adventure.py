def name():
	print("\nWhat is your name?")
	answer = input(">")
	print("\nYour name is " + answer + "? Are you sure this is your name? (y, n)")
	answer2 = input(">").lower()
	if "y" in answer2:
		print("Well then, let us continue to the game.")
	elif "n" in answer2:
		print("That's a shame. Well then, let us try again.")
		name()
	else:
		print("... I'll take that as a no.")
		name()

def gameover(deathmessage):
	print("\nWhoops! You're dead.")
	print("\n" + deathmessage)
	print("\nAh well. You can always try again tomorrow.")
	print("\nTry Again? (y, n)")
	response = input(">").lower()
	if "y" in response:
		print("\nOnce more!")
		start()
	elif "n" in response:
		print("\nWell, I guess this is goodbye for now.")
		exit()
	else:
		print("\n... I'll take that as a yes.")

def start():
	print("\nYou are standing in a dark and small room.")
	print("You can't seem to remember how you got there ... Strange.")
	print("\nBut that doesn't matter now. There is a sign on the wall. Read it? (y, n)")
	signread = input(">").lower()
	if "y" in signread:
		print("\nIt says:")
		print("\nHello! I'm sure you're wondering how you got here.\nWell, I've invited(kidnapped? Same difference.) you to my little game!\nTo the right is the adventurous route, and to the left is the puzzle route\nIf you can get through all the traps, puzzles, and creatures in this dungeon, you can leave with your life, and perhaps a secret prize! ... Or you could die. But don't worry! I'm sure you'll succeed!")
	elif "n" in signread:
		print("\nHow impolite. Not to mention, it could be important ... Ah well.")
	else:
		print("\n... I'll take that as a no.")
	print("\nYou look ahead, and you see a fork. Go left or right? (l, r)")
	forkdir = input(">").lower()
	if "l" in forkdir:
		print("\nYou go to the left.")
		creatureroom()
	elif "r" in forkdir:
		print("\nYou go to the right.")
		traproom()
	else:
		gameover("Didn't I tell you to type the right thing?")

def traproom():
	print("\nThis room is rather large. That's not it, though.")
	print("\nIt's covered all over with traps. Swinging blades, timed flamethrowers, spikes, pressure plates that probably do something bad ... Behind all that is the door out.")
	print("\n1) Well, you could sprint through it like an idiot.")
	print("\n2) You could also try to find a pattern")
	print("\nWhat shall it be? (1, 2)")
	choice = input(">").lower()
	if "1" in choice:
		print("\nWell, you got hit by a blade, burned by a flamethrower, and you stepped on spikes, but you're still alive!")
		print("\nNo, wait ...")
		gameover("You just had to step on the pressure plate, didn't you? The door locked and the ceiling slowly lowered until you were turned into a human pancake.")
	elif "2" in choice:
		print("\nIf the flamethrowers stop every 34 seconds, and the swinging blades completely clear out of your way every 18 seconds, when will they simultaneously stop?")
		time = input(">")
		if time == "306":
			print("\nYou sprint through quickly, but you're not fast enough. You could shortcut across a pressure plate ... (y, n)")
			choice2 = input(">").lower()
			if "y" in choice2:
				print("\nYou sprint across the pressure plate ...")
				gameover("You just had to step on the pressure plate, didn't you? The door locked and the ceiling slowly lowered until you were turned into a human pancake.")
			elif "n" in choice2:
				print("\nYou keep sprinting, avoiding the pressure plates. The blades and flamethrowers narrowly miss you as you get to the door.")
				print("\nYou quickly go inside.")
				puzzleroom()
			else:
				gameover("Didn't I tell you to type the right thing?")
		else:
			print("\nYour timing was terrible.")
			gameover("A blade removed part of your head.")
	else:
		gameover("Didn't I tell you to type the right thing?")

def puzzleroom():
	print("\nYou find yourself in a small room.")
	print("\nThere are 5 statues in the room. You ignore them, and go to the door.")
	print("\n... The door is locked.")
	print("\nYou go back and look at the statues. Each one has a switch, and a sign.")
	print("\nThe first says, 'I watch over the family.'")
	print("\nThe second says, 'I stay behind to make sure none are lost.'")
	print("\nThe third says, 'My daughters guard me from both sides.'")
	print("\nThe writing on the other signs is illegible from age.")
	print("\nThe first, fourth, and fifth statues seem to be female. The second and third statues seem to be male.")
	print("\nA sign next to the door says, 'First to last.'")
	print("\nIn what order should you press the switches?")
	order = input(">")
	if order == "14352":
		print("\nYou were right. The door swings open. You enter the next room.")
		treasureroom()
	elif order == "15342":
		print("\nYou were right. The door swings open. You enter the next room.")
		treasureroom()
	else:
		print("\nYou hear rumbling ...")
		gameover("The ceiling descended and crushed you into a human pancake.")

def creatureroom():
	print("\nYou find yourself in a somewhat small room.")
	print("\nNo, that's just because of all the cages. You see hundreds of creatures in cages, of every shape and size. Fish, birds, reptiles, mammals.")
	print("\nThrough the mess of cages, you see a door. Unfortunately, it seems to be blocked by a bunch of cages that have fallen over.")
	print("\nAnd just your luck, it seems these cages contain some of the most dangerous creatures. A rattlesnake, a golden poison dart frog ...")
	print("\nOh dear. That's a lot of dangerous spiders, and you happen to be allergic to spider venom.")
	print("\n1) Well, you could just try to move the cages. But you'd probably die.")
	print("\n2) Or, you could search for something to help you.")
	print("\nWhat do you choose? (1, 2)")
	choice = input(">")
	if choice == "1":
		print("\nYou try to move the cages ...")
		gameover("The spiders bit you, causing you to bend over from the pain. Your hand brushed the poison dart frog, and you had a seizure. Then you died. The rattlesnake couldn't even join in on the party.")
	elif choice == "2":
		print("\nYou found a long plastic pole.")
		print("\n1) You could use it to kill the creatures.")
		print("\n2) You could also use it to move their cages.")
		print("\nWhat do you choose? (1, 2)")
		choice2 = input(">")
		if "2" in choice:
			print("\nYou move the cages out of the way with the pole, and the door is clear.")
			print("\nYou pass through the door.")
			monsterroom()
		elif "1" in choice:
			print("\nYou kill the creatures by stabbing them with the pole. First you eliminate the frog, then squash the spiders, then ...")
			print("\nWait, where's the snake?")
			gameover("While you were busy massacring his buddies, the snake felt threatened, so it snuck out of its cage and bit you. That's what you get for violence.")
		else:
			gameover("Didn't I tell you to type the right thing?")
	else:
		gameover("Didn't I tell you to type the right thing?")

def monsterroom():
	print("\nYou find yourself in a huge room.")
	print("\nIt's not the only thing that's huge. There's a giant monster!")
	print("\nIt's a snake, but where it would have a head, it has three heads! Wolf heads! With big, sharp teeth!")
	print("\nSome distance behind the creature is a door, your ticket out of this room.")
	print("\nWell, do you attempt to kill the creature with your pole or sneak around it? Just kidding, obviously you should sneak around.")
	print("\nYou attempt to sneak around the creature, but you trip on a femur. That's when you realize ...")
	print("\nThe room is covered with the skeletons of people who were previously here, and were devoured by the monster!")
	print("\nYou spot a skeleton with a gun, and some ammo clips are spread around him.")
	print("\n1) You could continue trying to sneak around the monster, but it seems to be stirring ever since you tripped over that femur.")
	print("\n2) You could also pick up the gun and ammo and try to shoot the monster dead.")
	print("\nWhat do you do? (1, 2)")
	choice = input(">").lower()
	if choice == "2":
		print("\nYou pick up the gun and load it with ammo. You try to shoot the monster.")
		gameover("Unfortunately, you suck at shooting. You completely missed, waking up the monster. It then proceeded to devour you.")
	elif choice == "1":
		print("\nYou sneak around the monster and open the door. You go inside the room.")
		treasureroom()
	else:
		gameover("Didn't I tell you to type the right thing?")

def treasureroom():
	print("\nYou're in a truly gigantic room. It's beautiful. The walls are made of emerald, and there are treasures all around.")
	print("\nDiamonds, gold bars, emeralds, rubies, a huge golden trophy, a stuffed Huia bird. You don't know most of what's there, but it all looks awesome.")
	print("\nYou wish you could take it all ... wait, there's a box labeled 'pocket dimension storage'. Maybe you can.")
	print("\nYou stick everything in the box and happily walk off, now rich. Sure, maybe you almost died a few times, but look at what you have to show for your efforts!")
	replay()

def replay():
	print("\nCongrats, you've won! How nice.")
	print("\nWell then, do you want to play again? (y, n)")
	response = input(">").lower()
	if "y" in response:
		print("\nOnce more!")
		name()
		start()
	elif "n" in response:
		print("\nWell, goodbye for now.")
		exit()
	else:
		print("\n... I'll take that as a no.")
		exit()

def intro():
	print("\nHeya!")
	print("I see you're new, huh?")
	print("Well then, I guess I should give you an introduction.")
	print("\nThis is a text-based adventure game, although I'm sure you already know that!")
	print("\nAll you have to do is make some simple choices by typing some text!")
	print("\nIt might look something like this:")
	print("\nIt seems you've reached a fork. Go left or right? (l, r)")
	print("\nIn this case, you should type either l or r!")
	print("Easy, right? Just make sure you type the right thing! There will be consequences later.")
	print("\nHmm, it seems our time is up.")
	print("Well, that's a shame.")
	print("Ciao! See you at the end of the game!")
	start()

name()
intro()