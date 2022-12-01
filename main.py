from tkinter import *

# creating a new window and configurations
window = Tk()
window.title("Jackie's First GUI Program")
window.minsize(width=600, height=400)
window.config(padx=10,pady=10)

# labels
my_label = Label(text="Jackie转码ing", font=("Arial", 24, "bold"))
my_label.config(text="Jackie is studying Python")
my_label.grid(column=4, row=0)

# buttons
def action():
    print("I got clicked")
    my_label["text"] = entry.get()
    # my_label.config(text = input.get())

# call action() when clicked
button = Button(text="Click Here to Change the Day", command=action)
button.grid(column=3, row=1)

#spinbox
def spinbox_used():
    #gets the current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_= 0, to=100, width=5, command=spinbox_used)
spinbox.grid(column=4, row=1)

#Scale
#Called with current scale value
def scale_used(value):
    print(value)
scale = Scale(from_= 0, to=100, width=5, command=scale_used)
scale.grid(column=5, row=1)

#Entry
entry = Entry(width=30)
# add some text to begin with
entry.insert(END,string="大龄转码Day 27")
# Gets text in entry
print(entry.get())
entry.grid(column=4, row=2)


#checkbutton
def checkbutton_used():
    # print 1 if on button checked, otherwise 0
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Become Software Engineer?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=4, row=3)
checkbutton.config(padx=10,pady=10)

#Radobutton
def radio_used():
    print(radio_state.get())
#variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Machine Learning", value=1, variable=radio_state, command = radio_used)
radiobutton2 = Radiobutton(text="Data Science", value=2, variable=radio_state, command = radio_used)
radiobutton1.grid(column=4, row=4)
radiobutton2.grid(column=4, row=5)
radiobutton2.config(padx=10,pady=10)

#Listbox
def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
study = ["Pandas","Numpy","Matplotlib","Tkinter"]

for item in study:
    listbox.insert(study.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.grid(column=3, row=7)

#Text
text = Text(height=5, width=30)
#puts cursor in textbox
text.focus()
#add some text to begin with
text.insert(END,"大龄转码Day 27: Button,Text,Scale,Listbox")
#Get current value in textbox at line 1, character 0
print(text.get("1.0",END))
text.grid(column=4, row=7)

window.mainloop()