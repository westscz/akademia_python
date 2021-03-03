class StorageContext:
    ""

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


with StorageContext() as storage:
    print(storage)
