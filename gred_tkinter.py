from tkinter import *

root = Tk()

number =Label(root,text="hello world ! ")
goodbye= Label(root ,text="kaiakak")
goodbye.grid(row=0 , column=1)
number.grid(row=0 , column=0)
root.title("Python Tkinter Grid Tutorial")

root.geometry("500x400")
root.minsize(100,200)
root.maxsize(1920,1080)
root.mainloop()