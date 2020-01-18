import unittest
from sudo_solve import Solve_sudo

Ans = [[[3,6,7,8,9],]]

class MyclassTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sudoku = Solve_sudo("uint_test.txt")

    def test_remove_konw_num(self):
        ret = self.sudoku.remove_konw_num()
        for item in ret:


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_sudo_exclude'))

    runner = unittest.TextTestRunner()
    runner.run(suite)