class StorageContext:
    ""

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(args)


with StorageContext() as storage:
    raise ValueError
