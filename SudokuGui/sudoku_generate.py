#coding=utf-8
#owner: IFpop
#time: 2019/12/19

import numpy as np

# 先确定左上角的数字为5
# 由所述算法可知 对每一行的一位操作变换是基于0,3,6 ,1,4,7, 2,5,8
# 由于每种排列需要生成30种终局，提前将变化方式记录如下
move_way = (
    (0, 3, 6, 1, 4, 7, 2, 5, 8),
    (0, 3, 6, 1, 7, 4, 2, 5, 8),
    (0, 3, 6, 4, 1, 7, 2, 5, 8),
    (0, 3, 6, 4, 7, 1, 2, 5, 8),
    (0, 3, 6, 7, 1, 4, 2, 5, 8),
    (0, 3, 6, 1, 4, 7, 2, 8, 5),
    (0, 3, 6, 1, 4, 7, 5, 2, 8),
    (0, 3, 6, 1, 4, 7, 5, 8, 2),
    (0, 3, 6, 1, 4, 7, 8, 2, 5),
    (0, 3, 6, 1, 4, 7, 8, 5, 2),
    (0, 3, 6, 1, 7, 4, 2, 8, 5),
    (0, 3, 6, 4, 1, 7, 5, 2, 8),
    (0, 3, 6, 4, 7, 1, 5, 8, 2),
    (0, 3, 6, 7, 4, 1, 8, 2, 5),
    (0, 3, 6, 7, 1, 4, 8, 5, 2),
    (0, 6, 3, 1, 4, 7, 2, 5, 8),
    (0, 6, 3, 1, 7, 4, 2, 5, 8),
    (0, 6, 3, 4, 1, 7, 2, 5, 8),
    (0, 6, 3, 4, 7, 1, 2, 5, 8),
    (0, 6, 3, 7, 1, 4, 2, 5, 8),
    (0, 6, 3, 1, 4, 7, 2, 8, 5),
    (0, 6, 3, 1, 4, 7, 5, 2, 8),
    (0, 6, 3, 1, 4, 7, 5, 8, 2),
    (0, 6, 3, 1, 4, 7, 8, 2, 5),
    (0, 6, 3, 1, 4, 7, 8, 5, 2),
    (0, 6, 3, 1, 7, 4, 2, 8, 5),
    (0, 6, 3, 4, 1, 7, 5, 2, 8),
    (0, 6, 3, 4, 7, 1, 5, 8, 2),
    (0, 6, 3, 7, 4, 1, 8, 2, 5),
    (0, 6, 3, 7, 1, 4, 8, 5, 2),
)


class create_sudoku():
    def __init__(self, num):
        # 生成初始的第一行1-9
        self.sudo_num = list(range(1, 10))
        # 将学号移动到前列
        self.sudo_num.remove(5)
        # 记录当前生成的个数
        self.cur = 0
        # 记录终局
        self.perm = []
        self.num = num
        self.create()

    def create(self):
         # print("num:"+str(num))
        while self.cur < self.num:
            # 记录第一行
            self.first_row = [5] + self.sudo_num
            # print(self.first_row)
            self.get_sudoku()
        # self.write2file()

    # def write2file(self):
       # 写入文件
    #   with open("sudoku.txt", "w") as f:
           # print("write file...\n")
    #       length = len(self.perm)
    #       for i in range(length):
    #           for j in range(9):
    #               f.write(("%s\n" % self.perm[i][j]).replace(
    #                    '[', '').replace(']', '').replace(',', ''))
    #           f.write("\n")

    def get_sudoku(self):
        temp_row = []
        for i in move_way:
            # print("Create sudoku "+str(self.cur))
            self.perm.append([])
            # print("current change"+str(i))
            for j in range(9):
                # print("first row:")
                # print(self.first_row)
                # print(i[j], end="")
                temp_row = self.first_row[(
                    9-i[j]):9]+self.first_row[0:(9-i[j])]
                # print(temp_row)
                self.perm[self.cur].append(temp_row)
            # print(self.cur)
            # print(self.perm[self.cur])
            self.cur = self.cur + 1
            if self.cur == self.num:
                break
            self.nextPermutation(self.sudo_num)

    def nextPermutation(self, nums):
        if len(nums) < 2:
            return
        ind = len(nums) - 1
        while nums[ind - 1] >= nums[ind] and ind > 0:
            ind -= 1
        if ind == 0:
            self.traverse(nums, 0, len(nums) - 1)
            return
        else:
            for i in range(len(nums) - 1, ind - 1, -1):
                if nums[i] > nums[ind - 1]:
                    nums[i], nums[ind - 1] = nums[ind - 1], nums[i]
                    self.traverse(nums, ind, len(nums) - 1)
                    return

    def traverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# num = 2
# create_sudoku(num)
