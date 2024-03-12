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


game_old = load_game("game-old.txt")
game_new = load_game("game-new.txt")  # more 'X' than 'O'
assert valid_game(game_old)
assert not valid_game(game_new)
assert one_turn(game_old, game_new)