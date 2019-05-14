from datetime import datetime, timedelta
import time

Locales = {

}
class Formater():

    def __init__(self, *args, **kwargs):
        """
        delimiter: delimiter of column
        line_sep: separater of line as record
        """
        pass
    def D2Str(self, format):

class D2Str():

    def __init__(self, *args, **kwargs):
        """
        date to str
        """
        pass

class S2Date():

    def __init__(self, ):
        """
        str to date
        """
        pass

class StopWatch():

    def __init__(self, *args, **kwargs):
        """
        stopwatch
        """
        pass

class Traveler:
    def __init__(self, *args, **kwargs):
        """
        timetraveler
        arguments:lang=***, zone=***
        """
        pass

    def yesterday(date):
        return date + timedelta(days=-1)

class Artisan():

    @staticmethod
    def create(work, params):
        """ parame is something like locale, timezone """
        return work(params)
