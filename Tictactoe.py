# Rahul's Tic Tac Toe Game
# default Tic Tac Toe board layout
def reset_board():
    return [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]

board = reset_board()
turns = 0

def display_board():
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(player):
    # All possible win conditions
    win_patterns = [
        # rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # cols
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for pattern in win_patterns:
        if all(board[r][c] == player for r, c in pattern):
            return True
    return False

def update_board(choice, player):
    choice_map = {
        7: (0, 0), 8: (0, 1), 9: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        1: (2, 0), 2: (2, 1), 3: (2, 2)
    }

    if choice not in choice_map:
        print("Invalid move. Choose a number between 1 and 9.")
        return False

    row, col = choice_map[choice]

    if board[row][col] in ['X', 'O']:
        print("That spot is already taken. Try again.")
        return False

    board[row][col] = player
    return True

def is_tie():
    return all(cell in ['X', 'O'] for row in board for cell in row)

def run_game():
    global board, turns
    board = reset_board()
    turns = 0

    print("Welcome to Tic Tac Toe!")
    print("Input a number 1–9 corresponding to the board below:")
    display_board()

    game_over = False
    while not game_over:
        current_player = 'X' if turns % 2 == 0 else 'O'
        print(f"Player {1 if current_player == 'X' else 2}'s turn ({current_player})")

        try:
            choice = int(input("Enter your move (1–9): "))
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        success = update_board(choice, current_player)
        if not success:
            continue

        display_board()
        turns += 1

        if check_winner(current_player):
            print(f"Player {1 if current_player == 'X' else 2} ({current_player}) wins!")
            game_over = True
        elif is_tie():
            print("It's a tie!")
            game_over = True

    play_again = input("Play again? (Y/N): ").strip().upper()
    if play_again == 'Y':
        run_game()
    else:
        print("Thanks for playing!")

# Start the game
run_game()
