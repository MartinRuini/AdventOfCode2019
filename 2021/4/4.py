import numpy as np
from pdb import set_trace

def main():
    inFile = 'input.txt'
    boards = {}
    with open(inFile) as f:
        nBoard = -1
        for nLine,line in enumerate(f.readlines()):
            line = line.strip()
            if nLine==0:
                numbers = [int(n) for n in line.split(',')]
            elif len(line)==0:
                nBoard += 1
                boards[nBoard] = []
            else:
                boards[nBoard].append([int(n) for n in line.split(' ') if len(n)>0])
    for b in boards:
        boards[b] = np.array(boards[b])
    winningBoards = np.zeros_like(list(boards.keys()), dtype=bool)

    boardMasks = { b : np.zeros_like(board, dtype=bool) for b, board in boards.items() }
    winnerBoard = None
    foundFirstWinner, foundLastWinner = False, False
    for n in numbers:
        if foundFirstWinner and foundLastWinner: break
        for b,board in boards.items():
            boardMasks[b] |= (board==n)
            for row in boardMasks[b]:
                if row.all():
                    if winnerBoard is None:
                        winnerBoard = b
                    winningBoards[b] = 1
                    break
            for col in boardMasks[b].T:
                if col.all():
                    if winnerBoard is None:
                        winnerBoard = b
                    winningBoards[b] = 1
                    break
            #if winnerBoard is not None:
            if (not foundFirstWinner and np.sum(winningBoards)==1) or (not foundLastWinner and np.sum(winningBoards)==len(winningBoards)):
                sumUnmarked = np.sum( board[np.invert(boardMasks[b])] )
                if np.sum(winningBoards)==1:
                    print(f'first winning score = {sumUnmarked*n}')
                    foundFirstWinner = True
                else:
                    print(f'last winning score = {sumUnmarked*n}')
                    foundLastWinner = True


if __name__=='__main__':
    main()
