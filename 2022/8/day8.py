import numpy as np

INPUT = 'input.txt'

def main():
    tree_map = np.genfromtxt(INPUT, delimiter=1, dtype=int)

    #part 1
    visible_from_right  = np.zeros_like(tree_map, dtype=bool)
    visible_from_top    = np.zeros_like(tree_map, dtype=bool)
    visible_from_left   = np.zeros_like(tree_map, dtype=bool)
    visible_from_bottom = np.zeros_like(tree_map, dtype=bool)

    visible_from_right[:,-1]  = True
    visible_from_top[0,:]     = True
    visible_from_left[:,0]    = True
    visible_from_bottom[-1,:] = True

    for irow,row in enumerate(tree_map[1:-1,1:-1], start=1):
        for icol, tree in enumerate(row, start=1):
            if all(tree_map[irow, icol+1:]<tree):
                visible_from_right[irow,icol] = True
            if all(tree_map[:irow, icol]<tree):
                visible_from_top[irow,icol] = True
            if all(tree_map[irow, :icol]<tree):
                visible_from_left[irow,icol] = True
            if all(tree_map[irow+1:, icol]<tree):
                visible_from_bottom[irow,icol] = True
    visible_trees = visible_from_right | visible_from_top | visible_from_left | visible_from_bottom
    n_visible_trees = np.sum(visible_trees)
    print(f'{n_visible_trees = }')

    #part 2
    scenic_score = np.ones_like(tree_map)

    for irow,row in enumerate(tree_map[1:-1,1:-1], start=1):
        for icol, tree in enumerate(row, start=1):
            for view_distance_right, other_tree in enumerate(tree_map[irow, icol+1:], start=1):
                if other_tree>=tree:
                    break
            for view_distance_up, other_tree in enumerate(tree_map[:irow, icol][::-1], start=1):
                if other_tree>=tree:
                    break
            for view_distance_left, other_tree in enumerate(tree_map[irow, :icol][::-1], start=1):
                if other_tree>=tree:
                    break
            for view_distance_down, other_tree in enumerate(tree_map[irow+1:, icol], start=1):
                if other_tree>=tree:
                    break
            scenic_score[irow,icol] = view_distance_right * view_distance_up * view_distance_left * view_distance_down
    print(f'{np.max(scenic_score) = }')

if __name__=='__main__':
    main()
