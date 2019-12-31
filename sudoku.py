#coding=utf-8
#owner: IFpop
#time: 2019/12/20

import sudoku_generate
import sudo_solve
# import test
from copy import deepcopy
import sys
import time

def main():
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
            start = time.time()
            sudoku_solve.Solve_sudo(path)
            end = time.time()
            print("running time: %.4f" % (end-start))

    except ValueError:
        print("please input correct number")
    except IOError:
        print("Error: Not find or open failed!")

main()