def is_winner(stones, is_ai):
    return stones == 0 and not is_ai   # means human wins & return true

def minimax(stones, is_ai):
    if is_winner(stones, is_ai):
        return 1 if is_ai else -1

    if is_ai:
        best_score = -float('inf')        # to find highest number it takes lower number
        for move in range(1, 4):
            if stones >= move:
                score = minimax(stones - move, False)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')            # to find lowest number it takes bigger number
        for move in range(1, 4):
            if stones >= move:
                score = minimax(stones - move, True)
                best_score = min(best_score, score)
        return best_score

def ai_move(stones):
    best_score = -float('inf')
    best_move = 1
    for move in range(1, 4):
        if stones >= move:
            score = minimax(stones - move, False)
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def play_nim():
    stones = 10
    print(" Welcome to the Nim Game!")
    print("There are", stones, "stones in the pile.")
    print("Whoever picks the last stone wins.")

    is_human_turn = True             # who will take 1st move...if true=Human / false=AI

    while stones > 0:
        print("\nStones left:", stones)
        if is_human_turn:
            while True:            # to check if its human turn or not if its then take input
                try:
                    move = int(input("Your turn (Pick 1-3 stones): "))
                    if 1 <= move <= 3 and move <= stones:
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            move = ai_move(stones)
            print(" AI picks", move, "stones.")

        stones -= move
        is_human_turn = not is_human_turn

    if is_human_turn:
        print(" AI wins! Better luck next time.")
    else:
        print(" You win! Great job.")

if __name__ == "__main__":
    play_nim()