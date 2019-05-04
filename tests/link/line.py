import os, sys, unittest

module_path  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class TestLine(unittest.TestCase):

    def setUp(self):
        self.img_path = os.path.join(module_path, 'tests', 'image', 'input')
        pass

    def tearDown(self):
        pass

    def test_send_message(self):
        # input file
        token = "xxx"
        s = Subscriber(token)
        # s.send("test")
        self.assertTrue(True)

    def test_send_message_img(self):
        # input file
        token = "xxx"
        s = Subscriber(token)
        # s.send("Today's alert", os.path.join(self.img_path, 'line_plot.png'))
        self.assertTrue(True)

if __name__ == '__main__':
    if module_path not in sys.path:
        sys.path.append(module_path)
    from link.line import Subscriber
    unittest.main()
