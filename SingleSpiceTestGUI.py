
from pickle import TRUE
import tkinter as tk                # python 3
from tkinter import Frame, font as tkfont
from turtle import left  # python 3

def increase(lbl_value):
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease(lbl_value):
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"
def assign(value1):
    global x,x2
    x = int(value1)
    #x2 = int(value2)
def clear(lbl_value):
    global x
    lbl_value["text"] = "0"
    x=0



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Segoe UI', size=18, weight="bold")#, slant="italic")
        self.button_font =tkfont.Font(family='AngsanaUPC',size=12)
    

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, minsize=300, weight=1)
        container['background']='white'
        container.columnconfigure([0, 1, 2], minsize=100, weight=1)

        self.frames = {}
        for F in (StartPage,SpiceOne,SpiceTwo,SpiceThree,SpiceFour):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=1, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please Choose your Desired Spice", font=controller.title_font,
                        bg='#ffffff')
        #label.place(x=150, y=50, anchor='center')
        label.pack(side="top", fill="x", pady=30, expand=True)
        #label.grid(row=0,column=50,sticky="nsew")
        button1 = tk.Button(self, text="Spice 1",font=controller.button_font,bg='#1E5515', fg='#ffffff',
                            command=lambda: controller.show_frame("SpiceOne"),activebackground='#00A300')
        button1.pack(fill = 'both', expand = True,pady=10)
        button2 = tk.Button(self, text="Spice 2",font=controller.button_font,bg='#B6542C', fg='#ffffff',
                            command=lambda: controller.show_frame("SpiceTwo"),activebackground='#FF4500')
        button2.pack(fill = 'both', expand = True,pady=10)
        button3 = tk.Button(self, text="Spice 3",font=controller.button_font,bg='#B12B24', fg='#ffffff',
                            command=lambda: controller.show_frame("SpiceThree"),activebackground='#44110E', 
                            activeforeground='#ffffff')
        button3.pack(fill = 'both', expand = True,pady=10)
        button4 = tk.Button(self, text="Spice 4",font=controller.button_font,bg='#E3BEE0', fg='#ffffff',
                            command=lambda: controller.show_frame("SpiceFour"),activebackground='#FF0080')
        button4.pack(fill = 'both', expand = True,pady=10)
        


class SpiceOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select Amount of Spice for Spice 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Spice1=tk.Label(self, text="Spice 1", font=20)
        Spice1.pack(side='top',ipadx=10,ipady=10)
        lbl_value = tk.Label(self, text="0",font=7)
        btn_decrease = tk.Button(self, text="-",command=lambda: decrease(lbl_value),width=5,height=3)
        btn_decrease.place(relx=0,rely=0.5)
        lbl_value.place(relx=0.5,rely=0.5)
        btn_increase = tk.Button(self, text="+",command=lambda: increase(lbl_value),width=5,height=3)
        btn_increase.place(relx=0.89,rely=0.5)
        button = tk.Button(self, text="Return",font=10,
                            command=lambda: controller.show_frame("StartPage"))
        button.place(relx=0.15, rely=0.85)
        btn_submit = tk.Button(self, text="Submit",font=10,
                            command=lambda:assign(lbl_value["text"]))
        btn_submit.place(relx=0.7, rely=0.85)
        btn_clear=tk.Button(self, text="Clear",font=10,
                            command=lambda:clear(lbl_value))
        btn_clear.place(relx=0.45, rely=0.85)
        


class SpiceTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select Amount of Spice for Spice 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Spice1=tk.Label(self, text="Spice 2", font=20)
        Spice1.pack(side='top',ipadx=10,ipady=10)
        lbl_value = tk.Label(self, text="0",font=7)
        btn_decrease = tk.Button(self, text="-",command=lambda: decrease(lbl_value),width=5,height=3)
        btn_decrease.place(relx=0,rely=0.5)
        lbl_value.place(relx=0.5,rely=0.5)
        btn_increase = tk.Button(self, text="+",command=lambda: increase(lbl_value),width=5,height=3)
        btn_increase.place(relx=0.89,rely=0.5)
        button = tk.Button(self, text="Return",font=10,
                            command=lambda: controller.show_frame("StartPage"))
        button.place(relx=0.15, rely=0.85)
        btn_submit = tk.Button(self, text="Submit",font=10,
                            command=lambda:assign(lbl_value["text"]))
        btn_submit.place(relx=0.7, rely=0.85)
        btn_clear=tk.Button(self, text="Clear",font=10,
                            command=lambda:clear(lbl_value))
        btn_clear.place(relx=0.45, rely=0.85)
        
class SpiceThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select Amount of Spice for Spice 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Spice1=tk.Label(self, text="Spice 3", font=20)
        Spice1.pack(side='top',ipadx=10,ipady=10)
        lbl_value = tk.Label(self, text="0",font=7)
        btn_decrease = tk.Button(self, text="-",command=lambda: decrease(lbl_value),width=5,height=3)
        btn_decrease.place(relx=0,rely=0.5)
        lbl_value.place(relx=0.5,rely=0.5)
        btn_increase = tk.Button(self, text="+",command=lambda: increase(lbl_value),width=5,height=3)
        btn_increase.place(relx=0.89,rely=0.5)
        button = tk.Button(self, text="Return",font=10,
                            command=lambda: controller.show_frame("StartPage"))
        button.place(relx=0.15, rely=0.85)
        btn_submit = tk.Button(self, text="Submit",font=10,
                            command=lambda:assign(lbl_value["text"]))
        btn_submit.place(relx=0.7, rely=0.85)
        btn_clear=tk.Button(self, text="Clear",font=10,
                            command=lambda:clear(lbl_value))
        btn_clear.place(relx=0.45, rely=0.85)
        
class SpiceFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select Amount of Spice for Spice 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Spice1=tk.Label(self, text="Spice 4", font=20)
        Spice1.pack(side='top',ipadx=10,ipady=10)
        lbl_value = tk.Label(self, text="0",font=7)
        btn_decrease = tk.Button(self, text="-",command=lambda: decrease(lbl_value),width=5,height=3)
        btn_decrease.place(relx=0,rely=0.5)
        lbl_value.place(relx=0.5,rely=0.5)
        btn_increase = tk.Button(self, text="+",command=lambda: increase(lbl_value),width=5,height=3)
        btn_increase.place(relx=0.89,rely=0.5)
        button = tk.Button(self, text="Return",font=10,
                            command=lambda: controller.show_frame("StartPage"))
        button.place(relx=0.15, rely=0.85)
        btn_submit = tk.Button(self, text="Submit",font=10,
                            command=lambda:assign(lbl_value["text"]))
        btn_submit.place(relx=0.7, rely=0.85)
        btn_clear=tk.Button(self, text="Clear",font=10,
                            command=lambda:clear(lbl_value))
        btn_clear.place(relx=0.45, rely=0.85)
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()