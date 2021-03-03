from contextlib import contextmanager
from base import Storage


@contextmanager
def storage_access():
    storage = Storage()
    storage.block_resources()
    try:
        yield storage
    finally:
        storage.release_resources()


with storage_access() as s:
    s.get(filename="secrets.yaml")
