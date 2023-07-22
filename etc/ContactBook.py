# from tkinter import *
# from tkinter import messagebox

# root = Tk()
# root.geometry("700x550")
# root.config(bg = "#d3f3f5")
# root.title("pythonGeeks Contact Book")
# root.resizable(0,0)
# contactlist = [
#     ["Sidharth nigam","369854712"],["ratil kourav","521118755627"],
#     ["abinishek nilam","766868687"],["Sakshi gilard","3768724676"],
#     ["konit paull","68736726478676"],["aren patel","4698547898972"],
#     ["Sam sharma","329854712"],    ["jihn nigam","63788923748927"],
#     ["gimch nigam","9887565752"]]

# Name = StringVar()
# Number = StringVar()

# frame = Frame (root)
# frame.pack(side = RIGHT)

# scroll = Scrollbar(frame,orient = VERTICAL)
# select = Listbox(frame,yscrollcommand=scroll.set, font=('Times new roman',16),
#          bg='#f0fffc',width=20,height=20,borderwidth=3,relief="groove")
# scroll.config (command=select.yview)
# scroll.pack(side=RIGHT,fill=Y)
# select.pack(side=LEFT,fill="both",expand=1)

# def Selected():
#     print("hello",len(select.curselection()))
#     if len (select.curselection())==0:
#         messagebox.showerror("Error","please select the name")
#     else:
#         return int(select.curselection()[0])

# def AddContact():
#     if Name.get()!="" and Number.get()!="":
#         contactlist.append([Name.get(),Number.get()])
#         print(contactlist)
#         Select_set()
#         EntryReset()
#         messagebox.showinfo("Confirmation","Succesfully Add New Contact")
#     else:
#         messagebox.showerror("Error","please fill the information")

#  def UpdateDetail():
#      if Name.get()and Number.get():
#          contactlist[Selected()] = [Name.get(),Number.get()]
#          messagebox.showinfo("Confirmation","Succesfully Update contact")
#          EntryReset()
#          Select_set()
#       elif not(Name.get()) and not(Number.get()) and
#                                            not (len(select.curselection())==0):
#          messagebox.showerror("Error","please fill the information")

#  else:
#      if len(select.curselection())==0:
#          messagebox.showerror("Erorr","please select the name and \n press load button")
#      else:
#          message1:""" to load the all information OF \n
#                    selected row press load button  \n .
#                    """

#          messagebox.showerror("error",message1)


# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x550")
root.config(bg="#d3f3f5")
root.title("pythonGeeks Contact Book")
root.resizable(0, 0)

contactlist = [
    ["Sidharth nigam", "369854712"], ["ratil kourav", "521118755627"],
    ["abinishek nilam", "766868687"], ["Sakshi gilard", "3768724676"],
    ["konit paull", "68736726478676"], ["aren patel", "4698547898972"],
    ["Sam sharma", "329854712"], ["jihn nigam", "63788923748927"],
    ["gimch nigam", "9887565752"]
]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16),
                 bg='#f0fffc', width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill="both", expand=1)


def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please select a name")
    else:
        return int(select.curselection()[0])


def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully added a new contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")


def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Successfully updated contact")
        EntryReset()
        Select_set()
    elif not Name.get() and not Number.get() and not len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please fill in the information")
    else:
        if len(select.curselection()) == 0:
            messagebox.showerror(
                "Error", "Please select a name and press the load button")
        else:
            message1 = """To load all the information of the selected row, press the load button."""
            messagebox.showerror("Error", message1)


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


def EntryReset():
    Name.set("")
    Number.set()


Select_set()

Label(root, text="NAME", font=("Times new roman",
      20, "bold"), bg="#d3f3f5").place(x=30, y=20)
Entry(root, font=("Times new roman", 13),
      textvariable=Name, bg='#f0fffc').place(x=120, y=30)

Label(root, text="PHONE NO.", font=("Times new roman",
      20, "bold"), bg="#d3f3f5").place(x=30, y=70)
Entry(root, font=("Times new roman", 13),
      textvariable=Number, bg='#f0fffc').place(x=200, y=80)

Button(root, text="ADD", font=("Times new roman", 12, "bold"), bg="#03fcbe", relief="groove", command=AddContact).place(
    x=120, y=120)
Button(root, text="UPDATE", font=("Times new roman", 12, "bold"), bg="#03fcbe", relief="groove",
       command=UpdateDetail).place(x=200, y=120)

root.mainloop()
