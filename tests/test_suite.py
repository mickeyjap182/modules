import os, sys, time, unittest
from platform import python_version

from core import Config

def suite():
    """ do all tests """
    print(Config.os)
    top_dir = Config.module_path
    tests = unittest.TestLoader().discover(start_dir=Config.test_path,
                                         pattern='test*.py',
                                         top_level_dir=top_dir)
    runner = unittest.TextTestRunner()
    runner.run(tests)

if __name__ == '__main__':
    suite()
