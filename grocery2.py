from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Listbox")
root.geometry("720x720")

lb = Listbox(root, height = 10, width = 30)
label = Label(root, text = "GROCERY LIST")
label.pack()
lb.pack(pady=15)

tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show = 'headings', height = 5)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Item")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Quantity")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Price")
tree.pack()

grocery = ["milk", "eggs", "chicken", "bread", "sugar", "tomato"]

for item in grocery:    
    lb.insert(END, item)

lb.insert(3, "cereal")

def additem():
    lb.insert(ANCHOR)
    lb.insert(END, content.get())
    
def addquantity():
    lb.insert(ANCHOR, content.get())
    
def addprice():
    lb.insert(ANCHOR, content.get())
    
def removeitem():
    lb.delete(ANCHOR)
    
label = Label(root, text = "ITEM")
label.pack()
content = StringVar()
entry = Entry(root, textvariable=content).pack()

label = Label(root, text = "QUANTITY")
label.pack()
content = StringVar()
entry  = Entry(root, textvariable=content).pack()

label = Label(root, text = "PRICE")
label.pack()
content = StringVar()
entry  = Entry(root, textvariable=content).pack()

label = Label(root, text = "TOTAL")
label.pack()
content = StringVar()
entry  = Entry(root, textvariable=content).pack()
 
button1 = Button(root, text="Add", command = additem)
button1.pack(pady=5)
             
button2 = Button(root, text="Remove", command = removeitem)
button2.pack(pady=5)

 
 
 
 
 
global my_label
my_label = Label(root, text='')
my_label.pack(pady=5)

root.mainloop()