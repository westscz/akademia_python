import time
import logging

logging.basicConfig(level=logging.DEBUG)


class MeasureCodeExecution:
    def __init__(self, name=""):
        self.start = None
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        end = time.time()
        delta = end - self.start
        logging.info("time of execution '%s':%s", self.name, delta)


with MeasureCodeExecution("sleep"):
    time.sleep(1)
