class IceCreamStand:
    def __init__(self, name, flavors):
        self.name = name
        self.flavors = flavors

    def get_menu(self):
        menu = "Рады видеть вас в нашем кафе  " + self.name + "\n"
        menu += "Мы можем предложить вам следующие вкусы мороженого:\n"
        for flavor in self.flavors:
            menu += "- " + flavor + "\n"
        return menu


import tkinter as tk

my_stand = IceCreamStand("Ice", ['ванильное', 'шоколадное', 'клубничное'])

root = tk.Tk()
root.title("Ice")

menu_label = tk.Label(root, text=my_stand.get_menu())
menu_label.pack()

root.mainloop()