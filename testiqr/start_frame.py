import tkinter as tk
from tkinter import ttk

class StartFrame(tk.Frame):
    def __init__(self, parent, controller, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible = is_visible
        label = ttk.Label(self)
        label['text'] = "Start Frame"
        label.grid(row=0, column=4, padx=10, pady=10)

        open_QR_reader_frame = ttk.Button(self)
        open_QR_reader_frame['text'] = "Next Frame"
        open_QR_reader_frame['command'] = lambda : [self.set_is_visible(False), controller.show_frame(1)]
        open_QR_reader_frame.grid(row=4, column=4, padx=10, pady=10)

    
    def set_is_visible(self, is_visible):
        self.is_visible = is_visible
