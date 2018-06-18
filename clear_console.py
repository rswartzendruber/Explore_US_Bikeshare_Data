from os import system, name

def clear(command = None):
	if command is None:
		if name == "nt":
			system("cls")
		else:
			system("clear")
	elif command == "cls" or command == "clear":
		system(command)



