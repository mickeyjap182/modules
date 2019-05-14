import os, sys, time, unittest

module_path  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class TestArtisan(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_time_change(self):
        artisan = Artisan.create(Traveler)
        self.assertEqual('Traveler', type(artisan).__name__)
        artisan.yesterday()
        self.assertTrue(True)

    def test_stopwatch(self):
        artisan = Artisan.create(StopWatch)
        self.assertEqual('StopWatch', type(artisan).__name__)
        time.sleep(2)
        artisan.stop()
        self.assertEqual(2, artisan.elapsed())
        self.assertEqual(5, len(str(artisan.elapsed(3)))) #2.xxx

if __name__ == '__main__':
    if module_path not in sys.path:
        sys.path.append(module_path)
    from timekeeper.handler import (
        Artisan,
        Traveler,
        StopWatch,
    )
    unittest.main()
