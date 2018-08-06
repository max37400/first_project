import tkinter
root = tkinter.Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.winfo_toplevel().title("Распределитель онлайн")
root.geometry('{}x{}+5+5'.format(int(w/3),int(h/3)))
root.resizable(width=False, height=False)
b=tkinter.Button(root,activebackground = "red",text="Распределить!")
close = tkinter.Button(root,activebackground='green',text='Закрыть',command = root.destroy)
b.place(x=w/3-100,y=h/3-80)
close.place(x=w/3-100,y=h/3-40)
h=root.winfo_height()
w=root.winfo_width()
root.mainloop()
