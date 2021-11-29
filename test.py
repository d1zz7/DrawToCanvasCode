from tkinter import *
root = Tk()
root.title('Application Title')
root.geometry('700x700')
wn=Canvas(root, width=700, height=700, bg='white')


wn.create_line(69, 104, 78, 329, width=5, fill="black")
wn.create_line(80, 323, 330, 331, width=5, fill="black")
wn.create_line(329, 330, 308, 98, width=5, fill="black")
wn.create_line(307, 98, 63, 101, width=5, fill="black")
wn.create_line(66, 96, 155, 10, width=5, fill="black")
wn.create_line(153, 11, 304, 98, width=5, fill="black")
wn.create_rectangle(119, 141, 119 + 30, 141 + 30, width=5, fill="black", outline="black")
wn.create_rectangle(259, 259, 259 + 30, 259 + 30, width=5, fill="black", outline="black")
wn.create_rectangle(272, 296, 272 + 30, 296 + 30, width=5, fill="black", outline="black")
wn.create_rectangle(262, 289, 262 + 30, 289 + 30, width=5, fill="black", outline="black")




wn.pack()
root.mainloop()
