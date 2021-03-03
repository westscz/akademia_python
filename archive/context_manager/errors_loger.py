import logging

logging.basicConfig(level=logging.DEBUG)


class IgnoreExceptions:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logging.error("exception ignored : %s", exc_type.__name__)
        return True


with IgnoreExceptions():
    raise ArithmeticError
