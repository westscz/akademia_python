import tkinter

coord_moves = {
    "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
    "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
}


def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]


size = 100
board = create_board(size)
x, y = size // 2, size // 2
coordinates = (0, -1)

for _ in range(11000):
    field = board[y][x]
    direction = "L" if field else "R"
    board[y][x] = 0 if field else 1

    coordinates = coord_moves[direction][coordinates]
    y, x = y + coordinates[0], x + coordinates[1]

root = tkinter.Tk()
window_size = 400
canvas = tkinter.Canvas(root, width=window_size, height=window_size)
canvas.pack()

s = window_size / size
for y, row in enumerate(board):
    for x, field in enumerate(row):
        color = "white" if field == 0 else "black"
        canvas.create_rectangle(
            s * x, s * y, s + (s * x), s + (s * y), fill=color, outline=color
        )
root.mainloop()
