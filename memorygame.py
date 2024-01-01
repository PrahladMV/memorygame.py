import random
import time

def generate_board(size):
    numbers = list(range(1, size + 1)) * 2
    random.shuffle(numbers)
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return numbers, board

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

def reveal_tile(board, row, col):
    if board[row][col] == ' ':
        print("Already revealed.")
    else:
        print(f"Revealing: {board[row][col]}")
        time.sleep(1)
        print_board(board)
        return board[row][col]

def main():
    print("Welcome to the Unique Memory Game!")

    size = int(input("Enter the size of the board (even number, e.g., 4): "))
    if size % 2 != 0:
        print("Please enter an even number for the size.")
        return

    numbers, board = generate_board(size)
    attempts = size * size // 2
    matched_pairs = 0

    while matched_pairs < size * size // 2:
        print_board(board)

        try:
            print(f"Attempts left: {attempts}")
            row1 = int(input("Enter the row of the first tile: ")) - 1
            col1 = int(input("Enter the column of the first tile: ")) - 1
            value1 = reveal_tile(board, row1, col1)

            row2 = int(input("Enter the row of the second tile: ")) - 1
            col2 = int(input("Enter the column of the second tile: ")) - 1
            value2 = reveal_tile(board, row2, col2)

            if value1 == value2:
                print("Match found!")
                matched_pairs += 1
                board[row1][col1] = ' '
                board[row2][col2] = ' '
            else:
                print("No match. Try again.")
                attempts -= 1

            time.sleep(1)
            print("\n" * 50)  # Clear the console
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column values.")

    print("Congratulations! You've matched all pairs.")
    print("Designed by Prahlad MV")

if __name__ == "__main__":
    main()
