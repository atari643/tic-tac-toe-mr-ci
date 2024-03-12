# Check if one turn has been made
def one_turn(game_old, game_new):
    move_count = 0
    for i in range(0, 9):
        if game_old[i] != game_new[i]:
            move_count += 1
    if move_count == 1:
        return True
    return False


# Load game from file
def load_game(name):
    game = [''] * 9
    file = open(name, "r")
    for i in range(1, 10):
        game[i-1] = file.read(1)
        if i % 3 == 0:
            file.read(1)  # end-of-line
    file.close()
    return game


game_old = load_game("game-old.txt")
game_new = load_game("game-new.txt")  # more 'X' than 'O'
assert one_turn(game_old, game_new)