import time
import math
from datetime import (
    datetime,
    timedelta,
)

class StopWatch():

    def __init__(self, *args, **kwargs):
        """
        stopwatch
        """
        self.date = datetime
        self.start = time.perf_counter()
    def stop(self):
        self.last = time.perf_counter()
        return self.last
    def elapsed(self, rounded=None):
        if rounded is None:
            return round(self.last - self.start)
        return round(self.last - self.start, rounded)

class Traveler():
    def __init__(self, *args, **kwargs):
        """
        timetraveler
        arguments:date=***, lang=***, zone=***
        """
        self.date = kwargs['date']

    def yesterday(self):
        return self.date + timedelta(days=-1)

class Artisan():

    @staticmethod
    def create(product, *args, **kwargs):
        """ parame is something like locale, timezone """
        kwargs['date'] = kwargs.pop('date') if 'date' in kwargs else datetime.now()
        return product(**kwargs)
