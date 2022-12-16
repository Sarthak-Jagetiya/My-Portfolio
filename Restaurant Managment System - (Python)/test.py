from tkinter import *
root = Tk()
root.geometry("1000x500")
root.title("Bill Mangement")
root.resizable(False, False)


def Reset():
    entry_dosa.delete(0, END)
    entry_idli.delete(0, END)
    entry_vada.delete(0, END)
    entry_sambhar.delete(0, END)
    entry_rasam.delete(0, END)
    entry_uttapam.delete(0, END)
    entry_payasam.delete(0, END)


def Total():
    try:
        a1 = int(dosa.get())
    except:
        a1 = 0
    try:
        a2 = int(idli.get())
    except:
        a2 = 0
    try:
        a3 = int(vada.get())
    except:
        a3 = 0
    try:
        a4 = int(sambhar.get())
    except:
        a4 = 0
    try:
        a5 = int(rasam.get())
    except:
        a5 = 0
    try:
        a6 = int(uttapam.get())
    except:
        a6 = 0
    try:
        a7 = int(payasam.get())
    except:
        a7 = 0

    # define cost of each item per quantity
    c1 = 60*a1
    c2 = 30*a2
    c3 = 7*a3
    c4 = 100*a4
    c5 = 20*a5
    c6 = 15*a6
    c7 = 80*a7

    lbl_total = Label(f2, font=('aria', 20, 'bold'),
                      text="Total", width=16, fg="lightyellow", bg="black")
    lbl_total.place(x=0, y=50)
    entry_total = Entry(f2, font=('aria', 20, 'bold'),
                        textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_total.place(x=20, y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7
    string_bill = "Rs.", str('%.2f' % totalcost)
    Total_bill.set(string_bill)


Label(text="BILL MANAGEMENT", bg="black", fg="white",
      font=("calibri", 33), width="300", height="2"). pack()

# MENU CARD
f = Frame(root, bg="lightgreen", highlightbackground="black",
          highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)
Label(f, text="Menu", font=("Gabriola", 40, "bold"),
      fg="black", bg="lightgreen").place(x=80, y=0)

Label(f, font=("Lucida Calligraphy", 15, 'bold'),
      text="Dosa.......Rs.60/plate", fg="black", bg="lightgreen"). place(x=10, y=80)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Idli.......Rs.30/plate",
      fg="black", bg="lightgreen"). place(x=10, y=110)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Vada.......Rs.7/plate",
      fg="black", bg="lightgreen"). place(x=10, y=140)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Sambhar....Rs.100/plate",
      fg="black", bg="lightgreen"). place(x=10, y=170)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Rasam......Rs.20/plate",
      fg="black", bg="lightgreen"). place(x=10, y=200)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Uttapam....Rs.15/plate",
      fg="black", bg="lightgreen"). place(x=10, y=230)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Payasam....Rs.80/plate",
      fg="black", bg="lightgreen"). place(x=10, y=260)

# Bill
f2 = Frame(root, bg="lightyellow", highlightbackground="black",
           highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)
Bill = Label(f2, text="Bill", font=('calibri', 20), bg="lightyellow")
Bill.place(x=120, y=10)

# ENTRY WORK
f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()

dosa = StringVar()
idli = StringVar()
vada = StringVar()
sambhar = StringVar()
rasam = StringVar()
uttapam = StringVar()
payasam = StringVar()
Total_bill = StringVar()

# Label
lb1_dosa = Label(f1, font=("aria", 20, 'bold'),
                 text="Dosa", width=12, fg="blue4")
lb1_idli = Label(f1, font=("aria", 20, 'bold'),
                 text="Idli", width=12, fg="blue4")
lb1_vada = Label(f1, font=("aria", 20, 'bold'),
                 text="Vada", width=12, fg="blue4")
lb1_sambhar = Label(f1, font=("aria", 20, 'bold'),
                    text="Sambhar", width=12, fg="blue4")
lb1_rasam = Label(f1, font=("aria", 20, 'bold'),
                  text="Rasam", width=12, fg="blue4")
lb1_uttapam = Label(f1, font=("aria", 20, 'bold'),
                    text="Uttapam", width=12, fg="blue4")
lb1_payasam = Label(f1, font=("aria", 20, 'bold'),
                    text="payasam", width=12, fg="blue4")
lb1_dosa.grid(row=1, column=0)
lb1_idli.grid(row=2, column=0)
lb1_vada.grid(row=3, column=0)
lb1_sambhar.grid(row=4, column=0)
lb1_rasam.grid(row=5, column=0)
lb1_uttapam.grid(row=6, column=0)
lb1_payasam.grid(row=7, column=0)

# Entry
entry_dosa = Entry(f1, font=("aria", 20, 'bold'),
                   textvariable=dosa, bd=6, width=8, bg="lightpink")
entry_idli = Entry(f1, font=("aria", 20, 'bold'),
                   textvariable=idli, bd=6, width=8, bg="lightpink")
entry_vada = Entry(f1, font=("aria", 20, 'bold'),
                   textvariable=vada, bd=6, width=8, bg="lightpink")
entry_sambhar = Entry(f1, font=("aria", 20, 'bold'),
                      textvariable=sambhar, bd=6, width=8, bg="lightpink")
entry_rasam = Entry(f1, font=("aria", 20, 'bold'),
                    textvariable=rasam, bd=6, width=8, bg="lightpink")
entry_uttapam = Entry(f1, font=("aria", 20, 'bold'),
                      textvariable=uttapam, bd=6, width=8, bg="lightpink")
entry_payasam = Entry(f1, font=("aria", 20, 'bold'),
                      textvariable=payasam, bd=6, width=8, bg="lightpink")
entry_dosa.grid(row=1, column=1)
entry_idli.grid(row=2, column=1)
entry_vada.grid(row=3, column=1)
entry_sambhar.grid(row=4, column=1)
entry_rasam.grid(row=5, column=1)
entry_uttapam.grid(row=6, column=1)
entry_payasam.grid(row=7, column=1)

# buttons
btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=(
    "ariel", 16, 'bold'), width=10, text="Reset", command=Reset)
btn_reset.grid(row=9, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=(
    "ariel", 16, 'bold'), width=10, text="Total", command=Total)
btn_total.grid(row=9, column=1)

root.mainloop()
