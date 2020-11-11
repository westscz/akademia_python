"""https://web.archive.org/web/20021130164507/http://www.maxdila.prv.pl:80/"""

from collections import defaultdict
from random import randint


class DebtError(Exception):
    ...


class MoneyNotAvailableError(Exception):
    ...


class WrongMoneyAmountError(Exception):
    ...


class WrongCityError(Exception):
    ...


class GameEndException(Exception):
    ...


class MarketError(Exception):
    ...


class StashError(Exception):
    ...


class Game:
    def __init__(self, days=31, market=None):
        self.days = days
        self.day = 1

        self.cities = ["Katowice", "Oświęcim", "Zabrze", "Tychy", "Murcki", "Gliwice"]
        self.city = self.cities[0]

        self.health = 100
        self.respect = 0

        self.money = 198
        self.debt = 104
        self.deposit = 0

        self._market = market
        self._stash = defaultdict(lambda: 0)

    @property
    def market(self):
        return self._market.state

    @property
    def stash(self):
        return {k: v for k, v in self._stash.items() if v}

    def move(self, city):
        if city not in self.cities:
            raise WrongCityError("Not available city")
        self.day += 1
        if self.day > self.days:
            raise GameEndException
        self.city = city
        self.update_debt()
        self.update_respect()
        self.update_market()

    def update_market(self):
        self._market.generate()

    def update_debt(self):
        self.debt = int(self.debt * 1.05)

    def update_respect(self):
        if self.money == 0:
            self.respect -= 1

    def heal_price(self):
        return (100 - self.health) * 10

    def pay_debt(self, amount):
        if amount > self.debt:
            raise WrongMoneyAmountError
        if amount > self.money:
            raise MoneyNotAvailableError
        self.debt -= amount
        self.money -= amount

    def get_credit(self, amount):
        if self.debt:
            raise DebtError
        if amount > self.money * 2:
            raise WrongMoneyAmountError
        self.debt = amount
        self.money += amount

    def buy_drugs(self, name, amount):
        if not self._market.get(name):
            raise MarketError
        price = amount * self._market.get(name)
        if price > self.money:
            raise MoneyNotAvailableError
        self._stash[name] += amount
        self.money -= amount * self._market.get(name)

    def sell_drugs(self, name, amount):
        if not self._market.get(name):
            raise MarketError
        if self._stash[name] < amount:
            raise StashError
        self._stash[name] -= amount
        self.money += amount * self._market.get(name)


class Market:
    def __init__(self, prices):
        self._prices = prices
        self.generate()

    @property
    def state(self):
        return self._state

    def get(self, name):
        return self._state.get(name, 0)

    def generate(self):
        self._state = {
            key: randint(value[0], value[1]) for key, value in self._prices.items()
        }
        return self._state
