import random
board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']  #board = [' ' for _ in range(9)]
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()
def display_guidelines():
    print("Guidelines:")
    print("Below are the slot numbers of the game board.")
    print("enter the respective slot number to lock your sign on the slot of your choice.")
    print()
    print(f" 1 | 2 | 3 ")
    print("---|---|---")
    print(f" 4 | 5 | 6 ")
    print("---|---|---")
    print(f" 7 | 8 | 9 ")
    print()

def user_turn():
    turn = int(input("play your turn"))
    if turn in range(1, 10):

        if board[turn-1] == ' ':
            board[turn-1] = user_sign
            print("your turn :")
            display_board(board)
        else:
            print("slot is already locked.")
            user_turn()

    else:
        print("please enter valid slot number.")
        user_turn()

def computer_turn(comp_sign):
    print("Computer's Turn:")

    # 1. Try to win
    for combo in winning_combinations:
        combo_values = [board[i] for i in combo]
        if combo_values.count(comp_sign) == 2 and combo_values.count(' ') == 1:
            for index in combo:
                if board[index] == ' ':
                    board[index] = comp_sign
                    display_board(board)
                    return

    # 2. Try to block the user
    for combo in winning_combinations:
        combo_values = [board[i] for i in combo]
        if combo_values.count(user_sign) == 2 and combo_values.count(' ') == 1:
            for index in combo:
                if board[index] == ' ':
                    board[index] = comp_sign
                    display_board(board)
                    return

    # 3. Take the center if available
    if board[4] == ' ':
        board[4] = comp_sign
        display_board(board)
        return

    # 4. Take any available corner
    corners = [i for i in [0, 2, 6, 8] if board[i] == ' ']
    if corners:
        chosen_corner = random.choice(corners)
        board[chosen_corner] = comp_sign
        display_board(board)
        return

    # 5. Take any available side
    sides = [i for i in [1, 3, 5, 7] if board[i] == ' ']
    if sides:
        chosen_side = random.choice(sides)
        board[chosen_side] = comp_sign
        display_board(board)
        return

def check_for_result():
    global game_over
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            winning_sign = board[combo[0]]
            if winning_sign == user_sign:
                print("You Win!")
                game_over = True
            else:
                print("Computer Win!")
                game_over = True
            break
    if ' ' not in board:
        print("Game Draw")
        game_over = True


game_over = False
play = input("do you want to play Tic-Tac-Toe? type 'y' or 'n'\n")
if play == 'y':
    display_board(board)
    user_sign = input("choose your sign! X or O\n").upper()
    if user_sign == 'X':
        computer_sign = 'O'
    else:
        computer_sign = 'X'
    display_guidelines()
    print("\n"*20)
    display_board(board)
    while not game_over:
        user_turn()
        check_for_result()
        if not game_over:
            computer_turn(computer_sign)
            check_for_result()

