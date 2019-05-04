import os, sys, unittest

module_path  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class TestCsv(unittest.TestCase):

    def setUp(self):
        self.in_path = os.path.join(module_path, 'tests', 'datahandler', 'input')
        self.out_path = os.path.join(module_path, 'tests', 'datahandler', 'output')
        out_files = self._output_files()
        ret = [os.remove(file) for file in out_files]

    def tearDown(self):
        pass

    def test_file_format(self):
        f = Formatter()

        self.assertEqual(f.delimiter,',')
        self.assertEqual(f.line_sep,'\n')
        self.assertEqual(f.charset,'utf-8')

    def test_read_file(self):
        f = Formatter()
        c = Csv(f)
        headers = ['no', 'first_name', 'family_name']
        contents = c.read(os.path.join(self.in_path, 'comma_sep.csv'), headers=headers)
        # print(contents)
        self.assertEqual(4,len(contents))

    def test_write_file(self):
        f = Formatter()
        c = Csv(f)
        headers = ['rownum', 'code', 'name']
        contents = [
            [1,'C_001', "Apple"],
            [2,'C_002', "Banana"],
            [3,'C_002', "Cytras"],
        ]
        file_path = os.path.join(self.out_path, 'has_header.csv')
        ret = c.write(file_path, contents, headers=headers)

        contents_add = [
            [4,'C_003', "Donuts"],
        ]
        ret = c.write(file_path, contents_add, headers=headers)
        rows = c.read(file_path, headers=headers)
        # print(contents)
        self.assertEqual(4,len(rows))

        # print(contents)
        self.assertTrue(ret)

    def _output_files(self):
        return [os.path.join(self.out_path, name) for name in os.listdir(self.out_path) if os.path.isfile(os.path.join(self.out_path, name)) and name != '.gitkeep']

if __name__ == '__main__':
    if module_path not in sys.path:
        sys.path.append(module_path)
    from datahandler.csvfile import Formatter, Csv
    unittest.main()
