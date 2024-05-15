import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
from qreader import QReader

class QRReaderFrame(tk.Frame):
    def __init__(self, parent, controller, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible  = is_visible # check if the frame is visible (i.e. on top of other frames)
        self.controller = controller
        label = ttk.Label(self)
        label['text'] = "QR Reader Frame"

        open_previous_frame = ttk.Button(self)
        open_previous_frame['text'] = "Previous Frame"
        open_previous_frame['command'] = lambda : [self.set_is_visible(False), self.controller.show_frame(0)]

        open_next_frame = ttk.Button(self)
        open_next_frame['text'] = "Next Frame"
        open_next_frame['command'] = lambda : [self.set_is_visible(False), self.controller.show_frame(2)]
        
        # initiate Label component to contain camera frame
        self.image_label = ttk.Label(self)

        label.place(relx=0.5, rely=0.1, anchor=tk.N)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        open_previous_frame.place(relx=0.3, rely=0.9, anchor=tk.N)
        open_next_frame.place(relx=0.7, rely=0.9, anchor=tk.N)

        self.reader = QReader(model_size='s')

        # camera frame dimensions
        self.width = 600
        self.height = 400

        # opencv capture with camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.open_camera()

    
    def set_is_visible(self, is_visible):
        self.is_visible = is_visible

    def set_props(self, props):
        self.props = props
    

    def open_camera(self):
        ret, frame = self.cap.read()
        if not ret: return
        if not self.is_visible:
            # not showing the image read from camera
            # to improve performance
            self.image_label.after(10, lambda : self.open_camera())
            self.image_label.configure(image='')
        else:
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
            captured_image = Image.fromarray(cv2.flip(opencv_image, 1))
            photo_image = ImageTk.PhotoImage(image=captured_image) 
            self.image_label.photo_image = photo_image
            self.image_label.configure(image=photo_image)

            # detect QR reader here
            outputs = self.reader.detect_and_decode(frame)
            for data in outputs:
                try:
                    w = self.get_id(data)
                    print(w)
                    self.set_is_visible(False)
                    self.controller.show_frame(2, props={'id':w})
                except:
                    print("not correct qrcode")
            self.image_label.after(10, lambda : self.open_camera())

    def get_id(self, qrcode):
        json_qr = json.loads(qrcode)

        if json_qr['elem']['u']:
            u_value = json_qr['elem']['u']
            after_dot = u_value.split('.')[1]
            peppi_id = int(after_dot)

            return peppi_id
