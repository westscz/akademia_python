from pprint import pprint


def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]


size = 11
board = create_board(size)
x, y = size // 2, size // 2

direction = "L" if board[y][x] else "R"
print(direction)


if board[y][x]:
    direction = "L"
else:
    direction = "R"
# board[y - 1][x] = "N"
# board[y][x + 1] = "E"
# board[y + 1][x] = "S"
# board[y][x - 1] = "W"

pprint(board)
print(x, y)

coordinates = (0, -1)

coord_moves = {
    "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
    "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
}
print(coord_moves[direction][coordinates])


pprint(board)
