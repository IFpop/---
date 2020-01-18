import unittest
from sudo_solve import Solve_sudo
from copy import deepcopy

'''
这是测试单元测试函数，将预计结果从ans.txt中提取出来，存入Ans中，
使用unittest进行单元测试，对结果进行比较 
'''
Ans = []
with open("ans.txt", 'r') as f:
    line = f.readline()
    cur_row = 0  #记录当前是否是第九行
    temp = []
    while line:
        if(line[0] != '\n' and cur_row != 9):
            line = [int(i) for i in line if str.isdigit(i)]
            temp.append(deepcopy(line))
            cur_row += 1
            line = f.readline()
        # 已经收集了一个数独
        elif cur_row == 9 or line[0] == '\n':
            line = f.readline()
            Ans.append(temp)
            cur_row = 0
            temp = []
    Ans.append(temp)

num = 0
class MyclassTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sudoku = Solve_sudo(str(num)+".txt")

    def test_remove_konw_num(self):
        ret = self.sudoku.remove_konw_num()
        # print(ret)
        # print(Ans[num])
        self.assertEqual(ret,Ans[num]) 


def start():
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_remove_konw_num'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    for i in range(12):
        print(i)
        num = i
        start()