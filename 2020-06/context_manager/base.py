import random


class StorageException(Exception):
    """Raised when there is some issue with storage"""


class Storage:
    def __init__(self):
        print("init")

    def block_resources(self):
        print("block_resources")

    def release_resources(self):
        print("release_resources")

    def get(self, *args, **kwargs):
        if random.randint(0, 1):
            raise StorageException("Something goes wrong")
        print("get", args, kwargs)

    def put(self, *args, **kwargs):
        print("get", args, kwargs)
