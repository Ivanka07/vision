#!/bin/python

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from os import listdir

class ImageLabeler(Frame):

    path_to_image_dir = ''
    current_image_path = ''

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

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=2)

        label_1 = Label(self.master, text = "Current Image: " + self.current_image_path, background='#F8ECE0')
        label_2 = Label(self.master, text = "Curent Labels: " + self.current_image_path,background='#F8ECE0')

        label_1.grid(row = 1, column = 0)
        label_2.grid(row=1, column=1)


        self.init_buttons()
        self.init_menu()

    def show_image(self):
        canvas_frame = Frame(self.master, background='#F5BCA9', width=int(self.width*0.6), height=self.height*0.85, padx = 40, pady = 1)
        canvas_frame.grid(row = 2, column=0, sticky="ew")

        current_image_path = self.path_to_image_dir + "/result_pose_2018-3-27-18-35-13.png"
        img = ImageTk.PhotoImage(Image.open(current_image_path))
        print(img.height())

        image = Label(canvas_frame, image=img)
        image.image = img
        image.grid(row = 2, column = 0)



    def init_buttons(self):
        buttons_frame = Frame(self.master, background='#F8ECE0', pady=10, padx=10)
        buttons_frame.grid(row=4, column=0, sticky="ew")

        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)

        but_left = Button(buttons_frame, text='prev image', bg='#92C05D', width=25, height=2, command=self.get_prev_image)
        but_left.grid(row = 0, column = 0)

        but_rigth = Button(buttons_frame, text='next image', bg='#92C05D', width=25, height=2, command=self.get_next_image)
        but_rigth.grid(row=0, column=1)


    def get_prev_image(self):
        print('Getting previous image')

    def get_next_image(self):
        print('Getting next image')

    def init_menu(self):
        menubar = Menu(self.master)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Choose image directory", command=self.choose_image_directory)
        filemenu.add_command(label="Choose label yaml", command=self.choose_lables_file)
        filemenu.add_command(label="Save lables", command=self.choose_lables_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.master.config(menu=menubar)

    def choose_image_directory(self):
        print("hello!")
        self.path_to_image_dir = filedialog.askdirectory(initialdir="/home", title="Select image directory")
        print(self.path_to_image_dir)
        self.get_all_files_in_directory()
        self.show_image()

    def choose_lables_file(self):
            print("chosinmg lable file!")


    def get_all_files_in_directory(self):
        files = listdir(self.path_to_image_dir)
        filtered = list(filter(lambda f: f.endswith('.png') or f.endswith('jpeg') or f.endswith('jpg'), files))
        print(filtered)

if __name__ == '__main__':
    root = Tk()
    im = ImageLabeler(1500, 900, root)
    root.mainloop()
