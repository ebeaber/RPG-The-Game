import filehandler

print('\n{0:=^120}\n'.format(' RPG The Game '))

# run the file handler script
player = filehandler.game_load()

print(player.__dict__)
