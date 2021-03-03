from pprint import pprint


def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]


size = 11
board = create_board(size)
x, y = size // 2, size // 2

pprint(board)
print(x, y)
