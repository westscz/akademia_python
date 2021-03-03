class StorageContext:
    ""

    def __enter__(self):
        pass

    def __exit__(self):
        pass


with StorageContext() as storage:
    print(storage)
