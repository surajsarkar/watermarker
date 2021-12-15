import os.path
import tkinter.font
from tkinter import *
import tkinter.filedialog as file
from PIL import ImageTk
from tkinter import colorchooser


class Ui(Tk):
    def __init__(self, image_writer):
        super().__init__()
        self.image_writer = image_writer
        self.minsize(600, 400)
        self.title("Water marker")
        self.config(padx=20, pady=20)
        self.save_button = ''
        self.text_entry = ''
        self.text_entry_label = ''
        self.upload_button = ''
        self.button_font_config = tkinter.font.Font(size=12, weight='bold')
        self.uploaded_image=''
        self.selected_image = PhotoImage(file='C:/Users/suraj sarkar/Downloads/screenshot.png')
        self.canvas = ''
        self.canvas_image=''
        self.color_of_font=''
        self.new_selected_image=''

        self.btn()

    def btn(self):
        self.canvas = Canvas(self, bg='AliceBlue', width=550)
        self.canvas_image = self.canvas.create_image( 10, 10, image=self.selected_image, anchor=NW )
        self.canvas.grid(column=0, row=0, columnspan=4, rowspan=2)

        self.upload_button = Button(text='⬆ Upload', cursor='hand2', command=self.file_upload, padx='20', pady='10', activebackground='AliceBlue', bg='DeepSkyBlue', fg='honeydew', font=self.button_font_config)
        self.upload_button.grid(column=2, row=3)

        self.save_button = Button(
            text="Mark&Save",
            state='disabled',
            cursor = 'hand2',
            command = self.save,
            padx = '20',
            pady = '10',
            activebackground = 'AliceBlue',
            bg = 'DeepSkyBlue',
            fg = 'honeydew',
            font = self.button_font_config
        )
        self.save_button.grid(column=3, row=3)

        self.text_entry_label = Label(self, anchor='center', text='watermark text', width=20,)
        self.text_entry_label.grid(column=0, row=2)

        self.text_entry = Entry(self, bg='AliceBlue', cursor='pencil', width=20,)
        self.text_entry.grid(column=0, row=3, rowspan=2)

    def file_upload(self):
        self.new_selected_image = file.askopenfilename(parent=self, title='Select Image', filetypes=(("PNG file", "*.png"),("All Files", "*.*") ) )
        self.color_of_font = colorchooser.askcolor()[0]
        self.save_button['state'] = 'normal'
        self.uploaded_image = ImageTk.PhotoImage(file=self.new_selected_image)
        self.canvas.itemconfig(self.canvas_image, image=self.uploaded_image,)

    def save(self):
        text= self.text_entry.get()
        self.image_writer( self.new_selected_image, self.image_saver, text, 20, self.color_of_font )
        self.save_button['state'] = 'disabled'

    def image_saver(self, image, txt):
        f = file.asksaveasfile(mode='w', title='Save', initialfile=f'{txt}_watermarkered.png', defaultextension='.png', filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
        if f:
            path = os.path.abspath(f.name)
            image.save(path)
            image.show()



