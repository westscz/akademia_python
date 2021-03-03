from dataclasses import dataclass


@dataclass
class Store:
    uuid: int
    name: str


@dataclass
class PlaceStore:
    uuid: int
    place_id: int
    store_id: int


@dataclass
class Place:
    uuid: int
    name: str
    items: list
    store_id: int


@dataclass
class Item:
    uuid: int
    name: str
    quantity: int
    place_id: int
    mandatory: bool


class StoreRepository:
    def __init__(self):
        self.store = {}
        self.index = 1

    def add(self, name):
        obj = Store(self.index, name, [])
        self.store[self.index] = obj
        self.index += 1
        return obj


class PlaceRepository:
    def __init__(self):
        self.store = {}
        self.index = 1

    def add(self, name):
        obj = Place(self.index, name, [])
        self.store[self.index] = obj
        self.index += 1
        return obj


class ItemRepository:
    def __init__(self):
        self.store = {}
        self.index = 1

    def add(self, name, quantity=1, place_id=0, mandatory=True):
        obj = Item(self.index, name, quantity, place_id, mandatory)
        self.store[self.index] = obj
        self.index += 1
        return obj

    def update(self, item_id, place_id=None):
        if place_id:
            self.store[self.index].place_id = place_id
        return self.store[item_id]

    def get_mandatory_items(self):
        return [item for item in self.store.values() if item.mandatory]

    def get_not_mandatory_items(self):
        return [item for item in self.store.values() if not item.mandatory]


class Logic:
    def __init__(self, place_repository, item_repository):
        self.pr = place_repository
        self.ir = item_repository

    def add_item(self, name, quantity=1, place_id=0, mandatory=True):
        return self.ir.add(name, quantity, place_id, mandatory)

    def add_place(self, name):
        return self.pr.add(name)


pr = PlaceRepository()
ir = ItemRepository()
l = Logic(pr, ir)

kitchen = l.add_place("Kuchnia")
fridge = l.add_place("Lodówka")
bathroom = l.add_place("Łazienka")

l.add_item("Masło", place_id=fridge.uuid)
l.add_item("Mleko", 2, place_id=fridge.uuid)
l.add_item("Papier toaletowy", place_id=bathroom.uuid)
l.add_item("Woda mineralna", 6, place_id=kitchen.uuid)
