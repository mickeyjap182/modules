import os, sys, time, unittest

module_path  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class ProcessingTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        p = Processing()
        self.assertEqual('', p.example())


if __name__ == '__main__':
    if module_path not in sys.path:
        sys.path.append(module_path)
    from lang.nlp import (
        Processing,
    )
    unittest.main()
