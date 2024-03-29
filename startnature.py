import sys, os
from link.nature.remo import WebClient
from db.base import Factory, DataStore, ConnectInfo
from db.sqlite import Sqlite


class OUTPUT:
    """
    constants of Output mode.
    """
    SILENT = 0
    CONSOLE = 1
    FILE =2 
    VALUES = (SILENT, CONSOLE, FILE)

class DataBaseScript:
    CREATE_TABLE_DEVICE = "CREATE TABLE devices(id INTEGER PRIMARY KEY AUTOINCREMENT, values text, updatetime INTEGER)"
    CREATE_TABLE_APPLIANCE = "CREATE TABLE appliances(id INTEGER PRIMARY KEY AUTOINCREMENT, values text, updatetime INTEGER)"
    CREATE_TABLE_SETTING = "CREATE TABLE appliance_setting(id text PRIMARY KEY, type text, values text, updatetime INTEGER)"
    CREATE_TABLE_LOG = "CREATE TABLE log(id INTEGER PRIMARY KEY AUTOINCREMENT, event text, humidity INTEGER, temperature apicallcount INTEGER, messages text, updatetime INTEGER)"

class ApiResource:
    """
    constants of Output mode.
    """
    GET_DEVICE = "/1/appliances"
    GET_APPLIANCE = "/1/devices"
    POST_SIGNAL = "/1/devices"
    POST_SIGNAL = "/1/devices"
    START = 0
    END = 1
    SETTING = 2
    COOLER_MODE_TEMP = (30, 26 ,24)
    HOT_MODE_TEMP = (16, 21, 24)

def logger(mode) :
    """
    This is just for PoC.
    """
    PREFIX = "logger: "
    def _logger(func):
        def wrapper(*args, **kwargs):
            if mode == OUTPUT.SILENT:
                func(*args, **kwargs)
                return
            contents = dict(prefix=PREFIX, fn=func.__qualname__ + func.__name__)
            message = "{prefix} function: {fn} started."
            if mode == OUTPUT.CONSOLE :
                print(message.format(**contents))
            func(*args, **kwargs)
            message = "{prefix} function: {fn} finished."
            if mode == OUTPUT.CONSOLE :
                print(message.format(**contents))
        return wrapper
    return _logger

class Executable():
    @logger(OUTPUT.CONSOLE)
    def execute(self) :
        self.init()
        # start while loop 

        # check and update the datastore on every defined interval.
        # (backup table.)
        factory = Factory(Sqlite, ConnectInfo({"dbname":"./startnature.db"}))
        with factory.create() as con:
            pass

        # get information 
        # hume and temp, target device status.

        # if hume and temp is higer, make it be cool.

        # if hume and temp is lower, make it be warm. 

        # or else, hume and temp is comfortable, stay off or kill process. 

        # - hot season -> set starting cool point and stopping cool point 
        # e.g. ) start cool :30, stop cool :24, setting:20
        
        # - cold season -> set starting warm point and stopping warm point.  
        # e.g. ) start warm 16: stop warm 23:

        # - logging
        
        # repeat loop 

    def save(self) :
        # device master
        # device master history(by day? keep 180 days? )
        # airconditioner master 
        # cooler, warmer, handler setting 
        # logging current information: time, temp, huum, handle, target, device, use api count

        pass

class DryRunSet(Executable): 
    @logger(OUTPUT.CONSOLE)
    def init(self):
        self.token = "xxx"
        print("dummy start")

    @logger(OUTPUT.CONSOLE)
    def getDevice(self):
        print("dummy start")

class ProductSet(Executable):
    @logger(OUTPUT.CONSOLE)
    def init(self):
        self.token = os.getenv('NATURE_REMO_TOKEN')
        print("actual start")

    @logger(OUTPUT.CONSOLE)
    def getDevice(self):
        # firstAPI
        pass
        # apiClient = WebClient(self.token)
        # result = apiClient.send('/1/devices', Method=WebClient.get)

class DataSetup(Executable):
    @logger(OUTPUT.CONSOLE)
    def init(self):
        self.token = 'xxx'
        print("database setup start")
        Sqlite()
        DataBaseScript.c

        print("database setup end")
    @logger(OUTPUT.CONSOLE)
    def getDevice(self):
        pass


if __name__ == '__main__' :
    # TODO: multiprocess check

    args = sys.argv
    # DryRun or ProductRun
    if len(args) == 1:
        mode = DryRunSet() 
    elif not isinstance(args[1], int) :
        try :
            mode_value = int(args[1])
            mode = DryRunSet() if mode_value < 1 else ProductSet()
        except ValueError:
            exit("The 1st arg must be Integer. 0:DryRun 1:ProductMode.")
    mode.execute()

else :
    print("it is not main.")



