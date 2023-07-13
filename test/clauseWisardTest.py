import unittest

import os
import pickle

from clauseWizard import cwparse

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_file = os.path.join(THIS_DIR, 'res/sample.txt')
        parseres_file = os.path.join(THIS_DIR, 'res/list_res')
        with open(test_file, 'r', encoding='UTF-8') as f:
            res = cwparse(f.read(), False)
            print(res)
            with open(parseres_file, 'rb') as resf:
                reslist = pickle.load(resf)
                assert res == reslist
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
