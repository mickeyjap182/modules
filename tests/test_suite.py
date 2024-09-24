import os, sys, time, unittest
from core import Core

def suite():
    top_dir = os.path.dirname(Core.test_path)
    tests = unittest.TestLoader().discover(start_dir=Core.test_path,
                                         pattern='test*.py',
                                         top_level_dir=top_dir)
    runner = unittest.TextTestRunner()
    runner.run(tests)

if __name__ == '__main__':
    suite()
