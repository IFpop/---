# -*-coding = utf-8 -*-
#owner: IFpop
#time: 2019/12/20

import sudoku_generate
import sudo_solve
# import test
from copy import deepcopy
import sys
import time

try:
    cmd = sys.argv[1]
    print("cmd:"+cmd)
    # 如果是-c的话。就执行create
    if cmd[1] == 'c':
        # 确定开始时间
        start = time.process_time()
        num = int(sys.argv[2])
        # 开始生成终局
        sudoku_generate.create_sudoku(num)
        # 确定结束时间
        end = time.process_time()
        print("running time is %6.4f" % (end-start))
    elif cmd[1] == 's':
        start = time.process_time()
        # 第二个参数应该是数独文件路径
        path = sys.argv[2]
        # 打开文件
        with open(path, 'r') as f:
            line = f.readline()
            # 做个标记位，测试用
            num = 0
            # 定义一个list记录当前数组
            sudoku = []
            while line:
                if(line[0] != '\n' and num != 9):
                    # 将每一行转成数字
                    line = [int(i) for i in line if str.isdigit(i)]
                    # print(line)
                    sudoku.append(deepcopy(line))
                    # print(num)
                    num += 1
                    line = f.readline()
                # 已经收集了一个数独
                elif num == 9 or line[0] == '\n':
                    line = f.readline()
                    num = 0
                    sudo = sudo_solve.Solve_sudo(sudoku)
                    # sudo = test.Solve_sudo(sudoku)
                    print(u"完成，猜测了%s次" % sudo.guess_times)
                    print(sudo.value)
                    sudoku = []
            # 最后一个
            sudo = sudo_solve.Solve_sudo(sudoku)
            # sudo = test.Solve_sudo(sudoku)
            print(u"完成，猜测了%s次" % sudo.guess_times)
            end = end = time.process_time()
            print(sudo.value)
            print("running time is %6.4f" % (end-start))


except ValueError:
    print("please input correct number")
except IOError:
    print("Error: Not find or open failed!")
