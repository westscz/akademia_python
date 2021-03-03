from base import Storage

storage = Storage()
storage.block_resources()
try:
    storage.get(filename="secrets.yaml")
finally:
    storage.release_resources()
