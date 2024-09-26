import os, sys, time, unittest

# It is required when you'll run the unittest. 
if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    print(path)
    if path not in sys.path:
        sys.path.append(path)

    from network.mqtt import (
        Subscriber,
        Publisher,
    )

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
    unittest.main()
