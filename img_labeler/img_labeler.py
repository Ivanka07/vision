#!/bin/python

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from os import listdir
from config import CLASSES
from config import BG_COLOR

class ImageLabeler(Frame):

    path_to_image_dir = '/home/ivanna/fa_data/images_0'
    img_label = 'Current image'
    current_image_path = ''
    image_files = list()
    image_index = 0
    current_img_number = 0
    class_val = None

    def __init__(self, width=400, height=400, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.width = width
        self.height = height
        self.class_val = IntVar()

        self.init_window()

    def init_window(self):
        self.master.title('Image labeler')
        self.master.geometry('{}x{}'.format(self.width, self.height))
        self.master.configure(background=BG_COLOR)

        # layout all of the main containers
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=6)
        self.master.grid_rowconfigure(3, weight=1)

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=2)

        label_1 = Label(self.master, textvariable = self.img_label, background='#F8ECE0')
        label_2 = Label(self.master, text = "Curent Labels: " + self.current_image_path,background='#F8ECE0')

        label_1.grid(row = 1, column = 0)
        label_2.grid(row=1, column=1)

        if self.path_to_image_dir is not '':
            self.image_files = get_all_files_in_directory(self.path_to_image_dir)
            self.image_files = sorted(self.image_files)
            self.show_image()


        self.init_buttons()
        self.init_menu()
        self.init_radio_buttons()

    def show_image(self):

        self.current_image_path = self.path_to_image_dir + '/' + self.image_files[self.current_img_number]
        self.img_label = ''
        self.img_label = "Current image " +  str(self.current_image_path)

        canvas_frame = Frame(self.master, background='#F5BCA9', width=int(self.width*0.6), height=self.height*0.85, padx = 40, pady = 1)
        canvas_frame.grid(row = 2, column=0, sticky="ew")
        img_name = Label(canvas_frame, text = str(self.img_label), background='#F5BCA9')
        img_name.grid(row = 1, column = 0 )

        img = ImageTk.PhotoImage(Image.open(self.current_image_path))

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

        if  self.current_img_number>0:
            self.current_img_number -= 1
            self.show_image()

    def get_next_image(self):
        print('Getting next image')
        if len(self.image_files) > self.current_img_number:
            self.current_img_number += 1
            self.show_image()
        print("current class " + str(self.class_val.get()))


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
        self.path_to_image_dir = filedialog.askdirectory(initialdir="/home", title="Select image directory")
        self.image_files = get_all_files_in_directory(self.path_to_image_dir)
        self.image_files = sorted( self.image_files)
        if len(self.image_files)>=1:
            self.show_image()

    def choose_lables_file(self):
            print("work in progress!")

    def store_class(self):
        print("current image " + self.current_image_path)
        print("current class " + str(self.class_val.get()))

    def init_radio_buttons(self):
        buttons = Frame(self.master, background=BG_COLOR)
        buttons.grid(row = 2, column = 2)
        self.class_val.set(1)
        r = -1
        for txt, val in CLASSES:
            r += 1
            Radiobutton(buttons,
                        text=txt,
                        padx=50,
                        variable=self.class_val,
                        command=self.store_class,
                        value=val,
                        background=BG_COLOR,
                        ).grid(row = r, column = 0, pady = 20)




###################### Helpers #########################

def get_all_files_in_directory(path_to_dir):
    files = listdir(path_to_dir)
    image_files = list(filter(lambda f: f.endswith('.png') or f.endswith('jpeg') or f.endswith('jpg'), files))
    return image_files






if __name__ == '__main__':
    root = Tk()
    im = ImageLabeler(1500, 900, root)
    root.mainloop()
