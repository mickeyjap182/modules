import os, sys, time, unittest
from core import Config

def suite():
    print(Config.test_path)
    top_dir = os.path.dirname(Config.test_path)
    tests = unittest.TestLoader().discover(start_dir=Config.test_path,
                                         pattern='test*.py',
                                         top_level_dir=top_dir)
    runner = unittest.TextTestRunner()
    runner.run(tests)

if __name__ == '__main__':
    suite()
