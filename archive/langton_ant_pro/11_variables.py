import tkinter

coord_moves = {
    "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
    "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
}


def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def rgb_int_to_hex(number):
    return "#{n:02x}{n:02x}{n:02x}".format(n=number)


size = 200
pattern = "RLR"
window_size = 600

steps_number = 15000
steps_render = 1000


board = create_board(size)
x, y = size // 2, size // 2
coordinates = (0, -1)


color_step = int(255 / (len(pattern) - 1))
colors = [rgb_int_to_hex(color_step * i) for i in range(len(pattern))][::-1]

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=window_size, height=window_size, bg="#fff")
canvas.pack()


def redraw(window_size, size, canvas, colors, board):
    s = window_size / size
    canvas.delete("all")
    for y, row in enumerate(board):
        for x, field in enumerate(row):
            color = colors[field]
            if field:
                canvas.create_rectangle(
                    s * x, s * y, s + (s * x), s + (s * y), fill=color, outline=color
                )
    canvas.update()


try:
    for _ in range(steps_number):
        field = board[y][x]
        direction = pattern[field]
        board[y][x] = (field + 1) % len(pattern)

        coordinates = coord_moves[direction][coordinates]
        y, x = y + coordinates[0], x + coordinates[1]

        if y < 0 or x < 0:
            raise IndexError

        if not (_ % steps_render):
            redraw(window_size, size, canvas, colors, board)
except IndexError:
    print(_)

redraw(window_size, size, canvas, colors, board)
root.mainloop()
