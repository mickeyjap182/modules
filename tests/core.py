import os, sys

class Core():
    """ core module of tests. """
    test_path = None
    module_path = None
    # TODO: make them singleton.
    @classmethod
    def find_test_path(cls):
        if cls.test_path is None:
            cls.test_path = os.path.dirname(os.path.abspath(__file__))
        return cls.test_path
    @classmethod
    def find_module_path(cls):
        if cls.module_path is None:
            cls.module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return cls.module_path

test_path = Core.find_test_path()
module_path = Core.find_module_path()
