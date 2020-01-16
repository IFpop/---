#coding=utf-8
#owner: IFpop
#time: 2020/1/2
'''
- 这是界面的主控函数
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from sudoku_faceForm import Ui_MainWindow
from  Get_one_Sudoku import Get_one_Sudoku
import os
import numpy as np  
import random
import sys

def Is_notZero(n):
    if n != 0:
        return True
'''
- 定义一个栈的类，方便存储输入步数，进行返回操作
'''
class MyStack(object):
    def __init__(self):
        self.stack_list = []
        self.count = 0

    # 创建一个栈
    def create_stack(self):
        return self.stack_list

    # 栈中添加值
    def push(self, value):
        self.stack_list.insert(0,value)
        self.count += 1

    #返回栈顶元素值
    def peek(self):
        if self.count:
            return self.stack_list[0]

    # 删除栈顶元素
    def pop(self):
        self.stack_list.pop(0)
        self.count -= 1

    # 返回栈是否为空
    def is_empty(self):
        return self.count == 0

    #打印栈内容
    def print_all(self):
        for sl in self.stack_list:
            print(sl)

'''
- 主窗口界面类
- 用于显示界面，以及各类功能的实现
'''
class Face(QMainWindow):
    hoels = 0
    cur_sudoku_num = 0
    def __init__(self, parent=None):
        #游戏初始等级为1
        '''
        1 —— EASY
        2 —— MEDIUM
        3 —— HARD
        '''
        self.level = 1

        # 九宫格的基准元组
        self.base_points = ((0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6))

        # 使用堆栈实现上一步操作
        self.last = MyStack()

        super(Face, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # 分别设置开始，上一步，下一步文本
        self.ui.start.setText("START")
        self.ui.Done.setText("DONE")
        self.ui.Last.setText("LAST")
        self.ui.Next.setText("NEXT")
        # 初始选择难度为Easy
        self.ui.Level_state.setText("EASY")
        self.ui.Level_state.setReadOnly(True)
        self.ui.Level_state.setStyleSheet(
            "background-color: transparent;")
        self.ui.surplus.setText(str(self.hoels))
        self.ui.surplus.setReadOnly(True)
        self.ui.surplus.setStyleSheet(
            "background-color: transparent;")
        self.setWindowTitle("Sudoku Game")
        # 设置当前时间
        self.GetCurtime()
        # 游戏4种状态 
        '''
        0 —— 尚未开始  happy
        1 —— 开始游戏  come on
        2 —— 成功解出数独 
        3 —— 失败
        '''
        # 初始为0
        self.Put_pic(0)
        
        # 链接按钮功能
        self.ui.start.clicked.connect(self.start_game)
        self.ui.Done.clicked.connect(self.Game_Done)
        self.ui.Last.clicked.connect(self.Recover)
        self.ui.Next.clicked.connect(self.Next_step)

        # 菜单功能
        self.ui.actionEasy.triggered.connect(self.change_easy)
        self.ui.actionMedium.triggered.connect(self.change_medium)
        self.ui.actionHard.triggered.connect(self.change_hard)

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.ui.time.setText("   "+ text)

    '''
    显示当前系统时间
    '''   
    def GetCurtime(self):
        # 设置label属性
        self.ui.time.setStyleSheet("QLabel{color:rgb(0,0,0);font-size:15px;font-weight:bold;font-family:宋体;}")
        # 设置时间
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

    '''
    显示状态的图片
    '''
    def Put_pic(self,game_state):
        # 尚未开始游戏
        if(game_state == 0):
            # 设置状态图
            Pic_state = QMovie("./Pic/Original.gif")
            self.ui.Check_state.setMovie(Pic_state)
            Pic_state.start()
        # 已经开始游戏，还未结束
        elif(game_state == 1):
            Pic_state = QMovie("./Pic/Comeon.gif")
            self.ui.Check_state.setMovie(Pic_state)
            Pic_state.start()
        # 游戏成功
        elif(game_state == 2):
            Pic_state = QMovie("./Pic/Good.gif")
            self.ui.Check_state.setMovie(Pic_state)
            Pic_state.start()
     
    '''
    将难度改为Easy以及level改为1，并在框中显示字符
    '''
    def change_easy(self):
        self.level = 1
        self.ui.Level_state.setText("EASY")
    
    '''
    将难度改为medium以及level改为2，并在框中显示字符
    '''
    def change_medium(self):
        self.level = 2
        self.ui.Level_state.setText("MEDIUM")

    '''
    将难度改为hard以及level改为3，并在框中显示字符
    '''
    def change_hard(self):
        self.level = 3
        self.ui.Level_state.setText("HARD")
    
    '''
    使用按钮进行链接此函数，当第一次点击开始时，会将START改为RESTART
    调用Get_one_sudoku模块中的获取类，得到当前数独，进行界面初始化处理
    并将表格中数据的变化，链接到working函数，进行实时更新空闲个数
    '''
    def start_game(self):
        self.ui.start.setText('RESTART')
        self.Put_pic(1)
        # 用于记录现在界面上的数独
        self.sudoku =  np.array([[0] * 9] * 9, dtype=object)  # 数独的值，包括未解决和已解决的

        self.ui.tableWidget.clearContents()
        # 获取一个数独
        #self.cur_sudoku_num += 1
        # print(self.cur_sudoku_num)
        temp = Get_one_Sudoku(self.level)
        # 用于记录所获取的数独终局
        self.oldsudoku = temp.oldsudoku
        for i in range(9):
            for j in range(9):
                if(temp.sudoku[i][j] != 0):
                    item = QTableWidgetItem(str(temp.sudoku[i][j]))
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget.setItem(i,j,item)
                    self.sudoku[i][j] = temp.sudoku[i][j]
                else:
                     item = QTableWidgetItem("")
                     item.setBackground(QBrush(QColor(0, 255, 0)))
                     self.ui.tableWidget.setItem(i,j,item)

        self.hoels = temp.hoels
        # print(self.hoels)
        self.ui.surplus.setText(str(self.hoels))  # 剩余的空格数
        # 动态更新holes的值
        self.ui.tableWidget.itemChanged.connect(self.working)
        return True

    '''
    此函数用于判断游戏是否结束
    分别判断行、列以及九宫格是否正确
    '''
    def Game_Done(self):
        if(self.hoels > 0):
            QMessageBox.warning(self,"Warning","You haven't finished Sudoku yet")
            return
        # 判断行
        for row in range(9):
            temp_tuple = tuple(self.sudoku[row])
            if len(set(temp_tuple)) != len(temp_tuple):
                self.Put_pic(2)
                QMessageBox.warning(self,"Warning","There are some problems")
        # 判断列
        for col in range(9):
            temp_tuple = tuple(self.sudoku[:,col])
            if len(set(temp_tuple)) != len(temp_tuple):
               self.Put_pic(2)
               QMessageBox.warning(self,"Warning","There are some problems")
        
        # 九宫格
        # 先找到九宫格基准点，也就是3×3数组的左上角的点
        for bp in self.base_points:
            temp_tuple = tuple(self.sudoku[bp[0]:bp[0] + 3, bp[1]:bp[1] + 3].reshape(1, -1)[0])
            if len(set(temp_tuple)) != len(temp_tuple):
               self.Put_pic(2)
               QMessageBox.warning(self,"Warning","There are some problems")

        self.Put_pic(2)
        QMessageBox.warning(self,"Message","Congratulations on your success")

    '''
    此函数用于恢复上一步，用于LAST按钮链接
    通过堆栈，将之前填入的点数存储起来，最后进行恢复
    '''
    def Recover(self):
        row,col = self.last.peek()
        # print(self.last.peek())
        self.last.pop()
        item = QTableWidgetItem("")
        item.setBackground(QBrush(QColor(0, 255, 0)))
        self.ui.tableWidget.setItem(row,col,item)
        self.sudoku[row][col] = self.oldsudoku[row][col]

    '''
    此函数用于提示下一步，用于NEXT按钮链接
    通过oldsudoku以及随机数，随机填入一个未填入的数字，完成提示功能
    开始事先需要判断空格个数是否为0，如果是，那么此时就应该进行游戏判断
    否则，就随机填入一个数
    '''
    def Next_step(self):
        # 没有空格数，所以游戏结束，开始查看总体,这时下一步相当于Done
        if(self.hoels < 1):
            self.Game_Done()
        else:
            num = random.randint(1,self.hoels)  #随机从第一个空格到最后一个空给出随机数，然后将此空补上
            # print(num)
            # print(self.sudoku)
            # print(self.oldsudoku)
            for row in range(9):
                for col in range(9):
                    if(self.sudoku[row][col] == 0):
                        num -= 1
                        if(num == 0):
                            item = QTableWidgetItem(str(self.oldsudoku[row][col]))
                            self.ui.tableWidget.setItem(row,col,item)
                            self.sudoku[row][col] = self.oldsudoku[row][col]
        # self.last.print_all()

    '''
    检测当前填入的值是否正确，被working函数引用，用于动态判断
    '''
    def check_value(self,row,col)->bool:
        bp_r = int(row/3)*3
        bp_c = int(col/3)*3

        # 对行进行判断
        temp_tuple = tuple(filter(Is_notZero,self.sudoku[row]))
        # 不满足数独条件就将空格颜色置为红色
        # print(temp_tuple)
        # print(len(set(temp_tuple)) != len(temp_tuple))
        if len(set(temp_tuple)) != len(temp_tuple):
            return False
       
        # 对列进行判断
        temp_tuple = tuple(filter(Is_notZero,self.sudoku[:,col]))
        # print(temp_tuple)
        # print(len(set(temp_tuple)) != len(temp_tuple))
        if len(set(temp_tuple)) != len(temp_tuple):
            return False
        # 对九宫格进行判断
        temp_tuple = tuple(filter(Is_notZero,self.sudoku[bp_r:bp_r + 3, bp_c:bp_c + 3].reshape(1, -1)[0]))
        # print(temp_tuple)
        # print(len(set(temp_tuple)) != len(temp_tuple))
        if len(set(temp_tuple)) != len(temp_tuple):
            return False
        return True
    
    '''
    这是working函数，当填入数字时会被触发
    触发后，会判断是否填入有效值
    如果填入错误，就会报出错误，并将界面单元格变红，否则就变为白色
    '''
    # 动态计算空的个数
    def working(self,item):
        temp_row = item.row()
        temp_column = item.column()
        # 不是 ""
        if(len(item.text()) != 0):
            # 是个数字
            if item.text().isdigit():
                temp_value = int(item.text())
                # 在1-9范围内，被认为是可输入，而且开始应该是空的
                if temp_value <= 9 and temp_value >= 0:
                    if(self.sudoku[temp_row][temp_column]==0):
                        self.hoels -= 1
                        # 更新剩余的空格数
                        self.ui.surplus.setText(str(self.hoels))
                        self.sudoku[temp_row][temp_column] = int(item.text())
                        self.last.push((temp_row,temp_column))
                        check_bool = self.check_value(temp_row,temp_column)
                        if check_bool:
                            #将颜色改成白色
                            item.setBackground(QBrush(QColor(255, 255, 255)))
                        else:
                            #将颜色改成红色
                            item.setBackground(QBrush(QColor(255, 0, 0)))
                else:
                    # QMessageBox.warning(self,"Warning","Invalid Input")
                    # 这里会将函数调用两次，因为颜色改变
                    # 如果是不在可输入范围内的数字，那么就将其刚刚的输入置为红色
                    item.setBackground(QBrush(QColor(255, 0, 0)))

            # 不是数字，放出提示框，然后将字符串置为初始值
            else:
                QMessageBox.warning(self,"Warning","Invalid Input")
                item.setText("")
                return
        
if __name__ == "__main__":
        app = QApplication(sys.argv)
        myapp = Face()
        myapp.show()
        sys.exit(app.exec_())