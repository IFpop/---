#coding=utf-8
#owner: IFpop
#time: 2020/1/2

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from sudoku_faceForm import Ui_MainWindow
from  Get_one_Sudoku import Get_one_Sudoku
import os
import numpy as np  
import sys

class Face(QMainWindow):
    hoels = 0
    num = 0
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

        # 数独
        self.sudoku =  np.array([[0] * 9] * 9, dtype=object)  # 数独的值，包括未解决和已解决的

        super(Face, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.ui.start.setText("START")
        self.ui.Ok.setText("DONE")
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
        self.ui.Ok.clicked.connect(self.check_value)

        # 菜单功能
        self.ui.actionEasy.triggered.connect(self.change_easy)
        self.ui.actionMedium.triggered.connect(self.change_medium)
        self.ui.actionHard.triggered.connect(self.change_hard)

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.ui.time.setText("   "+ text)
        
    def GetCurtime(self):
        # 设置label属性
        self.ui.time.setStyleSheet("QLabel{color:rgb(0,0,0);font-size:15px;font-weight:bold;font-family:宋体;}")
        # 设置时间
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

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
        # 游戏失败
        else:
            Pic_state = QPixmap("./Pic/false.png")
            self.ui.Check_state.setPixmap(Pic_state)

    def change_easy(self):
        self.level = 1
        self.ui.Level_state.setText("EASY")

    def change_medium(self):
        self.level = 2
        self.ui.Level_state.setText("MEDIUM")

    def change_hard(self):
        self.level = 3
        self.ui.Level_state.setText("HARD")

    def start_game(self):
        self.ui.start.setText('RESTART')
        self.Put_pic(1)
        self.ui.tableWidget.clearContents()
        # 获取一个数独
        self.num += 1
        # print(self.num)
        temp = Get_one_Sudoku(self.level)
        for i in range(9):
            for j in range(9):
                if(temp.sudoku[i][j] != 0):
                    item = QTableWidgetItem(str(temp.sudoku[i][j]))
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget.setItem(i,j,item)
                else:
                     item = QTableWidgetItem()
                     item.setBackground(QBrush(QColor(0, 255, 0)))
                     self.ui.tableWidget.setItem(i,j,item)

        self.hoels = temp.hoels
        self.ui.surplus.setText(str(self.hoels))  # 剩余的空格数
        # 动态更新holes的值
        self.ui.tableWidget.itemChanged.connect(self.working)

    def check_value(self):
        # 还未完成所有空格
        if(self.hoels != 0):
            QMessageBox.warning(self,"Warning","You haven't finished Sudoku yet")
            for i in range(9):
                for j in range(9):
                    if len(self.ui.tableWidget.item(i,j).text()) == 0:
                        # 将检测到的所有的空的标红
                        item = QTableWidgetItem()
                        item.setBackground(QBrush(QColor(255, 0, 0)))
                        self.ui.tableWidget.setItem(i,j,item)
                        self.Put_pic(1)
                    else:
                       self.sudoku[i][j] = (int(self.ui.tableWidget.item(i,j).text()))
            return
        #print(temp) 
        # 判断行
        for row in range(9):
            temp_tuple = tuple(self.sudoku[row])
            if(set(temp_tuple) != 9):
                # QMessageBox.warning(self,"Message","You are wrong")

                self.Put_pic(3)
                # return


        # 判断列
        for col in range(9):
            temp_tuple = self.sudoku[:,col]
            if(set(temp_tuple) != 9):
                # QMessageBox.warning(self,"Message","You are wrong")
                self.Put_pic(3)
                # return
        
        # 九宫格
        # 先找到九宫格基准点，也就是3×3数组的左上角的点
        for bp in self.base_points:
            vals = list(self.sudoku[bp[0]:bp[0] + 3, bp[1]:bp[1] + 3].reshape(1, -1)[0])
            if(set(vals) != 9):
                # QMessageBox.warning(self,"Message","You are wrong")
                self.Put_pic(3)
                # return

        # 现在该程序尚未结束，就证明游戏成功完成
        self.Put_pic(2)
        QMessageBox.warning(self,"Message","Congratulations on your success")
    
    def check(self,row,col,item):
        bp_r = int(row/3)*3
        bp_c = int(col/3)*3

        # 对行进行判断
        temp_tuple = tuple(self.sudoku[row])
        # 不满足数独条件就将空格颜色置为红色
        if len(set(temp_tuple)) != 9:
            item.setBackground(QBrush(QColor(255, 0, 0)))
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
                    # 其他情况只需要改一下颜色就行
                    item.setBackground(QBrush(QColor(255, 255, 255)))
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