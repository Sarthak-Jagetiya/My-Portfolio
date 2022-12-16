import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('800x550')
root.title('Restaurant Managment System')
root.resizable(0, 0)


def home_page():
    home_frame = tk.Frame(main_frame, bg="#f5ebe0")
    tk.Label(main_frame, text='Home', bg="#f5ebe0",
             font=('Imprint MT Shadow', 25)).pack(pady=5)
    tk.Label(main_frame, text='What do you want to eat today!', bg="#f5ebe0",
             font=('Imprint MT Shadow', 20)).pack(pady=5)
    home_frame.pack()

    image1 = Image.open("download1.jpeg")
    test1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("download4.jpeg")
    test2 = ImageTk.PhotoImage(image2)

    label1 = tk.Label(image=test1, bg="#f5ebe0")
    label1.image = test1
    label2 = tk.Label(image=test2, bg="#f5ebe0")
    label2.image = test2

    img1 = tk.Label(home_frame, image=test1, bg="#f5ebe0")
    img1.image = test1
    img2 = tk.Label(home_frame, image=test2, bg="#f5ebe0")
    img2.image = test2

    img1.grid(row=1, column=0)
    img2.grid(row=2, column=0)
    tk.Label(home_frame, font=("aria", 18, 'bold'),
             text='', bg="#f5ebe0", width=12, fg="blue4").grid(row=8, column=1)

    btn_order = tk.Button(home_frame, bd=3, fg="#f5ebe0", bg="#780000", font=(
        "Sitka Small Semibold", 16, 'bold'), width=10, text="Menu", command=lambda: indicator(menu_indicator, menu_page))
    btn_order.grid(row=2, column=1)


def menu_page():
    menu_frame = tk.Frame(
        main_frame, bg="#f5ebe0")
    tk.Label(menu_frame, text="Menu", font=("Imprint MT Shadow", 25),
             fg="black", bg="#f5ebe0").pack()
    tk.Label(menu_frame, text=" ", font=("Imprint MT Shadow", 25),
             fg="black", bg="#f5ebe0").pack()
    tk.Label(menu_frame, font=("consolas", 15, 'bold',), bg="#f5ebe0",
             text="Dosa - Rs.60/plate", fg="black").pack()
    tk.Label(menu_frame, font=("consolas", 15, 'bold'), bg="#f5ebe0",
             text="Idli - Rs.30/plate", fg="black").pack()
    tk.Label(menu_frame, font=("consolas", 15, 'bold'), bg="#f5ebe0",
             text="Vada - Rs.7/plate", fg="black").pack()
    tk.Label(menu_frame, font=("consolas", 15, 'bold'), bg="#f5ebe0",
             text="Sambhar - Rs.100/plate", fg="black").pack()
    tk.Label(menu_frame, font=("consolas", 15, 'bold'), bg="#f5ebe0",
             text="Rasam - Rs.20/plate", fg="black").pack()
    tk.Label(menu_frame, font=("consolas", 15, 'bold'), bg="#f5ebe0",
             text="Uttapam - Rs.15/plate", fg="black").pack()
    tk.Label(menu_frame, font=("consolas", 15, 'bold'), bg="#f5ebe0",
             text="Payasam - Rs.80/plate", fg="black").pack()
    menu_frame.pack(pady=10)

    btn_order = tk.Button(menu_frame, bd=0, fg="#f5ebe0", bg="#f5ebe0",
                          command=lambda: indicator(order_indicator, order_page))
    btn_order.pack()
    btn_order = tk.Button(menu_frame, bd=3, fg="#f5ebe0", bg="#780000", font=(
        "Sitka Small Semibold", 16, 'bold'), width=10, text="Order", command=lambda: indicator(order_indicator, order_page))
    btn_order.pack()


def order_page():
    order_frame = tk.Frame(main_frame, bd=5, height=370,
                           width=300, bg="#f5ebe0")
    tk.Label(main_frame, text='Order Cart', bg="#f5ebe0",
             font=('Imprint MT Shadow', 25)).pack(pady=15)
    order_frame.pack()

    global dosa
    dosa = tk.StringVar()
    global idli
    idli = tk.StringVar()
    global vada
    vada = tk.StringVar()
    global sambhar
    sambhar = tk.StringVar()
    global rasam
    rasam = tk.StringVar()
    global uttapam
    uttapam = tk.StringVar()
    global payasam
    payasam = tk.StringVar()

    # Label
    lb1_dosa = tk.Label(order_frame, font=("Sitka Display", 15, 'bold'), bg="#f5ebe0",
                        text="Dosa", width=12, fg="black")
    lb1_idli = tk.Label(order_frame, font=("Sitka Display", 15, 'bold'), bg="#f5ebe0",
                        text="Idli", width=12, fg="black")
    lb1_vada = tk.Label(order_frame, font=("Sitka Display", 15, 'bold'), bg="#f5ebe0",
                        text="Vada", width=12, fg="black")
    lb1_sambhar = tk.Label(order_frame, font=("Sitka Display", 15, 'bold'), bg="#f5ebe0",
                           text="Sambhar", width=12, fg="black")
    lb1_rasam = tk.Label(order_frame, font=("Sitka Display", 15, 'bold'), bg="#f5ebe0",
                         text="Rasam", width=12, fg="black")
    lb1_uttapam = tk.Label(order_frame, font=("Sitka Display", 15, 'bold'), bg="#f5ebe0",
                           text="Uttapam", width=12, fg="black")
    lb1_payasam = tk.Label(order_frame, font=("Sitka Display", 15, 'bold'), bg="#f5ebe0",
                           text="Payasam", width=12, fg="black")
    lb1_dosa.grid(row=1, column=0)
    lb1_idli.grid(row=2, column=0)
    lb1_vada.grid(row=3, column=0)
    lb1_sambhar.grid(row=4, column=0)
    lb1_rasam.grid(row=5, column=0)
    lb1_uttapam.grid(row=6, column=0)
    lb1_payasam.grid(row=7, column=0)

    # Entry
    entry_dosa = tk.Entry(order_frame, font=("Sitka Display", 15, 'bold'),
                          textvariable=dosa, bd=4, width=8, bg="#a3b18a")
    entry_idli = tk.Entry(order_frame, font=("Sitka Display", 15, 'bold'),
                          textvariable=idli, bd=4, width=8, bg="#a3b18a")
    entry_vada = tk.Entry(order_frame, font=("Sitka Display", 15, 'bold'),
                          textvariable=vada, bd=4, width=8, bg="#a3b18a")
    entry_sambhar = tk.Entry(order_frame, font=("Sitka Display", 15, 'bold'),
                             textvariable=sambhar, bd=4, width=8, bg="#a3b18a")
    entry_rasam = tk.Entry(order_frame, font=("Sitka Display", 15, 'bold'),
                           textvariable=rasam, bd=4, width=8, bg="#a3b18a")
    entry_uttapam = tk.Entry(order_frame, font=("Sitka Display", 15, 'bold'),
                             textvariable=uttapam, bd=4, width=8, bg="#a3b18a")
    entry_payasam = tk.Entry(order_frame, font=("Sitka Display", 15, 'bold'),
                             textvariable=payasam, bd=4, width=8, bg="#a3b18a")
    entry_dosa.grid(row=1, column=1)
    entry_idli.grid(row=2, column=1)
    entry_vada.grid(row=3, column=1)
    entry_sambhar.grid(row=4, column=1)
    entry_rasam.grid(row=5, column=1)
    entry_uttapam.grid(row=6, column=1)
    entry_payasam.grid(row=7, column=1)

    btn_help = tk.Button(order_frame, bd=0, fg="#f0f0f0",
                         bg="#f5ebe0", text='')
    btn_help.grid(row=9, column=0)

    def Reset():
        entry_dosa.delete(0, 'end')
        entry_idli.delete(0, 'end')
        entry_vada.delete(0, 'end')
        entry_sambhar.delete(0, 'end')
        entry_rasam.delete(0, 'end')
        entry_uttapam.delete(0, 'end')
        entry_payasam.delete(0, 'end')

    btn_reset = tk.Button(order_frame, bd=3, fg="#f5ebe0", bg="#780000", font=(
        "Sitka Small Semibold", 16, 'bold'), width=10, text="Reset", command=Reset)
    btn_reset.grid(row=10, column=0)

    btn_order = tk.Button(order_frame, bd=3, fg="#f5ebe0", bg="#780000", font=(
        "Sitka Small Semibold", 16, 'bold'), width=10, text="Place Order", command=lambda: indicator(bill_indicator, bill_page))
    btn_order.grid(row=10, column=1)


def bill_page():
    bill_frame = tk.Frame(main_frame, bd=5, height=370,
                          width=300, bg="#f5ebe0")
    tk.Label(main_frame, text='Bill', font=(
        'Imprint MT Shadow', 30), bg="#f5ebe0").pack(pady=15)
    bill_frame.pack()

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

    Total_items = 0
    if (a1 > 0):
        Total_items = Total_items+a1
    else:
        a1 = 0
    if (a2 > 0):
        Total_items = Total_items+a2
    else:
        a2 = 0
    if (a3 > 0):
        Total_items = Total_items+a3
    else:
        a3 = 0
    if (a4 > 0):
        Total_items = Total_items+a4
    else:
        a4 = 0
    if (a5 > 0):
        Total_items = Total_items+a5
    else:
        a5 = 0
    if (a6 > 0):
        Total_items = Total_items+a6
    else:
        a6 = 0
    if (a7 > 0):
        Total_items = Total_items+a7
    else:
        a7 = 0

    c1 = 60*a1
    c2 = 30*a2
    c3 = 7*a3
    c4 = 100*a4
    c5 = 20*a5
    c6 = 15*a6
    c7 = 80*a7

    lbl_dosa = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                        text="Dosa \u2192 "+str(a1)+" * " + "60"+" = Rs." + str(c1), bd=6, width=20, fg="black", bg="#f5ebe0")
    lbl_dosa.grid(row=0, column=0)
    lbl_idli = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                        text="Idli \u2192 "+str(a2)+" * " + "30"+" = Rs." + str(c2), bd=6, width=20, fg="black", bg="#f5ebe0")
    lbl_idli.grid(row=1, column=0)
    lbl_vada = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                        text="Vada \u2192 "+str(a3)+" * " + "7"+" = Rs." + str(c3), bd=6, width=20, fg="black", bg="#f5ebe0")
    lbl_vada.grid(row=2, column=0)
    lbl_sambhar = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                           text="Sambhar \u2192 "+str(a4)+" * " + "100"+" = Rs." + str(c4), bd=6, width=20, fg="black", bg="#f5ebe0")
    lbl_sambhar.grid(row=3, column=0)
    lbl_rasam = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                         text="Rasam \u2192 "+str(a5)+" * " + "20"+" = Rs." + str(c5), bd=6, width=20, fg="black", bg="#f5ebe0")
    lbl_rasam.grid(row=4, column=0)
    lbl_uttapam = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                           text="Uttapam \u2192 "+str(a6)+" * " + "15"+" = Rs." + str(c6), bd=6, width=20, fg="black", bg="#f5ebe0")
    lbl_uttapam.grid(row=5, column=0)
    lbl_payasam = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                           text="Payasam \u2192 "+str(a7)+" * " + "80"+" = Rs." + str(c7), bd=6, width=20, fg="black", bg="#f5ebe0")
    lbl_payasam.grid(row=6, column=0)

    lbl_item = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                        text="Total Item(s)", bd=6, width=10, bg='#606c38', borderwidth=2, relief="solid")
    lbl_item.grid(row=7, column=0)
    entry_item = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                          text=Total_items, bd=6, width=10, fg="#f5ebe0", bg="#780000", borderwidth=1, relief="solid")
    entry_item.grid(row=7, column=1)

    lbl_total = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                         text="Total Amount", bd=6, width=10, bg='#606c38', borderwidth=2, relief="solid")
    lbl_total.grid(row=8, column=0)

    Total_bill = c1+c2+c3+c4+c5+c6+c7
    entry_total = tk.Label(bill_frame, font=('consola', 18, 'bold'),
                           text="Rs."+str('%.2f' % Total_bill), bd=3, width=10, fg="#f5ebe0", bg="#780000", borderwidth=1, relief="solid")
    entry_total.grid(row=8, column=1)


def about_page():
    about_frame = tk.Frame(main_frame)
    tk.Label(about_frame, text='About Us',
             font=('Imprint MT Shadow', 30)).pack()
    about_frame.pack(pady=20)

    image1 = Image.open("Screenshot2.jpg")
    test1 = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test1)
    label1.image = test1

    img1 = tk.Label(about_frame, image=test1)
    img1.image = test1
    img1.pack()


def feedback_page():
    feedback_frame = tk.Frame(
        main_frame, bd=5, height=370, width=300, bg="#f5ebe0")
    tk.Label(main_frame, text='Feedback', font=(
        'Imprint MT Shadow', 30), bg="#f5ebe0").pack(pady=15)
    tk.Label(main_frame, width=60, font=20,
             text="How was the food?", fg="#f5ebe0", bg="#780000").pack()
    feedback_frame.pack()

    global val1, val2, val3
    val1 = tk.IntVar()
    val2 = tk.IntVar()
    val3 = tk.IntVar()

    option1 = tk.Checkbutton(feedback_frame, variable=val1, font=20,
                             text="Excellent", command=lambda: check(1), bg="#f5ebe0")
    option1.grid(row=0, column=0)

    option2 = tk.Checkbutton(feedback_frame, variable=val2, text="Average", font=20,
                             command=lambda: check(2), bg="#f5ebe0")
    option2.grid(row=0, column=1)

    option3 = tk.Checkbutton(feedback_frame, variable=val3, font=20,
                             text="Could be better", command=lambda: check(3), bg="#f5ebe0")
    option3.grid(row=0, column=2)

    btn_help = tk.Button(feedback_frame, bd=0,
                         fg="#f0f0f0", bg="#f5ebe0", text='')
    btn_help.grid(row=1, column=1)

    btn_submit = tk.Button(feedback_frame, bd=3, fg="#f5ebe0", bg="#780000", font=(
        "Sitka Small Semibold", 16, 'bold'), width=5, text="Submit", command=lambda: check(4))
    btn_submit.grid(row=2, column=1)


def hide_indicator():
    home_indicator.config(bg='#606c38')
    menu_indicator.config(bg='#606c38')
    about_indicator.config(bg='#606c38')
    order_indicator.config(bg='#606c38')
    bill_indicator.config(bg='#606c38')
    feedback_indicator.config(bg='#606c38')


def check(option):
    if (option == 1):
        val2.set(0)
        val3.set(0)
    elif (option == 2):
        val1.set(0)
        val3.set(0)
    elif (option == 3):
        val2.set(0)
        val1.set(0)
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicator(lb, page):
    hide_indicator()
    lb.config(bg='#fefae0')
    delete_pages()
    page()


# heading
heading_label = tk.Label(text="Desilicious", bg="#000814",
                         fg="#f5ebe0", font=('castellar', 25), width=800, height=2)
heading_label.pack(side=tk.TOP)
# Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri", 33), width="300", height="2"). pack()


# Side frame
options_frame = tk.Frame(
    root, bg='#606c38', highlightbackground='black')

home_btn = tk.Button(options_frame, text='Home',
                     font=('Sitka Small Semibold', 15), fg='#fefae0', bd=0, bg='#606c38', command=lambda: indicator(home_indicator, home_page))
home_btn.place(x=10, y=50)
home_indicator = tk.Label(options_frame, text='', bg='#606c38')
home_indicator.place(x=3, y=50, width=5, height=40)

about_btn = tk.Button(options_frame, text='About',
                      font=('Sitka Small Semibold', 15), fg='#fefae0', bd=0, bg='#606c38', command=lambda: indicator(about_indicator, about_page))
about_btn.place(x=10, y=100)
about_indicator = tk.Label(options_frame, text='', bg='#606c38')
about_indicator.place(x=3, y=100, width=5, height=40)

menu_btn = tk.Button(options_frame, text='Menu',
                     font=('Sitka Small Semibold', 15), fg='#fefae0', bd=0, bg='#606c38', command=lambda: indicator(menu_indicator, menu_page))
menu_btn.place(x=10, y=150)
menu_indicator = tk.Label(options_frame, text='', bg='#606c38')
menu_indicator.place(x=3, y=150, width=5, height=40)

order_btn = tk.Button(options_frame, text='Order',
                      font=('Sitka Small Semibold', 15), fg='#fefae0', bd=0, bg='#606c38', command=lambda: indicator(order_indicator, order_page))
order_btn.place(x=10, y=200)
order_indicator = tk.Label(options_frame, text='', bg='#606c38')
order_indicator.place(x=3, y=200, width=5, height=40)

bill_btn = tk.Button(options_frame, text='Bill',
                     font=('Sitka Small Semibold', 15), fg='#fefae0', bd=0, bg='#606c38', command=lambda: indicator(bill_indicator, bill_page))
bill_btn.place(x=10, y=250)
bill_indicator = tk.Label(options_frame, text='', bg='#606c38')
bill_indicator.place(x=3, y=250, width=5, height=40)


feedback_btn = tk.Button(options_frame, text='Feedback',
                         font=('Sitka Small Semibold', 15), fg='#fefae0', bd=0, bg='#606c38', command=lambda: indicator(feedback_indicator, feedback_page))
feedback_btn.place(x=10, y=300)
feedback_indicator = tk.Label(options_frame, text='', bg='#606c38')
feedback_indicator.place(x=3, y=300, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=120, height=480)

# main frame
main_frame = tk.Frame(root, highlightbackground='black',
                      bg="#f5ebe0", highlightthickness=1)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=500, width=680)
indicator(home_indicator, home_page)
root.mainloop()
