from base import Storage

storage = Storage()
storage.block_resources()
storage.get(filename="secrets.yaml")
storage.release_resources()
