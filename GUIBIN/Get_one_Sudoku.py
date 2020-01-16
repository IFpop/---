#coding: utf-8
#owner: IFpop
#time: 2020/1/3

'''
- 这是获取一个随机数独的模块
'''
import sudoku_generate
import sudo_solve
from copy import deepcopy
import random

'''
- 获取数独类
- 基本思路：
    1. 调用sudo_solve.py随机生成100个数独
    2. 调用随机函数random根据难度设定进行挖洞
    3. 策略：
        猜测次数0~30为简单，30~60为中等，60~无穷为困难
        洞的个数30~40为简单，40~50为中等，50~60为困难
    4. 挖洞时，要时时检测当前数独可求解的个数，超过1代表此洞不能挖
    5. 将挖洞的数独保存在oldsudoku中，方便进行下一步预测以及反悔操作
'''
class Get_one_Sudoku():
    Guess_time = 0
    hoels = 0
    def __init__(self,level):
        # print("level:"+str(level))
        num = random.randint(0,100)  # 从一百个中随机挑一个
        sudokus = sudoku_generate.create_sudoku(120)#生成一百个终局
        # print(num)
        self.oldsudoku = deepcopy(sudokus.perm[num])
        self.sudoku = deepcopy(sudokus.perm[num])
        #print(sudokus.perm[1])
        self.Remove_base_point()
        add_hoels_num = random.randint(0,3)
        while True:
            self.dig_hole()
            if(level == 1):
                if(self.Guess_time < 30 and self.Guess_time>0):  # 猜测次数0~30为简单，30~60为中等，60~无穷为困难
                    break
                if(self.hoels > 30 and self.hoels < 40):
                    break
            elif level == 2:
                if(self.Guess_time < 60 and self.Guess_time>30):  # 猜测次数0~30为简单，30~60为中等，60~无穷为困难
                    break
                if(self.hoels > 40 and self.hoels < 50):
                    break
            elif level == 3:
                if(self.Guess_time>60):  # 猜测次数0~30位简单，30~60为中等，60~无穷为困难
                    break
                if(self.hoels > 50 and self.hoels < 60):
                    break
        # print(add_hoels_num)
        while(add_hoels_num >= 0):
            self.dig_hole()
            add_hoels_num -= 1
    def check_repeate(self): #查看解是否唯一
        ans = sudo_solve.Solve_sudo(self.sudoku)
        # 出现多个解
        if(ans.current_sudoku.count != 1):
            return True
        # 没有出现多个解
        else:
            self.Guess_time = ans.current_sudoku.guess_times

    # 删除九宫格中的点
    def  Remove_base_point(self):
        for i in range(3):
            for j in range(3):
                # 每个方格挖两个
                while True:
                    pos = random.randint(0, 8)
                    row = int(pos/3)+i*3
                    col = int(pos % 3)+j*3
                    temp = self.sudoku[row][col]
                    if self.sudoku[row][col] != 0:
                        self.sudoku[row][col] = 0
                        if self.check_repeate():
                            self.sudoku[row][col] = temp
                        else:
                            self.hoels = self.hoels+1
                            break
                while True:
                    pos = random.randint(0, 8)
                    row = int(pos/3)+i*3
                    col = int(pos % 3)+j*3
                    temp = self.sudoku[row][col]
                    if self.sudoku[row][col] != 0:
                        self.sudoku[row][col] = 0
                        if self.check_repeate():
                            self.sudoku[row][col] = temp
                        else:
                            self.hoels = self.hoels+1
                            break
    
    def dig_hole(self):   #挖洞
        while True:
            pos = random.randint(0, 80)
            row = int(pos/9)
            col = int(pos % 9)
            temp = self.sudoku[row][col]
            if self.sudoku[row][col] != 0:
                self.sudoku[row][col] = 0
                # 如果出现多个解
                if self.check_repeate():
                    self.sudoku[row][col] = temp
                else:
                    self.hoels = self.hoels+1
                    break
                    

# test = Get_one_Sudoku(1)
# print(test.sudoku)

