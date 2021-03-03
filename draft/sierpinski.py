# x = [[0 for _ in range(3)] for _ in range(3)]
# # mala tablica 3x3
# cube = len(x)//3
# # sprawdzamy rozmiar jednego kwadratu
# slice_ = [row[:cube] for row in x[:cube]]
# # wycinamy ten kwadrat
# s = slice_.copy()

# #doszlismy do najmniejszego elementu wiec zaczynamy wracać:
# if len(slice_) == 1:
#     slice_=[[1]]

# y = [cub*3 for cub in slice_] +[cub+ empty+ cub for cub in slice_ for empty in s] + [cub*3 for cub in slice_]
# from pprint import pprint
# pprint(y)

# mala tablica 3x3
import math


def create_table(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def sierp(table):
    cube_size = len(table) // 3
    cube = [row[:cube_size] for row in table[:cube_size]]
    s = cube.copy()

    if len(cube) == 1:
        cube = [[1]]
    else:
        cube = sierp(cube)
    result = (
        [cub * 3 for cub in cube]
        + [cub + s[i] + cub for i, cub in enumerate(cube)]
        + [cub * 3 for cub in cube]
    )
    return result


result = sierp(create_table(3))
assert result == [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

result = sierp(create_table(pow(3, 5)))


import tkinter

root = tkinter.Tk()
resolution = 800
canvas = tkinter.Canvas(root, width=resolution, height=resolution, bg="#FFF")
canvas.pack()
print(len(result))
size = resolution // len(result)
for x, row in enumerate(result):
    for y, field in enumerate(row):
        if field:
            canvas.create_rectangle(
                size * y,
                size * x,
                size + (size * y),
                size + (size * x),
                outline="white" if not field else "black",
                fill="white" if not field else "black",
            )

root.mainloop()
