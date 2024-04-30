while True:
    board_size = input("Please mark the size of the board you want to play in: ")
    if board_size.startswith('-'):
        print("Please enter a positive number!")
        continue
    if not board_size.isdigit():
        print("Please enter a number!")
        continue
    board_size = int(board_size)
    if board_size <= 0:
        print("The size of the board must be a whole positive number!")
        continue
    else:
        break

matrix = []
knights = []
# Coordinates of every knight on the board

for row in range(board_size):
    matrix.append([x for x in input()])
    for col in range(board_size):
        if matrix[row][col].upper() == "K":
            knights.append([row, col])

removed_knights = 0
possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
# All the possible moves for a knight

while True:
    max_hits = 0
    knight_with_max_hits = None
    for k_row, k_col in knights:
        current_hits = 0
        for move in possible_moves:
            new_row = k_row + move[0]
            new_col = k_col + move[1]
            if 0 <= new_row < board_size and 0 <= new_col < board_size:
                if matrix[new_row][new_col] == "K":
                    current_hits += 1
        if current_hits > max_hits:
            max_hits = current_hits
            knight_with_max_hits = [k_row, k_col]

    if max_hits == 0:
        break

    knights.remove(knight_with_max_hits)
    matrix[knight_with_max_hits[0]][knight_with_max_hits[1]] = "0"
    removed_knights += 1

print(f"The number of knights removed from the board is: {removed_knights}")
print("Updated Chess Board:")
for row in matrix:
    print("".join(row))


