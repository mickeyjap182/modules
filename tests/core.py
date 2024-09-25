
import os, sys

class Helper():
    # TODO: make them singleton.
    @classmethod
    def find_test_path(cls):
        return os.path.dirname(os.path.abspath(__file__))

    @classmethod
    def find_module_path(cls):
        return  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    @classmethod
    def append_sys_path(cls, path):
        if path not in sys.path:
            sys.path.append(path)

class Config():
    """ config module of tests. """
    test_path = Helper.find_test_path()
    module_path = Helper.find_module_path()
