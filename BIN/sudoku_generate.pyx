#coding=utf-8
#owner: IFpop
#time: 2019/12/24

import sys
import time
from libc.stdio cimport FILE, fopen, fclose, fputs, fgets, feof, fputc

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

cdef class create_sudoku:
    cdef FILE* Save_txt  #创建文件类型
    cdef list sudo_num,cur_first_row
    cdef list perm          #记录所有全排列 以5开头
    cdef int cur            #用于生成全排列
    cdef int index          #进行缓存区计数
    cdef char buf[1000200]  #创建缓存区

    def __init__(self,num:int):
        #打开文件句柄
        self.Save_txt = fopen('sudoku.txt', 'w+')
        if self.Save_txt == NULL:
            print("open failed!")
            sys.exit(0)
        
        # 生成初始的第一行1-9
        self.sudo_num = list(range(1, 10))
        # 将学号移动到前列
        self.sudo_num.remove(5)
        #记录当前第一行
        self.cur_first_row = [5]+self.sudo_num
        # 用于生成全排列
        self.cur = 1
        # 初始化全排列
        self.perm = []

        # 初始化缓存区
        self.index = 0

        #计时加运行
        cdef double start_time = time.time()
        self.create(num)
        cdef double end_time = time.time()
        print("running time: %.4f" % (end_time-start_time))

    '''
    将数独以字符串的形式写入缓存区
    '''
    cdef void write2buf(self,sudoku:list,n:int):
        cdef int i
        cdef int j
        if n != 0:
            self.buf[self.index] = 10 # '\n'
            self.index += 1
        for i in range(9):
            for j in range(9):
                if j != 0:
                    self.buf[self.index] = 32  # ' '
                    self.index += 1
                self.buf[self.index] = sudoku[i][j] + 48 # 0
                self.index += 1
            self.buf[self.index] = 10
            self.index += 1
        #print(len(self.buf)) 
    
    '''
    根据第一行生成数独
    '''
    cdef get_sudoku(self,n:int,rows:list):
        # 临时变量存取数独
        cdef list Grid_sudoku = []
        num = n % 30
        for i in move_way[num]:
            Grid_sudoku.append(rows[-i:]+rows[:-i])
        return Grid_sudoku
    
    '''
    递归计算出所有全排列结果
    '''
    cdef permutation(self,list a_row):
        cdef list temp
        if not a_row:
            self.perm.append(list(self.cur_first_row))
            return
        for i in a_row:
            self.cur_first_row[self.cur] = i
            self.cur += 1
            temp = list(a_row)
            temp.remove(i)
            self.permutation(temp)
            self.cur -= 1
    '''
    主控函数
    '''
    cdef create(self,num:int):
        cdef int i
        cdef int tag  #当前全排列
        # 生成所有全排列
        self.permutation(self.sudo_num)
        # 0~num-1
        for i in range(num-1):
            tag = i % 40320 
            # 将数独生成后，写入缓存区
            self.write2buf(self.get_sudoku(i,self.perm[tag]),i)
            # 缓存区已满，输入，然后初始化
            if self.index > 1000000:
                self.buf[self.index] = 0
                fputs(self.buf,self.Save_txt)
                self.index = 0
        tag = num % 40320
        self.write2buf(self.get_sudoku(i,self.perm[tag]), num)
        fputs(self.buf, self.Save_txt)
        fclose(self.Save_txt)