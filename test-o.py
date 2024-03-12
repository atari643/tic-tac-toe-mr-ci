# Check if one turn has been made
def one_turn(game_old, game_new):
    move_count = 0
    for i in range(0, 9):
        if game_old[i] != game_new[i]:
            move_count += 1
    if move_count == 1:
        return True
    return False
