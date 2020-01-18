# 个人项目

## 文件结构

```txt
/ Soduku
/ BIN
	/ Coverage_test
	/ TestFile
	/ UnitTest
	/ code
/GUIBIN
	/ Pic
	/ Get_one_Sudoku.py
	/ sudo_solve.py
	/ sudoku.Gui.py
	/ sudoku_faceForm.py
	/ sudoku_faceForm.ui
	/ sudoku_generate.py

```

## 依赖

```bash
- python 3.6.8
- pyqt5
- unittest
- cython
- pyqt5-tools
- opencv-python
- pyinstaller
```

## 数独(无界面)

### `sudoku_generate`编译

在BIN/code目录下运行(保证已经安装好`cython`):

```bash
python setup.py build_ext --inplace
```

### 运行与测试

编译好之后，在BIN/code目录下，使用下面命令进行测试:

+ 生成终局

  ```bash
  python sudoku.py -c 10000
  ```

  终端有如下输出：

  ![1579348276039](https://postimg.cc/SJYVVYP5)

+ 解数独

  在对应目录下,打开`powershell`，键入:

  ```bash
  python sudoku.py -s ../TestFile/test.txt
  ```

  ![1579348736581](https://postimg.cc/tYPRbDfz)

## 数独(有界面)

### 运行

安装好上述依赖以后可直接进行运行，在`GUIBIN/`目录下，打开`Powershell`，键入:

```bash
python sudokuGui.py
```

会出现下面界面：

![1579349080302](https://postimg.cc/hhM4tfPX)

下面是各种状态的情况：

+ 开始游戏

  点击start后，start按钮会变为restart，然后图片发现改变，右上角显示是空格个数，右边左上角显示的是难度。

  ![1578424065129](https://postimg.cc/qzssRPZb)

+ 点击下一步进行补全

  如果点击 Next按钮，那么会帮助你随机填入当前一步。

  ![1578424084453](https://postimg.cc/K19g3x7N)

+ 使用上一步进行恢复

  如果点击Last按钮，那么会撤回之前所走的一步。

  ![1578424103811](https://postimg.cc/4K7nKtxf)

+ 在未完成的情况下，点击DONE

  此时，会爆出提示未完成游戏的提示信息。

  ![1578424244071](https://postimg.cc/30KvDRqt)

+ 完成一局游戏后，如果正确，将会出现如下结果

  ![1578424301099](https://postimg.cc/JGH15mWx)

## `exe`文件

若不想配置环境，可以到下面链接中下载`exe`文件

- [Sudoku](https://pan.baidu.com/s/11LO5OW7sxWbcHaMywkVT2w)

  提取码：`kj8o`

- [SudokuGui](https://pan.baidu.com/s/1Cfe3T4hf3zPnHyku1dFUZw)

  提取码：`92nf`

