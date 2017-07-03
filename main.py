import filehandler

print('\n{0:=^120}\n'.format(' RPG The Game '))

# run the file handler script
player = filehandler.game_load()

# for testing purposes, remove this line when done.
print(player.__dict__)  # for testing purposes
