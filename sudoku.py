#coding=utf-8
#owner: IFpop
#time: 2019/12/20

import sudoku_generate
import sudo_solve
from copy import deepcopy
import sys
import time

def print_help()->None:
    print("sudoku.exe [选项] 参数")
    print("选项：")
    print("    -c <数字>\t生成<数字>个数独终局至文件sudoku.txt")
    print("    -s <绝对路径>\t从<绝对路径>中读取数独题目并生成一个可行解至sudoku.txt")
    print("    -h 显示当前帮助信息")

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ['-c', '-s', '-h']:
        print_help()
    else:
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
                sudo_solve.Solve_sudo(path)
            elif cmd[1] == 'h':
                print_help()
        except ValueError:
            print("please input correct number")    
        except IOError:
            print("Error: Not find or open failed!")

main()