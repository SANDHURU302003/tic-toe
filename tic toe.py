import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_free_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def get_computer_move(board):
    free_cells = get_free_cells(board)
    return random.choice(free_cells)

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")

    players = ["X", "O"]
    player_names = ["Player 1", "Player 2"]

    while True:
        game_mode = input("Enter '1' for two-player mode or '2' for player vs. computer: ")

        if game_mode == '1':
            player_names[0] = input("Enter the name of Player 1: ")
            player_names[1] = input("Enter the name of Player 2: ")
            break

        elif game_mode == '2':
            player_names[0] = input("Enter your name: ")
            player_names[1] = "Computer"
            break

        else:
            print("Invalid input. Please try again.")

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = 0
        total_moves = 0

        while True:
            print_board(board)

            if game_mode == '1' or current_player == 0:
                move_row = int(input(f"{player_names[current_player]}, enter the row (0-2): "))
                move_col = int(input(f"{player_names[current_player]}, enter the column (0-2): "))
            else:
                move_row, move_col = get_computer_move(board)
                print(f"{player_names[current_player]} (Computer) chooses row {move_row}, column {move_col}.")

            if board[move_row][move_col] == " ":
                board[move_row][move_col] = players[current_player]
                total_moves += 1

                if check_winner(board, players[current_player]):
                    print_board(board)
                    print(f"Congratulations! {player_names[current_player]} wins!")
                    break
                elif total_moves == 9:
                    print_board(board)
                    print("It's a tie!")
                    break

                current_player = 1 - current_player
            else:
                print("Cell already taken. Please try again.")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Thanks for playing Tic Tac Toe!")
