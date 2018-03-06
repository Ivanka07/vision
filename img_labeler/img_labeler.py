#!/bin/python

from tkinter import *

class ImageLabeler(Frame):

    def __init__(self, width=400, height=400, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.width = width
        self.height = height

        self.init_window()

    def init_window(self):
        self.master.title('Image labeler')
        self.master.geometry('{}x{}'.format(self.width, self.height))
        self.master.configure(background='#F8ECE0')

        # layout all of the main containers
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=6)
        self.master.grid_rowconfigure(3, weight=1)

        self.master.grid_columnconfigure(0, weight=2)
        self.master.grid_columnconfigure(1, weight=1)
        label_1 = Label(self.master, text = "Hier kommen die Bilder", background='#F8ECE0')
        label_2 = Label(self.master, text = "Hier kommen die Labels",background='#F8ECE0')

        label_1.grid(row = 1, column = 0)
        label_2.grid(row=1, column=1)

        buttons_frame = Frame(self.master, background='#F8ECE0',pady=1)
        buttons_frame.grid(row=4, column=0, sticky="ew")

        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)


#        canvas_frame = Frame(self.master, background='#F5BCA9', width=int(self.width*0.45), height=self.height*0.85, pady=1)
 #       canvas_frame.grid(row = 2, column=0, sticky="ew")

        canvas = Canvas(self.master, width = int(self.width*0.75), height=self.height*0.85)
        img = PhotoImage(file="/home/ivanna/motion_planning_handle.png")
        print(img.height())
        canvas.create_image(10, 10, image=img)
        canvas.grid(row = 2, column=0)

        self.init_buttons(buttons_frame)


    def init_buttons(self, frame):
        but_left = Button(frame, text='prev image', bg='#92C05D', width=25, height=2, command=self.get_prev_image)
        but_left.grid(row = 0, column = 0)

        but_rigth = Button(frame, text='next image', bg='#92C05D', width=25, height=2, command=self.get_next_image)
        but_rigth.grid(row=0, column=1)




    def get_prev_image(self):
        print('Getting previous image')

    def get_next_image(self):
        print('Getting next image')


if __name__ == '__main__':
    root = Tk()
    im = ImageLabeler(1500, 900, root)
    root.mainloop()
