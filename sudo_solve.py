# -*-coding=utf-*-
#owner: IFpop
#time: 2019/12/21
# reference: u"杨仕航" http://yshblog.com/blog/74

import numpy as np
from queue import Queue, LifoQueue
from copy import deepcopy


class Recorder:
    point = None  # 进行猜测的点
    point_index = 0  # 猜测候选列表使用的值的索引
    value = None  # 回溯记录的值


class Solve_sudo:
    def __init__(self, data):
        # 将data进行整理
        sudoku = np.array(data)

        # 数据初始化(二维的object数组)
        self.value = np.array([[0] * 9] * 9, dtype=object)  # 数独的值，包括未解决和已解决的
        self.new_points = Queue()  # 先进先出，新解（已解决值）的坐标
        self.recorder = LifoQueue()  # 先进后出，回溯器
        self.guess_times = 0  # 猜测次数

        # 九宫格的基准列表
        self.base_points = [[0, 0], [0, 3], [0, 6], [
            3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

        # 对数独进行处理
        for row in range(9):
            for col in range(9):
                if sudoku[row][col]:  # 如果是已确定点
                    self.value[row][col] = int(sudoku[row][col])
                    # 新的确认的值添加到列表中，以便遍历
                    self.new_points.put((row, col))
                else:
                    self.value[row][col] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # print(self.value)

    def sudo_exclude(self):
        type_same = True
        type_one = True

        while type_same:
            while type_one:
                # 剔除数字
                while not self.new_points.empty():
                    point = self.new_points.get()  # 先进先出
                    self.cut_num(point)

                # 检查List里值为单个数字的情况，如有新answer则加入new_points Queue，立即cut_num
                type_one = self.check_one_possible()

            # 检查同行或列的情况
            type_same = self.check_same_num()
            type_one = True

    # 解题
    def solve(self):
        # 第一次解题，排除法
        self.sudo_exclude()

    def cut_num(self, point):
        # 获取该点的横纵列坐标
        row, col = point
        # 通过坐标获取对应值
        val = self.value[row, col]

        # 检查行
        for i, item in enumerate(self.value[row]):
            if(isinstance(item, list)):
                # 统计该点在该行出现的次数
                if(item.count(val)):
                    item.remove(val)  # 移除
                    # 判断移除后，是否剩下一个元素
                    if(len(item) == 1):
                        self.new_points.put((row, i))  # 添加该坐标到已解决
                        self.value[row][i] = item[0]
        # 检查列
        for i, item in enumerate(self.value[:, col]):
            if isinstance(item, list):
                if item.count(val):
                    item.remove(val)

                    # 判断移除后，是否剩下一个元素
                    if len(item) == 1:
                        self.new_points.put((i, col))
                        self.value[i][col] = item[0]
        # 检查九宫格
        # 先找到九宫格基准点，也就是3×3数组的左上角的点
        bp_row, bp_col = map(lambda x: x // 3 * 3, point)
        # print(bp_row, bp_col)
        # 在3×3的矩阵里进行排除
        for m_r, row in enumerate(self.value[bp_row:bp_row + 3, bp_col:bp_col + 3]):
            for m_c, item in enumerate(row):
                if(isinstance(item, list)):
                    if(item.count(val)):
                        item.remove(val)

                        # 判断移除后
                        if len(item) == 1:
                            r = bp_row + m_r
                            c = bp_col + m_c
                            self.new_points.put((r, c))
                            self.value[r][c] = item[0]

    # 对于一类可直接确定其他行，列或九宫格中没有的，可直接确定该点
    def check_one_possible(self):
        # 同一行只有一个数字的情况
        for row in range(9):
            # 只取出的是这一行是list格子
            vals = list(filter(lambda x: isinstance(x, list), self.value[row]))
            # print(val) #得到该行的所有可能性的二维数组
            for col, item in enumerate(self.value[row]):
                if(isinstance(item, list)):
                    for value in item:  # 对其中的每个元素判断，如果只出现一次则确定
                        if(sum(map(lambda x: x.count(value), vals)) == 1):
                            self.value[row][col] = value
                            self.new_points.put((row, col))
                            return True
        # 对于列
        for col in range(0, 9):
            vals = list(
                filter(lambda x: isinstance(x, list), self.value[:, col]))

            for row, item in enumerate(self.value[:, col]):
                if(isinstance(item, list)):
                    for value in item:
                        if(sum(map(lambda x: x.count(value), vals)) == 1):
                            self.value[row][col] = value
                            self.new_points.put((row, col))
                            return True

        # 对于九宫格
        for row, col in self.base_points:
            # reshape: 3x3 改为1维数组
            vals = list(filter(lambda x: isinstance(x, list),
                               self.value[row:row + 3, col:col + 3].reshape(1, -1)[0]))
            for m_r, rows in enumerate(self.value[row:row + 3, col:col + 3]):
                for m_c, item in enumerate(rows):
                    if(isinstance(item, list)):
                        for value in item:
                            if(sum(map(lambda x: x.count(value), vals)) == 1):
                                self.value[row + m_r, col + m_c] = value
                                self.new_points.put((row + m_r, col + m_c))
                                return True

    # 九宫格内同行列隐性排除
    def check_same_num(self):
        for bp_r, bp_c in self.base_points:
            block = self.value[bp_r:bp_r + 3, bp_c:bp_c + 3]

            # 判断数字1~9在该九宫格的分布情况,reshape变为一维
            _data = block.reshape(1, -1)[0]
            for i in range(1, 10):
                result = map(lambda x: 0 if not isinstance(x[1], list) else x[0] + 1 if x[1].count(i) else 0,
                             enumerate(_data))
                result = list(filter(lambda x: x > 0, result))
                r_count = len(result)

                if r_count in [2, 3]:
                    # 2或3个元素才有可能同一行或同一列
                    rows = list(map(lambda x: (x - 1) // 3, result))
                    cols = list(map(lambda x: (x - 1) % 3, result))

                    if len(set(rows)) == 1:
                        # 同一行，去掉其他行的数字
                        result = list(
                            map(lambda x: bp_c + (x - 1) % 3, result))
                        row = bp_r + rows[0]

                        for col in range(0, 9):
                            if not col in result:
                                item = self.value[row, col]
                                if isinstance(item, list):
                                    if item.count(i):
                                        item.remove(i)

                                        # 判断移除后，是否剩下一个元素
                                        if len(item) == 1:
                                            self.new_points.put((row, col))
                                            # Logger.debug(
                                            # f'block compare row: answer={self.value[row, col]} at {(row, col)}')
                                            self.value[row, col] = item[0]
                                            return True

                    elif len(set(cols)) == 1:
                        # 同一列
                        result = list(
                            map(lambda x: bp_r + (x - 1) // 3, result))
                        col = bp_c + cols[0]

                        for row in range(0, 9):
                            if not row in result:
                                item = self.value[row, col]
                                if isinstance(item, list):
                                    if item.count(i):
                                        item.remove(i)

                                        # 判断移除后，是否剩下一个元素
                                        if len(item) == 1:
                                            self.new_points.put((row, col))
                                            # Logger.debug(
                                            # f'block compare col: answer={self.value[row, col]} at {(row, col)}')
                                            self.value[row, col] = item[0]
                                            return True
