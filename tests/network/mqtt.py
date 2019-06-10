import os, sys, time, unittest

module_path  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class SubscriberTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bind_service(self):
        s = Subscriber()
        print(s.connect())
        p = Publisher()
        self.assertEqual('Publisher', (p.connect()))


if __name__ == '__main__':
    if module_path not in sys.path:
        sys.path.append(module_path)
    from network.mqtt import (
        Subscriber,
        Publisher,
    )
    unittest.main()
