from mxd import Market, Game
from tkinter import *


class MxdGui:
    def __init__(self):
        self.root = Tk()

    def set_menubar(self):
        menubar = Menu(self.root)

        game_menu = Menu(menubar, tearoff=0)
        game_menu.add_cascade(label="Gra")
        options_menu = Menu(menubar, tearoff=0)
        options_menu.add_cascade(label="Opcje")
        info_menu = Menu(menubar, tearoff=0)
        info_menu.add_cascade(label="Informacja")
        self.root.config(menu=menubar)

    def set_control_buttons(self):
        menu_frame = Frame(self.left_frame, bg="#F44")
        menu_frame.pack()

        Button(menu_frame, text="Nowa gra").pack(side=LEFT)
        Button(menu_frame, text="Wykres").pack(side=LEFT)
        Button(menu_frame, text="Gang").pack(side=LEFT)

    def set_base_layout(self):
        self.control_frame = Frame(self.main_frame, bg="#F00", width=400, height=500)
        self.control_frame.pack()

        self.left_frame = Frame(self.control_frame, bg="#F22", width=200, height=200)
        self.left_frame.pack(side=LEFT)

        self.right_frame = Frame(self.control_frame, bg="#F66", width=200, height=200)
        self.right_frame.pack(side=RIGHT)

        self.event_frame = Frame(self.main_frame, bg="#0F0", width=400, height=50)
        self.event_frame.pack()

        self.bussines_frame = Frame(self.main_frame, bg="#00F", width=400, height=250)
        self.bussines_frame.pack(side=BOTTOM)

        self.left_frame_b = Frame(self.bussines_frame, bg="#22F", width=170, height=250)
        self.left_frame_b.pack(side=LEFT)

        self.buttons_frame_b = Frame(
            self.bussines_frame, bg="#44F", width=60, height=250
        )
        self.buttons_frame_b.pack(side=LEFT)

        self.right_frame_b = Frame(
            self.bussines_frame, bg="#66F", width=170, height=250
        )
        self.right_frame_b.pack(side=LEFT)

    def initialize_gui(self, cities):
        self.main_frame = Frame(self.root, bg="#0F0", width=400, height=600)
        self.main_frame.pack()

        self.set_menubar()
        self.set_base_layout()
        self.set_left_frame()
        self._set_right_frame(cities)
        self.set_event_frame()

        self.set_bussines_left_frame()
        self.set_bussines_buttons_frame()
        self.set_bussines_right_frame()

        return self

    def set_left_frame(self):

        self.set_control_buttons()
        stats_frame = Frame(self.left_frame)
        stats_frame.pack()

        money_frame = Frame(stats_frame)
        money_frame.grid(row=0, column=0)
        Label(money_frame, text="Kasa", bg="white", width=8).pack(side=LEFT)
        self.money = Label(money_frame, text="0", width=8)
        self.money.pack(side=RIGHT)

        deposit_frame = Frame(stats_frame)
        deposit_frame.grid(row=0, column=1)
        Label(deposit_frame, text="Depozyt", bg="white", width=8).pack(side=LEFT)
        self.deposit = Label(deposit_frame, text="0", width=8)
        self.deposit.pack(side=RIGHT)

        respect_frame = Frame(stats_frame)
        respect_frame.grid(row=1, column=0)
        Label(respect_frame, text="Prestiż", width=8).pack(side=LEFT)
        self.respect = Label(respect_frame, text="0", width=8)
        self.respect.pack(side=RIGHT)

        debt_frame = Frame(stats_frame)
        debt_frame.grid(row=1, column=1)
        Label(debt_frame, text="Dług", width=8).pack(side=LEFT)
        self.debt = Label(debt_frame, text="0", width=8)
        self.debt.pack(side=RIGHT)

        health_frame = Frame(self.left_frame)
        health_frame.pack()
        Label(health_frame, text="Kondycja:").pack(side=TOP)
        self.health = Label(health_frame, text="100%", bg="red", width=16)
        self.health.pack(side=BOTTOM)

    def _set_right_frame(self, cities):
        self.cities_buttons = {}

        Label(self.right_frame, text="Wybierz miasto do którego pojedziesz.").pack()

        city_frame = Frame(self.right_frame)
        city_frame.pack(side=RIGHT)

        grids = [(r, c) for r in range(3) for c in range(2)]

        for i, city in enumerate(cities):
            city_button = Button(city_frame, text=city, width=12, height=3)
            city_button.grid(row=grids[i][0], column=grids[i][1])
            self.cities_buttons[city] = city_button

    def initialize_game(self):
        self.update_cities("Katowice")
        return self

    def update_cities(self, active):
        for name, button in self.cities_buttons.items():
            if active == name:
                button.config(state=DISABLED)
            else:
                button.config(state=NORMAL)

    def set_event_frame(self):
        Label(self.event_frame, text="Wydarzenia").pack()
        self.event_box = Listbox(self.event_frame, height=3, width=60).pack(side=BOTTOM)

    def set_bussines_left_frame(self):
        Label(self.left_frame_b, text="Dostępne na rynku narkotyki").pack()
        self.market_box = Listbox(self.left_frame_b)
        self.market_box.pack(side=BOTTOM)

    def set_bussines_buttons_frame(self):
        Button(self.buttons_frame_b, width=8, text="Wyrzuć").pack()
        self.buy = Button(self.buttons_frame_b, width=8, height=2, text="Kupuj >>")
        self.buy.pack()

        self.sell = Button(self.buttons_frame_b, width=8, height=2, text="<< Sprzedaj")
        self.sell.pack()

        Button(self.buttons_frame_b, width=8, text="Sklep").pack()
        Button(self.buttons_frame_b, width=8, text="Szpital").pack()
        Button(self.buttons_frame_b, width=8, text="Finanse").pack()

    def set_bussines_right_frame(self):
        right_top_frame = Frame(self.right_frame_b)
        right_top_frame.pack()

        Label(right_top_frame, text="Miejsce").pack(side=LEFT)

        self.stash_size_label = Label(right_top_frame, text=f"0/0")
        self.stash_size_label.pack(side=LEFT)

        self.inventory_button = Button(right_top_frame, text="Towar")
        self.inventory_button.pack(side=RIGHT)

        self.stash_box = Listbox(self.right_frame_b)
        self.stash_box.pack(side=BOTTOM)

    def update_market(self, market):
        self.market_box.delete(0, END)
        for i, drug in enumerate(market.keys()):
            self.market_box.insert(i, f"{drug}|{market[drug]}")

    def update_stash(self, stash):
        self.stash_box.delete(0, END)
        for i, drug in enumerate(stash.keys()):
            self.stash_box.insert(i, f"{drug}|{stash[drug]}")

    def run(self):
        self.root.mainloop()

    def update_stats(self, money, deposit, respect, debt):
        self.money.config(text=money)
        self.deposit.config(text=deposit)
        self.respect.config(text=respect)
        self.debt.config(text=debt)


def buy(g, gui):
    if not gui.market_box.curselection():
        return
    drug = gui.market_box.get(gui.market_box.curselection()).split("|")[0]
    g.buy_drugs(drug, 1)
    gui.update_stats(g.money, g.deposit, g.respect, g.debt)
    gui.update_stash(g.stash)


def sell(g, gui):
    if not gui.stash_box.curselection():
        return
    drug = gui.stash_box.get(gui.stash_box.curselection()).split("|")[0]
    g.sell_drugs(drug, 1)
    gui.update_stats(g.money, g.deposit, g.respect, g.debt)
    gui.update_stash(g.stash)


def change_city(g: Game, gui: MxdGui, city: str):
    g.move(city)
    gui.update_cities(city)
    gui.update_stats(g.money, g.deposit, g.respect, g.debt)
    gui.update_market(g.market)


if __name__ == "__main__":
    prices = {
        "grass": (20, 29),
        "scun": (30, 44),
        "hash": (20, 29),
        "acid": (20, 29),
        "extasy": (15, 21),
        "speed": (28, 44),
        "heroine": (40, 59),
        "coca": (100, 149),
        "sugar": (40, 59),
        "mush": (15, 21),
    }

    m = Market(prices)
    g = Game(days=31, market=m)
    gui = MxdGui().initialize_gui(cities=g.cities)
    gui.initialize_game()
    gui.update_market(g.market)
    gui.update_stash(g.stash)
    gui.update_stats(g.money, g.deposit, g.respect, g.debt)

    gui.buy.config(command=lambda: buy(g, gui))
    gui.sell.config(command=lambda: sell(g, gui))

    for city, button in gui.cities_buttons.items():
        button.config(command=(lambda x=city: change_city(g, gui, x)))

    gui.run()
