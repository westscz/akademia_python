class StorageContext:
    ""

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass


with StorageContext() as storage:
    print(storage)
