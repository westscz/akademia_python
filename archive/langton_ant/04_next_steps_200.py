from pprint import pprint


def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]


size = 11
board = create_board(size)
x, y = size // 2, size // 2

coord_moves = {
    "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
    "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
}

coordinates = (0, -1)
for _ in range(199):
    field = board[y][x]
    direction = "L" if field else "R"
    coordinates = coord_moves[direction][coordinates]
    board[y][x] = 0 if field else 1
    y, x = y + coordinates[0], x + coordinates[1]

pprint(board)

for row in board:
    for field in row:
        print(f"[{'█' if field else ' '}]", end="")
    print()
