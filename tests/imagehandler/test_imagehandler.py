import os, sys, unittest

# set import path for environment
if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    if path not in sys.path:
        sys.path.append(path)
from tests.core import Config
from imagehandler.filehandler import Separator

class TestSeparator(unittest.TestCase):

    def setUp(self):
        self.in_path = os.path.join(Config.test_path, 'image', 'input')
        self.out_path = os.path.join(Config.test_path, "image", "output")
        out_files = self._output_files()
        ret = [os.remove(file) for file in out_files]

    def tearDown(self):
        pass

    def test_separate_01(self):
        # input file
        i = Separator(input_file=os.path.join(self.in_path, 'sample.png'))
        # output (3 × 3)separated files.
        i.separate(3, 3, out_file=os.path.join(self.out_path, "split_file_{:010}.png"))
        out_files = self._output_files()
        self.assertEqual(len(out_files), 9)

    def test_separate_02(self):
        # input file
        i = Separator(input_file=os.path.join(self.in_path, 'sample.png'))
        # output (3 × 3)separated files.
        i.separate(2, 5, out_file=os.path.join(self.out_path, "split_file_{:010}.png"))
        out_files = self._output_files()
        self.assertEqual(len(out_files), 10)

    def _output_files(self):
        return [os.path.join(self.out_path, name) for name in os.listdir(self.out_path) if os.path.isfile(os.path.join(self.out_path, name)) and name != '.gitkeep']

if __name__ == '__main__':
    unittest.main()
