from pprint import pprint

from mxd import Market, Game

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


def print_basic_info(game):
    g = game
    print(f"Kasa {g.money} Depozyt {g.deposit} Prestiż {g.respect} Dług {g.debt})")
    print(f"Kondycja {g.health}")


def print_market(game):
    pprint(game.market)


if __name__ == "__main__":
    m = Market(prices)
    g = Game(days=31, market=m)
    print_basic_info(g)
    print_market(g)
