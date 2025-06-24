import math           # use math.inf (infinity) to initialize the best score in the Minimax algorithm.

def print_board(board):  # for print the board
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Rows, Columns, and Diagonals
    lines = board + [list(col) for col in zip(*board)] + [   # to find the column
        [board[i][i] for i in range(3)],     # for left-right diagonal
        [board[i][2 - i] for i in range(3)]  # for right-left diagonal
    ]
    for line in lines:
        if line.count('X') == 3:     # if all the line contains x
            return 'X'
        elif line.count('O') == 3:
            return 'O'
    return None                        

def is_full(board):     # to check if all the cells are full or not if not then fill them
    return all(cell != ' ' for row in board for cell in row)   # if it is and no one win then declare draw  # not_empty=true

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)   
                    board[i][j] = ' '         #backtracking
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)          # default
    for i in range(3):       # for row
        for j in range(3):   # for column
            if board[i][j] == ' ':    # empty
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter your move row (0-2): "))
                col = int(input("Enter your move column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("That spot is taken. Try again.")
            except (IndexError, ValueError):
                print("Invalid input. Try again.")

        print_board(board)

        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        row, col = best_move(board)
        board[row][col] = 'O'
        print_board(board)

        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()