import sys, os
from link.nature.remo import WebClient

class OUTPUT:
    """
    constants of Output mode.
    """
    SILENT = 0
    CONSOLE = 1
    FILE =2 
    VALUES = (SILENT, CONSOLE, FILE)

class ApiResourceKey:
    """
    constants of Output mode.
    """
    GET_DEVICE = ""
    GET_ = ""

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



