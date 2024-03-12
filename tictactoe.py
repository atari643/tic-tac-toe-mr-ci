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
print(game_old)
print("it does work")
game_new = load_game("game-new.txt")  # more 'X' than 'O'
print(game_new)


# Check if the game is valid
def valid_game(game):
    # 1. check if the game is a list of 9 characters
    if not isinstance(game, list):
        return False
    if len(game) != 9:
        return False
    # 2. check if the game contains only 'X', 'O' or '.'
    for i in range(0, 9):
        if game[i] != 'X' and game[i] != 'O' and game[i] != '.':
            return False
    # 3. check if #('O') == #('X') or #('O') == #('X') + 1
    x_count = 0
    o_count = 0
    for i in range(0, 9):
        if game[i] == 'X':
            x_count += 1
        elif game[i] == 'O':
            o_count += 1
    if o_count != x_count and o_count != x_count + 1:
        return False
    return True


# Check if one turn has been made
def one_turn(game_old, game_new):
    move_count = 0
    for i in range(0, 9):
        if game_old[i] != game_new[i]:
            move_count += 1
    if move_count == 1:
        return True
    return False


assert valid_game(game_old)
assert not valid_game(game_new)
assert one_turn(game_old, game_new)


# Check game (return 'X' or 'O' or '.')
def check_game(game):
    # check rows
    for i in range(0, 9, 3):
        if game[i] == game[i+1] == game[i+2] and game[i] != '.':
            return game[i]
    # check columns
    for i in range(0, 3):
        if game[i] == game[i+3] == game[i+6] and game[i] != '.':
            return game[i]
    # check diagonals
    if game[0] == game[4] == game[8] and game[0] != '.':
        return game[0]
    if game[2] == game[4] == game[6] and game[2] != '.':
        return game[2]
    return '.'


print(check_game(game_old))
print(check_game(game_new))
