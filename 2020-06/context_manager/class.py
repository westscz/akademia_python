from base import Storage


class StorageContext:
    def __init__(self):
        self.storage = Storage()

    def __enter__(self):
        self.storage.block_resources()
        return self.storage

    def __exit__(self, *args, **kwargs):
        self.storage.release_resources()


with StorageContext() as s:
    s.get(filename="secrets.yaml")
