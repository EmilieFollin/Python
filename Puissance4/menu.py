menulist= '''Mode de jeux,
    1. Player VS Player,
    2. Player VS IA''' 

print menulist

def choose_game_mod():
    game_mode = input('Which game mode ?\n')
    if game_mode == 1 :
        print "Player VS Player"
    elif game_mode == 2 :
        print "Player VS IA"
    else: 
        print "unknown"
    return game_mode


def choose_game_level():
    game_level = input('which level ? \n 1 : Easy \n 2 : Medium \n 3 : Hard \n')
    if game_level == 1 : 
        print "Easy level"
    elif game_level == 2:
        print "medium"
    elif game_level == 3:
        print "Hard"
    else:
        print "unknown"
    return game_level


user_choices = {}
user_choices['game_mod'] = choose_game_mod()

if user_choices['game_mod'] == 1:
    user_choices['game_level'] = choose_game_level()


print user_choices    