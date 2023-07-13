import unittest
import pyradox


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = pyradox.parse_file("res/sample.txt", game="HoI4", path_relative_to_game=False)
        print(result['technologies']['iw_small_airframe'])


if __name__ == '__main__':
    unittest.main()
