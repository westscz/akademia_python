import tkinter

coord_moves = {
    "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
    "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
}


def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def rgb_int_to_hex(number):
    return "#{n:02x}{n:02x}{n:02x}".format(n=number)


size = 100
board = create_board(size)
x, y = size // 2, size // 2
coordinates = (0, -1)

pattern = "RLR"

color_step = int(255 / (len(pattern) - 1))
colors = [rgb_int_to_hex(color_step * i) for i in range(len(pattern))][::-1]
print(colors)

root = tkinter.Tk()
window_size = 400
canvas = tkinter.Canvas(root, width=window_size, height=window_size)
canvas.pack()


def redraw(window_size, size, canvas, colors, board):
    s = window_size / size
    for y, row in enumerate(board):
        for x, field in enumerate(row):
            color = colors[field]
            canvas.create_rectangle(
                s * x, s * y, s + (s * x), s + (s * y), fill=color, outline=color
            )
    canvas.update()


for _ in range(11000):
    field = board[y][x]
    direction = pattern[field]
    board[y][x] = (field + 1) % len(pattern)

    coordinates = coord_moves[direction][coordinates]
    y, x = y + coordinates[0], x + coordinates[1]

    if not (_ % 1000):
        redraw(window_size, size, canvas, colors, board)


redraw(window_size, size, canvas, colors, board)
root.mainloop()
