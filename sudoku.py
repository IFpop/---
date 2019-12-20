#-*-coding = utf-8 -*-
#owner: IFpop
#time: 2019/12/20

import sudoku_generate
import sys
import time

try:
    # command=raw_input("please input command\n")
    type = sys.argv[1]
    print(type)
    if type[1] == 'c':
        start = time.process_time()
        num = int(sys.argv[2])
        sudoku_generate.create_sudoku(num)
        end = time.process_time()
        print("running time is %6.4f" % (end-start))

except ValueError:
        print("please input correct number")
except IOError:
    print("Error: 没有找到文件或读取文件失败")