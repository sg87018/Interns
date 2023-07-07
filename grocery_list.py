from tkinter import *
from tkinter import ttk 

trae = open(r"C:\Users\SERN_INTERN\Desktop\Python Testing\item_cost.txt", "r")
trae = (trae.read())
print(trae)


gitem = []
gquantity = []
gprice = []

class stuff:
    def __init__(name, item, quantity, price):
        name.item = item
        name.quantity = quantity
        name.price = price
        
def calc():
    t = 0
    for i in range(len(gitem)):
        try:
            qu = float(gquantity[i])
            pr = float(gprice[i])
            answer = qu * pr
            t = answer + t
            
        except ValueError:
            continue
    entry4.delete(0,"end")
    entry4.insert(0, "$" + str(t))

def remove():
    try:
        a = tree.selection()
        print(a)
        ap = (gitem.index(a[0]))
        gitem.remove(a[0])
        gquantity.remove(gquantity[ap])
        gprice.remove(gprice[ap])
        tree.delete(tree.selection())
        calc()
    except IndexError:
        return



root = Tk()
root.title("Listbox")
root.geometry("720x720")

label = Label(root, text = "GROCERY LIST")
label.pack()

tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show = 'headings', height = 5)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Item")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Quantity")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Price")
tree.pack()

label = Label(root, text = "ITEM")
label.pack()
entry1 = Entry(root)
entry1.pack()

label = Label(root, text = "QUANTITY")
label.pack()
entry2  = Entry(root)
entry2.pack()

label = Label(root, text = "PRICE")
label.pack()
entry3 = Entry(root)
entry3.pack()

label = Label(root, text = "TOTAL")
label.pack()
entry4  = Entry(root)
entry4.pack()

def add():
    if entry1.get() == "":
        return
    it = stuff(entry1.get(), entry2.get(), entry3.get())
    for i in range(len(gitem)):
        if gitem[i] == entry1.get():
            tree.delete(entry1.get())
            tree.insert('', i, iid = entry1.get(), values = (entry1.get(), entry2.get(), entry3.get()))
            gquantity[i] = entry2.get()
            gprice[i] = entry3.get()
            calc()
            remove()
            return
    gitem.append(entry1.get())
    gquantity.append(entry2.get())
    gprice.append(entry3.get())
    tree.insert('',END , iid = entry1.get(), values = (entry1.get(), entry2.get(), "$" + entry3.get()))
    calc()
    remove()
 
button1 = Button(root, text="Add", command = add)
button1.pack(pady=5)
             
button2 = Button(root, text="Remove", command = remove)
button2.pack(pady=5)

 
 

root.mainloop()