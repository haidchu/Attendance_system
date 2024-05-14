import tkinter as tk
from tkinter import ttk

class InputFrame(tk.Frame):
    def __init__(self, parent, controller, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible = is_visible

        wrapper_frame = tk.Frame(self)

        self.id_label = ttk.Label(wrapper_frame)
        id = -1 # example id, should get from previous reader
        self.id_label['text'] = "ID"

        self.id_value = ttk.Label(wrapper_frame)
        self.id_value['text'] = id

        self.name_input_lb = ttk.Label(wrapper_frame)
        self.name_input_lb['text'] = "Your name: "
        name = None
        # get name from database using given ID
        # if not found, ask user to type in their name
        self.name_input_text = tk.Entry(wrapper_frame)
        if not name:
            self.name_input_text.focus_set()
        else:
            self.name_input_text.insert(-1, name)

        self.email_input_lb = ttk.Label(wrapper_frame)
        self.email_input_lb['text'] = "Your email: "
        email = None
        # get email from database using given ID
        # if not found, ask user to type in their email
        self.email_input_text = tk.Entry(wrapper_frame)
        if not email:
            self.email_input_text.focus_set()
        else:
            self.email_input_text.insert(-1, email)

        # button to change pages
        open_previous_frame = ttk.Button(wrapper_frame)
        open_previous_frame['text'] = "Previous Frame"
        open_previous_frame['command'] = lambda : [self.set_is_visible(False), controller.show_frame(1)]

        submit_button = ttk.Button(wrapper_frame)
        submit_button['text'] = "Submit"
        submit_button['command'] = lambda : [self.set_is_visible(False), controller.show_frame(3)]

        self.id_label.grid(row=2, column=2, padx=10, pady=10)
        self.id_value.grid(row=2, column=3, padx=10, pady=10)
        self.name_input_lb.grid(row=3, column=2, padx=10, pady=10)
        self.name_input_text.grid(row=3, column=3, padx=10, pady=10)
        self.email_input_lb.grid(row=4, column=2, padx=10, pady=10)
        self.email_input_text.grid(row=4, column=3, padx=10, pady=10)
        open_previous_frame.grid(row=5, column=2, padx=10, pady=10)
        submit_button.grid(row=5, column=3, padx=10, pady=10)

        wrapper_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def set_is_visible(self, is_visible):
        self.is_visible = is_visible
    