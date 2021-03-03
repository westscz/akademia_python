from mxd import Market, Game
from tkinter import *

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

# root = Tk()
# Label(root, text='Kasa').pack()
# Label(root, text=f"{g.money}").pack()
# Label(root, text='Depozyt').pack()
# Label(root, text=f"{g.deposit}").pack()
# Label(root, text='Prestiż').pack()
# Label(root, text=f"{g.respect}").pack()
# Label(root, text='Dług').pack()
# Label(root, text=f"{g.debt}").pack()
# Label(root, text='Kondycja').pack()
# Label(root, text=f"{g.health}%").pack()
# for city in g.cities:
#     Button(root, text=city).pack()
# root.mainloop()


## STEP 2

# root = Tk()
# info_frame = Frame(root)
# info_frame.pack(side=LEFT)

# city_frame = Frame(root)
# city_frame.pack(side=RIGHT)

# Label(info_frame, text='Kasa').pack()
# Label(info_frame, text=f"{g.money}").pack()
# Label(info_frame, text='Depozyt').pack()
# Label(info_frame, text=f"{g.deposit}").pack()
# Label(info_frame, text='Prestiż').pack()
# Label(info_frame, text=f"{g.respect}").pack()
# Label(info_frame, text='Dług').pack()
# Label(info_frame, text=f"{g.debt}").pack()
# Label(info_frame, text='Kondycja').pack()
# Label(info_frame, text=f"{g.health}%").pack()

# for city in g.cities:
#     Button(city_frame, text=city).pack()
# root.mainloop()

## STEP3

# root = Tk()
# info_frame = Frame(root)
# info_frame.pack(side=LEFT)

# city_frame = Frame(root)
# city_frame.pack(side=RIGHT)

# Label(info_frame, text='Kasa').pack()
# Label(info_frame, text=f"{g.money}").pack()
# Label(info_frame, text='Depozyt').pack()
# Label(info_frame, text=f"{g.deposit}").pack()
# Label(info_frame, text='Prestiż').pack()
# Label(info_frame, text=f"{g.respect}").pack()
# Label(info_frame, text='Dług').pack()
# Label(info_frame, text=f"{g.debt}").pack()
# Label(info_frame, text='Kondycja').pack()
# Label(info_frame, text=f"{g.health}%").pack()

# for city in g.cities:
#     Button(city_frame, text=city).pack()

# market = Listbox(root)
# for i, drug in enumerate(g.market.keys()):
#     market.insert(i, f"{drug}|{g.market[drug]}")
# market.pack(side=BOTTOM)

# root.mainloop()


## Step 4

# root = Tk()

# manager_frame = Frame(root)
# manager_frame.pack(side=TOP)

# bussines_frame = Frame(root)
# bussines_frame.pack(side=BOTTOM)

# info_frame = Frame(manager_frame)
# info_frame.pack(side=LEFT)

# city_frame = Frame(manager_frame)
# city_frame.pack(side=RIGHT)

# Label(info_frame, text='Kasa').pack()
# Label(info_frame, text=f"{g.money}").pack()
# Label(info_frame, text='Depozyt').pack()
# Label(info_frame, text=f"{g.deposit}").pack()
# Label(info_frame, text='Prestiż').pack()
# Label(info_frame, text=f"{g.respect}").pack()
# Label(info_frame, text='Dług').pack()
# Label(info_frame, text=f"{g.debt}").pack()
# Label(info_frame, text='Kondycja').pack()
# Label(info_frame, text=f"{g.health}%").pack()

# for city in g.cities:
#     Button(city_frame, text=city).pack()

# market = Listbox(bussines_frame)
# for i, drug in enumerate(g.market.keys()):
#     market.insert(i, f"{drug}|{g.market[drug]}")
# market.pack(side=LEFT)

# market = Listbox(bussines_frame)
# for i, drug in enumerate(g.stash.keys()):
#     market.insert(i, f"{drug}|{g.stash[drug]}")
# market.pack(side=RIGHT)


# root.mainloop()

## Step 5

root = Tk(className="MaxDilla 2020")

manager_frame = Frame(root, bg="green")
manager_frame.pack(side=TOP)

bussines_frame = Frame(root)
bussines_frame.pack(side=BOTTOM)

events_frame = Frame(root)
events_frame.pack()

events_listbox = Listbox(events_frame, height=3)
events_listbox.pack()

info_frame = Frame(manager_frame)
info_frame.pack(side=LEFT)

stats_frame = Frame(info_frame)
stats_frame.pack(side=TOP)


city_frame = Frame(manager_frame)
city_frame.pack(side=RIGHT)

money_frame = Frame(stats_frame)
deposit_frame = Frame(stats_frame)
respect_frame = Frame(stats_frame)
debt_frame = Frame(stats_frame)

gr = [(r, c) for c in range(2) for r in range(2)]
for i, f in enumerate([money_frame, deposit_frame, respect_frame, debt_frame]):
    f.grid(row=gr[i][0], column=[gr[i][1]])


health_frame = Frame(info_frame)
health_frame.pack(side=BOTTOM)

Label(money_frame, text="Kasa", bg="white", width=5).pack(side=LEFT)
Label(money_frame, text=f"{g.money}", width=5).pack(side=RIGHT)
Label(deposit_frame, text="Depozyt", bg="white", width=5).pack(side=LEFT)
Label(deposit_frame, text=f"{g.deposit}", width=5).pack(side=RIGHT)
Label(respect_frame, text="Prestiż", width=5).pack(side=LEFT)
Label(respect_frame, text=f"{g.respect}", width=5).pack(side=RIGHT)
Label(debt_frame, text="Dług", width=5).pack(side=LEFT)
Label(debt_frame, text=f"{g.debt}", width=5).pack(side=RIGHT)
Label(health_frame, text="Kondycja").pack(side=TOP)
Label(health_frame, text=f"{g.health}%", bg="red", width=20).pack(side=BOTTOM)

Label(city_frame, text="Wybierz miasto do którego pojedziesz").pack()
city_buttons = Frame(city_frame)
city_buttons.pack()


cities = {}


market_listbox = Listbox(bussines_frame)
for i, drug in enumerate(g.market.keys()):
    market_listbox.insert(i, f"{drug}|{g.market[drug]}")
market_listbox.pack(side=LEFT)


def change_city(game, city):
    print(f"change city {city}")
    game.move(city)
    for city, city_button in cities.items():
        if game.city == city:
            city_button.config(state=DISABLED)
        else:
            city_button.config(state=NORMAL)
    market_listbox.delete(0, END)
    for i, drug in enumerate(g.market.keys()):
        market_listbox.insert(i, f"{drug}|{g.market[drug]}")


gr = [(r, c) for c in range(2) for r in range(3)]
for i, city in enumerate(g.cities):
    b = Button(
        city_buttons,
        text=city,
        width=12,
        command=(lambda x=city: change_city(g, x)),
        state=NORMAL if i else DISABLED,
        padx=10,
        pady=10,
    )
    b.grid(row=gr[i][0], column=gr[i][1])
    cities[city] = b


stash_listbox = Listbox(bussines_frame)
for i, drug in enumerate(g.stash.keys()):
    stash_listbox.insert(i, f"{drug}|{g.stash[drug]}")


def buy_drugs():
    index, *_ = market_listbox.curselection()
    drug, *_ = market_listbox.get(index).split("|")
    g.buy_drugs(drug, 1)
    stash_listbox.delete(0, END)
    for i, drug in enumerate(g.stash.keys()):
        stash_listbox.insert(i, f"{drug}|{g.stash[drug]}")


bussines_panel = Frame(bussines_frame)
bussines_panel.pack(side=LEFT)
buy = Button(bussines_panel, width=8, text="Wyrzuc").pack()
buy = Button(
    bussines_panel, width=8, height=2, text="Kupuj >>", command=buy_drugs
).pack()
buy = Button(bussines_panel, width=8, height=2, text="<< Sprzedaj").pack()
buy = Button(bussines_panel, width=8, text="Sklep").pack()
buy = Button(bussines_panel, width=8, text="Szpital").pack()
buy = Button(bussines_panel, width=8, text="Finanse").pack()


stash_listbox.pack(side=RIGHT)


root.mainloop()
