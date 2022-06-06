import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.frame = tk.Frame(self.master)
        self.butnew("Single Spices", "ONE", SingleSpice)
        self.butnew("Recipes", "TWO", Recipes)
        self.label = tk.Label(master, text=f"Select your Method!")
        self.label.pack()
        self.frame.pack()

    def butnew(self, text, number, _class):
        tk.Button(self.frame, text = text, width = 25, command = lambda: self.new_window(number, _class)).pack()

    def new_window(self, number, _class):
        self.newWindow = tk.Toplevel(self.master)
        _class(self.newWindow, number)


class SingleSpice:
    def __init__(self, master, number):
        self.master = master
        self.master.geometry("400x400+400+400")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.butnew("pepper", 0, SelectedSpice)
        self.butnew("salt", 1, SelectedSpice)
        self.butnew("paprika", 2, SelectedSpice)
        self.butnew("tumeric", 3, SelectedSpice)
        self.label = tk.Label(master, text=f"Select your spice!")
        self.label.pack(side="top", fill="x", pady=10)
        self.quitButton.pack(side="bottom",pady=20)
        self.frame.pack()



    
    def butnew(self, text, number, _class):
        tk.Button(self.frame, text = text, width = 25, command = lambda: self.new_window(number, _class)).pack(side="top", fill="x", pady=10)

    def new_window(self, number, _class):
        self.newWindow = tk.Toplevel(self.master)
        _class(self.newWindow, number)
       


    def close_windows(self):
        self.master.destroy()


class SelectedSpice:
    def __init__(self, master, number):
        self.number = number
        self.amt = 0
        self.master = master
        self.master.geometry("500x500+400+400")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)

        btn_decrease = tk.Button(self.frame, text="+",command=lambda: self.increase(lbl_value) ,width=5,height=3)
        btn_decrease.pack(side="top", fill="x", pady=10)

        lbl_value = tk.Label(self.frame, text="0",font=7)
        lbl_value.pack(side="top", fill="x", pady=10)

        btn_increase = tk.Button(self.frame, text="-",command=lambda: self.decrease(lbl_value) ,width=5, height=3)
        btn_increase.pack(side="top", fill="x", pady=10)

        btn_submit = tk.Button(self.frame, text="Sumbit",command=lambda: self.extract(lbl_value)  ,width=5, height=3)
        btn_submit.pack(side="top", fill="x", pady=10)
  

        self.label = tk.Label(master, text=f"Specify your quantity of {spices[number]}")
        self.label.pack()
        self.quitButton.pack()
        self.frame.pack()
    

    def increase(self, lbl_value):
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value + 1}"

    def decrease(self, lbl_value):
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value - 1}"

    def extract(self, lbl_value):
        value = int(lbl_value["text"])
        #seb put ur function into here, we pass the spice as a number (0-3 (refer to spices dict)), then the number of tsp's
        spices = (self.number,value)

        print("testmsg"+str(spices[0]))
        # example
        # functionforservos(spices)
        # then somewhere outside this class
        # def servo(spices):
        #   ur fnct
        self.master.destroy()
        
    def butnew(self, text, number, _class):
        tk.Button(self.frame, text = text, width = 25, command = lambda: self.new_window(number, _class)).pack()

    def new_window(self, number, _class):
        self.newWindow = tk.Toplevel(self.master)
        _class(self.newWindow, number)

    def close_windows(self):
        self.master.destroy()

class Recipes:
    def __init__(self, master, number):
        self.master = master
        self.master.geometry("400x400+400+400")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.label = tk.Label(master, text=f"this is window number {number}")
        self.label.pack()
        self.label2 = tk.Label(master, text="THIS IS HERE TO DIFFERENTIATE THIS WINDOW")
        self.label2.pack()
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


spices = {0:"pepper",1:"salt",2:"paprika",3:"tumeric"}

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()