INPUT = 'input.txt'
DRAW = 3
LOSE = 0
WIN  = 6

points_for_playing = {
        'A' : 1, #rock
        'B' : 2, #paper
        'C' : 3, #scissors
        }

move_cycle = ('A', 'B', 'C') # move at index i loses against i+1

part1 = {
        'X' : 'A', #rock
        'Y' : 'B', #paper
        'Z' : 'C', #scissors
        }

points_part2 = {
        'X' : LOSE,
        'Y' : DRAW,
        'Z' : WIN,
        }

my_move_part2 = {
        'X' : -1,
        'Y' : 0,
        'Z' : +1,
        }

if __name__=='__main__':
    my_score_part1 = 0
    my_score_part2 = 0
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            opp_move, instruction = line.strip().split(' ')

            #part 1
            my_move = part1[instruction]
            opp_move_idx = move_cycle.index(opp_move)
            my_move_idx  = move_cycle.index(my_move)
            if opp_move_idx==(my_move_idx+1)%len(move_cycle):
                outcome = LOSE
            elif opp_move_idx==my_move_idx:
                outcome = DRAW
            else:
                outcome = WIN
            my_score_part1 += points_for_playing[my_move] + outcome

            #part 2
            my_move_idx = (move_cycle.index(opp_move)+my_move_part2[instruction])%len(move_cycle)
            my_move     = move_cycle[my_move_idx]
            my_score_part2 += points_for_playing[my_move] + points_part2[instruction]

    print(f'{my_score_part1 = }, {my_score_part2 = }')
