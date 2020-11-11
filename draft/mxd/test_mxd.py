import unittest
from mxd import (
    Game,
    Market,
    WrongMoneyAmountError,
    WrongCityError,
    MoneyNotAvailableError,
    DebtError,
    GameEndException,
    MarketError,
    StashError,
)


class TestGame(unittest.TestCase):
    def setUp(self):
        m = Market({})
        self.g = Game(market=m)

    def test_day_one_on_start(self):
        self.assertEqual(self.g.day, 1)

    def test_city_start(self):
        self.assertEqual(self.g.city, "Katowice")

    def test_change_city_next_day(self):
        """Change city should also change day to next"""
        self.g.move("Tychy")
        self.assertEqual(self.g.day, 2)
        self.assertEqual(self.g.city, "Tychy")

    def test_respect_on_start(self):
        self.assertEqual(self.g.respect, 0)

    def test_money_on_start(self):
        self.assertEqual(self.g.money, 198)

    def test_debt_on_start(self):
        self.assertEqual(self.g.debt, 104)

    def test_deposit_on_start(self):
        self.assertEqual(self.g.deposit, 0)

    def test_next_day_change_debt(self):
        self.g.move("Tychy")
        self.assertEqual(self.g.debt, 109)

    def test_health_on_start(self):
        self.assertEqual(self.g.health, 100)

    def test_lower_respect_if_no_money(self):
        self.g.money = 0
        self.g.move("Tychy")
        self.assertEqual(self.g.respect, -1)

    def test_heal_price_full_health(self):
        result = self.g.heal_price()
        self.assertEqual(result, 0)

    def test_heal_price_90_percent(self):
        self.g.health = 90
        result = self.g.heal_price()
        self.assertEqual(result, 100)

    def test_available_cities(self):
        self.assertEqual(
            self.g.cities,
            ["Katowice", "Tychy", "Oświęcim", "Murcki", "Zabrze", "Gliwice"],
        )

    def test_move_to_illegal_city(self):
        with self.assertRaises(WrongCityError):
            self.g.move("Krakow")

    def test_pay_debt(self):
        self.g.pay_debt(0)
        self.assertEqual(self.g.debt, 104)

    def test_pay_debt_should_change_available_money(self):
        self.g.pay_debt(4)
        self.assertEqual(self.g.money, 194)
        self.assertEqual(self.g.debt, 100)

    def test_pay_debt_clear_debt(self):
        self.g.pay_debt(104)
        self.assertEqual(self.g.money, 94)

    def test_pay_debt_more_than_debt(self):
        with self.assertRaises(WrongMoneyAmountError):
            self.g.pay_debt(150)

    def test_pay_debt_more_than_available_money(self):
        self.g.debt = 300
        with self.assertRaises(MoneyNotAvailableError):
            self.g.pay_debt(200)

    def test_get_credit_not_available(self):
        with self.assertRaises(DebtError):
            self.g.get_credit(1)

    def test_get_credit(self):
        self.g.pay_debt(104)
        self.g.get_credit(50)
        self.assertEqual(self.g.debt, 50)
        self.assertEqual(self.g.money, 198 - 104 + 50)

    def test_get_credit_too_much(self):
        self.g.pay_debt(104)
        with self.assertRaises(WrongMoneyAmountError):
            self.g.get_credit(200)

    def test_set_game_time(self):
        g = Game(365)
        self.assertEqual(g.days, 365)

    def test_end_game_after_days_limit(self):
        m = Market({})
        g = Game(2, market=m)
        g.move("Tychy")
        with self.assertRaises(GameEndException):
            g.move("Katowice")

    def test_get_market_empty(self):
        m = Market({})
        g = Game(market=m)
        self.assertEqual(g.market, {})

    def test_empty_drugs_stash_on_start(self):
        self.assertEqual(self.g.stash, {})

    def test_buy_drug(self):
        config = {"grass": (20, 29)}
        m = Market(config)
        g = Game(market=m)
        g.buy_drugs("grass", 1)
        self.assertEqual(g.stash, {"grass": 1})

    def test_buy_drugs_subtracts_money(self):
        config = {"grass": (20, 20)}
        m = Market(config)
        g = Game(market=m)
        g.buy_drugs("grass", 1)
        self.assertEqual(g.money, 198 - 20)

    def test_buy_drugs_should_fail_if_not_available(self):
        m = Market({})
        g = Game(market=m)
        with self.assertRaises(MarketError):
            g.buy_drugs("grass", 1)

    def test_buy_drugs_should_fail_if_money_not_available(self):
        m = Market({"grass": (200, 200)})
        g = Game(market=m)
        with self.assertRaises(MoneyNotAvailableError):
            g.buy_drugs("grass", 1)

    def test_drug_price_should_change_next_day(self):
        config = {"grass": (20, 200)}
        m = Market(config)
        g = Game(market=m)
        before = g.market
        g.move("Tychy")
        self.assertNotEqual(before["grass"], g.market["grass"])

    def test_sell_drug(self):
        config = {"grass": (20, 20)}
        m = Market(config)
        g = Game(market=m)
        g.buy_drugs("grass", 1)
        g.sell_drugs("grass", 1)
        self.assertDictEqual(g.stash, {})
        self.assertEqual(g.money, 198)

    def test_sell_drugs_not_available_on_market(self):
        config = {"grass": (20, 20)}
        m = Market(config)
        g = Game(market=m)
        with self.assertRaises(MarketError):
            g.sell_drugs("acid", 1)

    def test_sell_drugs_wrong_amount(self):
        config = {"grass": (20, 20)}
        m = Market(config)
        g = Game(market=m)
        g.buy_drugs("grass", 1)
        with self.assertRaises(StashError):
            g.sell_drugs("grass", 41)


class TestMarket(unittest.TestCase):
    def test_generate_returns_dict(self):
        result = Market({}).generate()
        self.assertEqual(result, {})

    def test_set_config(self):
        config = {"grass": (20, 29)}
        m = Market(config)

    def test_generate_returns_drug_from_config(self):
        config = {"grass": (20, 29)}
        m = Market(config)
        result = m.generate()
        self.assertEqual(result.keys(), config.keys())

    def test_generate_price_from_range(self):
        config = {"grass": (20, 29)}
        m = Market(config)
        result = m.generate()
        self.assertGreaterEqual(result["grass"], 20)
        self.assertLessEqual(result["grass"], 29)
