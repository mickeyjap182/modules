import os, sys, unittest

module_path  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.in_path = os.path.join(module_path, 'tests', 'imagehandler', 'input')
        self.out_path = os.path.join(module_path, 'tests', 'imagehandler', 'output')
        out_files = self._output_files()
        ret = [os.remove(file) for file in out_files]

    def tearDown(self):
        pass

    def test_line_graph(self):
        left   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24']
        height = [22,  20,  18,  19,  20,  14,  15.2,16.2,18.3, 19.9, 21.1, 20.8, 21.6, 22.2, 23.1, 21.2, 20.4, 19.9, 18.9, 18.2, 17.9, 17.7, 17.8, 18.0]
        b_high = [60,  70,  90,  88,  75,  67,  67,  78,  46,   78,   46,   57,   74,   68,   69,   62,   87,   68,   89,   57,   54,  65,  76,   65]

        # create multipul graph
        graph = Graph()
        save_path = os.path.join(self.out_path, 'line_plot.pdf')
        graph.draw(Bar(y_label="humi"), left, b_high, color="royalblue")
        graph.draw(Line(title="2019/05/03 temp",x_label="time", y_label="temp"), left, height, color="red", linewidth=5, addtional=True)
        graph.save(graph.fig, os.path.join(self.out_path, 'line_plot.png'))

        self.assertTrue(True)


    def _output_files(self):
        return [os.path.join(self.out_path, name) for name in os.listdir(self.out_path) if os.path.isfile(os.path.join(self.out_path, name)) and name != '.gitkeep']

if __name__ == '__main__':
    if module_path not in sys.path:
        sys.path.append(module_path)
    from imagehandler.graphhandler import Line, Bar, Graph
    unittest.main()
