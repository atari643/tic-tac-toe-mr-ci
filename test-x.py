# Check if the game is valid
def valid_game(game):
    print("well it runs")
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
game_now=load_game("game.txt")
assert valid_game(game_old)
assert not valid_game(game_new)
assert valid_game(game_now)
