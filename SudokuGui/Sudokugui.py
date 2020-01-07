#coding=utf-8
#owner: IFpop
#time: 2020/1/2


import tkinter as tk
import base64
import os
from icon import JPG_IMG, ICO_IMG
from PIL import Image, ImageTk

root = tk.Tk() 
# 设置窗口大小不可变
root.resizable(width=False, height=False)
root.title("Sudoku")

tmp = open("tmp.ico", "wb+")
tmp.write(base64.b64decode(ICO_IMG))
tmp.close()
root.iconbitmap('tmp.ico')
os.remove("tmp.ico")
tmp = open("tmp.jpg", "wb+")
tmp.write(base64.b64decode(JPG_IMG))
tmp.close()
tmp_image = Image.open("tmp.jpg")
photo = ImageTk.PhotoImage(tmp_image)
label = tk.Label(root, image=photo)
os.remove("tmp.jpg")
label.grid(row=0, column=0, rowspan=12, columnspan=11, sticky='NSEW')
 # 确定按钮
submit_btn = tk.Button(root, text='OK')
submit_btn.grid(row=11, column=9, pady=10, ipadx=30, columnspan=2)
# next按钮
next_btn = tk.Button(root, text='Next>')
next_btn.grid(row=11, column=0, pady=10, ipadx=20, columnspan=2)
root.mainloop()