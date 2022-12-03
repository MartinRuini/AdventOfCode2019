INPUT = 'input.txt'
DRAW = 3
LOSE = 0
WIN  = 6

points_for_playing = {
        'X' : 1, #rock
        'Y' : 2, #paper
        'Z' : 3, #scissors
        'A' : 1, #rock
        'B' : 2, #paper
        'C' : 3, #scissors
        }

opponent = {
        'X' : {
            'A' : DRAW, #rock
            'B' : LOSE, #paper
            'C' : WIN,  #scissors
            },
        'Y' : {
            'A' : WIN,
            'B' : DRAW,
            'C' : LOSE,
            },
        'Z' : {
            'A' : LOSE,
            'B' : WIN,
            'C' : DRAW,
            }
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

move_cycle = ('A', 'B', 'C')

if __name__=='__main__':
    my_score_part1 = 0
    my_score_part2 = 0
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            opp_move, my_move = line.strip().split(' ')
            my_score_part1 += points_for_playing[my_move] + opponent[my_move][opp_move]
            my_move_idx = (move_cycle.index(opp_move)+my_move_part2[my_move])%len(move_cycle)
            my_score_part2 += points_for_playing[move_cycle[my_move_idx]] + points_part2[my_move]
    print(f'{my_score_part1 = }, {my_score_part2 = }')
