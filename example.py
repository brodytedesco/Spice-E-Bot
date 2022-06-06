import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.frame = tk.Frame(self.master)
        self.butnew("SingleSpice", "ONE", SingleSpice)
        self.butnew("Recipes", "TWO", Recipes)
        self.butnew("Recipes", "TWO", Recipes)
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
        
        self.quitButton = tk.Button(self.frame, text = 'Back', width = 25, command = self.close_windows)
        
        # self.butnew("Recipes1", "a" , SingleSpiceDispenser)
        # self.butnew("Recipes1", "a" , SingleSpiceDispenser)
        # self.butnew("Recipes1", "a" , SingleSpiceDispenser)
          

        self.butnew("Recipes", "TWO", Recipes)

        self.label = tk.Label(master, text=f"this is window number {number}")



        self.label.pack()
        self.quitButton.pack()

       

        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    def butnew(self, text, number, _class):
        tk.Button(self.frame, text, width = 25, command = lambda: self.new_window(number, _class)).pack()

    def new_window(self, number, _class):
        self.newWindow = tk.Toplevel(self.master)
        _class(self.newWindow, number)
        

class SingleSpiceDispenser:
    def __init__(self, master, number):
        self.master = master
        self.master.geometry("400x400+400+400")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.label = tk.Label(master, text=f"this is window number {spices[number]}")
        self.label.pack()
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    def butnew(self, text, number, _class):
        tk.Button(self.frame, text = text, width = 25, command = lambda: self.new_window(number, _class)).pack()

    def new_window(self, number, _class):
        self.newWindow = tk.Toplevel(self.master)
        _class(self.newWindow, number)



    def close_windows(self):
        self.master.destroy()

    def butnew(self, text, number, _class):
        tk.Button(self.frame, text = text, width = 25, command = lambda: self.new_window(number, _class)).pack()

    def new_window(self, number, _class):
        self.newWindow = tk.Toplevel(self.master)
        _class(self.newWindow, number)

class Recipes:
    def __init__(self, master, number):
        self.master = master
        self.master.geometry("400x400+400+400")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Back', width = 25, command = self.close_windows)
        self.label = tk.Label(master, text=f"this is window number {number}")
        self.label.pack()
        self.label2 = tk.Label(master, text="THIS IS HERE TO DIFFERENTIATE THIS WINDOW")
        self.label2.pack()
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


spices = {0:"salt", 1:"pepper", 2:"paprika", 3:"tumeric"}

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()



if __name__ == '__main__':
    main()