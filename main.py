import numpy as np


def add_block(board, is_start=False):
    if is_start:
        rand = np.random.choice([2, 4], 1, p=[0.9, 0.1])
        board[np.random.randint(0, 4)][np.random.randint(0, 4)] = rand
        board = add_block(board)
    else:
        rand = np.random.choice([2, 4], 1, p=[0.9, 0.1])
        done = False
        while not done:
            x = np.random.randint(0, 4)
            y = np.random.randint(0, 4)
            if board[x][y] == 0:
                board[x][y] = rand
                done = True
    return board


def check_full(board):
    for x in range(0, 3):
        for y in range(0, 3):
            if board[y][x] == 0:
                return False
    return True


def check_game(board):
    if not check_full(board):
        return False
    board_copy = board[:]
    board_copy, empty = move_up(board_copy)
    if not check_full(board_copy):
        return False
    board_copy = board[:]
    board_copy, empty = move_down(board_copy)
    if not check_full(board_copy):
        return False
    board_copy = board[:]
    board_copy, empty = move_right(board_copy)
    if not check_full(board_copy):
        return False
    board_copy = board[:]
    board_copy, empty = move_left(board_copy)
    if not check_full(board_copy):
        return False
    return True


def move_up(board, score=0):
    for y in range(1, 4):
        for x in range(0, 4):
            if board[y - 1][x] == 0:
                y2 = y
                while y2 != 0:
                    if board[y2 - 1][x] == 0:
                        board[y2 - 1][x] = board[y2][x]
                        board[y2][x] = 0
                    elif board[y2][x] == board[y2 - 1][x]:
                        board[y2 - 1][x] += board[y2][x]
                        board[y2][x] = 0
                        score += board[y2 - 1][x]
                    else:
                        break
                    y2 -= 1
            elif board[y][x] == board[y - 1][x]:
                board[y - 1][x] += board[y][x]
                board[y][x] = 0
                score += board[y - 1][x]
    return board, score


def move_down(board, score=0):
    for y in range(2, -1, -1):
        for x in range(0, 4):
            if board[y + 1][x] == 0:
                y2 = y
                while y2 != 3:
                    if board[y2 + 1][x] == 0:
                        board[y2 + 1][x] = board[y2][x]
                        board[y2][x] = 0
                    elif board[y2][x] == board[y2 + 1][x]:
                        board[y2 + 1][x] += board[y2][x]
                        board[y2][x] = 0
                        score += board[y2 + 1][x]
                    else:
                        break
                    y2 += 1
            elif board[y][x] == board[y + 1][x]:
                board[y + 1][x] += board[y][x]
                board[y][x] = 0
                score += board[y + 1][x]
    return board, score


def move_right(board, score=0):
    for x in range(2, -1, -1):
        for y in range(0, 4):
            if board[y][x + 1] == 0:
                x2 = x
                while x2 != 3:
                    if board[y][x2 + 1] == 0:
                        board[y][x2 + 1] = board[y][x2]
                        board[y][x2] = 0
                    elif board[y][x2] == board[y][x2 + 1]:
                        board[y][x2 + 1] += board[y][x2]
                        board[y][x2] = 0
                        score += board[y][x2 + 1]
                    else:
                        break
                    x2 += 1
            elif board[y][x] == board[y][x + 1]:
                board[y][x + 1] += board[y][x]
                board[y][x] = 0
                score += board[y][x + 1]
    return board, score


def move_left(board, score=0):
    for x in range(1, 4):
        for y in range(0, 4):
            if board[y][x - 1] == 0:
                x2 = x
                while x2 != 0:
                    if board[y][x2 - 1] == 0:
                        board[y][x2 - 1] = board[y][x2]
                        board[y][x2] = 0
                    elif board[y][x2] == board[y][x2 - 1]:
                        board[y][x2 - 1] += board[y][x2]
                        board[y][x2] = 0
                        score += board[y][x2 - 1]
                    else:
                        break
                    x2 -= 1
            elif board[y][x] == board[y][x - 1]:
                board[y][x - 1] += board[y][x]
                board[y][x] = 0
                score += board[y][x - 1]
    return board, score


def start(board):
    print("To play use 'w' to go up, 'a' to go left, 's' to go down, and 'd' to go right.")
    print("After choosing your direction click the 'enter' or 'return' key too update board.")
    board = add_block(board, True)
    print(board)
    done = False
    str_score = 'SCORE so far: '
    score = 0
    while not done:
        input_direction = input()
        if input_direction == 'w':
            board, add_score = move_up(board)
            board = add_block(board)
            print('UP')
            print(board)
            score += add_score
            print(str_score + str(score))
        elif input_direction == 'a':
            board, add_score = move_left(board)
            board = add_block(board)
            print('LEFT')
            print(board)
            score += add_score
            print(str_score + str(score))
        elif input_direction == 's':
            board, add_score = move_down(board)
            board = add_block(board)
            print('DOWN')
            print(board)
            score += add_score
            print(str_score + str(score))
        elif input_direction == 'd':
            board, add_score = move_right(board)
            board = add_block(board)
            print('RIGHT')
            print(board)
            score += add_score
            print(str_score + str(score))
        if check_game(board):
            done = True
            print('GAME OVER')
            print('FINAL SCORE: ' + str(score))


# chooses the best move
def cpu_find_move(board):
    best_score = -1
    move = None
    empty, score = move_up(board)
    if score > best_score:
        best_score = score
        move = 'w'
    empty, score = move_left(board)
    if score > best_score:
        best_score = score
        move = 'a'
    empty, score = move_down(board)
    if score > best_score:
        best_score = score
        move = 's'
    empty, score = move_right(board)
    if score > best_score:
        move = 'd'

    return move


def play_cpu(board):
    score = 0
    board = add_block(board, True)
    while True:
        move = cpu_find_move(board)
        if move == 'w':
            board, score = move_up(board, score)
            board = add_block(board)
        elif move == 'a':
            board, score = move_left(board, score)
            board = add_block(board)
        elif move == 's':
            board, score = move_down(board, score)
            board = add_block(board)
        elif move == 'd':
            board, score = move_right(board, score)
            board = add_block(board)
        if check_game(board):
            break
    return board, score


play_board = np.array([[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]])
# start(play_board)

print(play_cpu(play_board))
