from tkinter import *
from tkinter import messagebox
import math, random, os

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Brightway Billing Software")
        bg_color = "#074463"

        title = Label(self.root, text="Brightway Billing Software", bd=12, relief=GROOVE,
                      bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2)
        title.pack(fill=X)

        #================ Variables ================
        # Cosmetics
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()

        # Grocery
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # Cold Drinks
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # Price & Tax
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # Customer Details
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        #================ Customer Detail Frame ================
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details",
                        font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=90, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white",
                          font=("times new roman", 15, "bold"))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=20, textvariable=self.c_name,
                          font="arial 15", bd=7, relief=SUNKEN)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white",
                         font=("times new roman", 15, "bold"))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=20, textvariable=self.c_phone,
                         font="arial 15", bd=7, relief=SUNKEN)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white",
                           font=("times new roman", 15, "bold"))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=20, textvariable=self.search_bill,
                           font="arial 15", bd=7, relief=SUNKEN)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.search_bill_func, width=10, bd=7,
                          font="arial 12 bold")
        bill_btn.grid(row=0, column=6, padx=20, pady=10)

        #================= Cosmetics Frame =================
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics",
                        font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        self.add_item(F2, "Bath Soap", self.soap, 0)
        self.add_item(F2, "Face Cream", self.face_cream, 1)
        self.add_item(F2, "Face Wash", self.face_wash, 2)
        self.add_item(F2, "Hair Spray", self.spray, 3)
        self.add_item(F2, "Hair Gel", self.gell, 4)
        self.add_item(F2, "Body Lotion", self.loshan, 5)

        #================= Grocery Frame =================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery",
                        font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        self.add_item(F3, "Rice", self.rice, 0)
        self.add_item(F3, "Food Oil", self.food_oil, 1)
        self.add_item(F3, "Daal", self.daal, 2)
        self.add_item(F3, "Wheat", self.wheat, 3)
        self.add_item(F3, "Sugar", self.sugar, 4)
        self.add_item(F3, "Tea", self.tea, 5)

        #================= Cold Drinks Frame =================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks",
                        font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=675, y=180, width=325, height=380)

        self.add_item(F4, "Maza", self.maza, 0)
        self.add_item(F4, "Cock", self.cock, 1)
        self.add_item(F4, "Frooti", self.frooti, 2)
        self.add_item(F4, "Thumbs Up", self.thumbsup, 3)
        self.add_item(F4, "Limca", self.limca, 4)
        self.add_item(F4, "Sprite", self.sprite, 5)

        #================= Bill Area =================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=330, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.text_area = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.text_area.yview)
        self.text_area.pack(fill=BOTH, expand=1)

        #================= Button Frame =================
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu",
                        font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold"))
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price,
                       font="arial 10 bold", bd=7, relief=SUNKEN)
        m1_txt.grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold"))
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price,
                       font="arial 10 bold", bd=7, relief=SUNKEN)
        m2_txt.grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drink Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold"))
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price,
                       font="arial 10 bold", bd=7, relief=SUNKEN)
        m3_txt.grid(row=2, column=1, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=820, width=510, height=105)

        total_btn = Button(btn_F, text="Total", command=self.calculate_prices,
                           bg="cadetblue", fg="white", pady=10, width=10, bd=4, font="arial 12 bold")
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        gbill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area,
                           bg="cadetblue", fg="white", pady=10, width=10, bd=4, font="arial 12 bold")
        gbill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_F, text="Clear", command=self.reset_bill,
                           bg="cadetblue", fg="white", pady=10, width=10, bd=4, font="arial 12 bold")
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_F, text="Exit", command=self.Exit_app,
                          bg="cadetblue", fg="white", pady=10, width=10, bd=4, font="arial 12 bold")
        exit_btn.grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()

    #================ Helper Function ================
    def add_item(self, frame, text, var, row):
        Label(frame, text=text, font=("times new roman", 15, "bold"), bg="#074463",
              fg="lightgreen").grid(row=row, column=0, padx=10, pady=10, sticky="w")
        Entry(frame, width=10, textvariable=var, font=("times new roman", 12, "bold"),
              bd=5, relief=SUNKEN).grid(row=row, column=1, padx=10, pady=10)

    #================ Total Calculation ================
    def calculate_prices(self):
        self.c_s_p = self.soap.get()*40
        self.c_fc_p = self.face_cream.get()*120
        self.c_fw_p = self.face_wash.get()*60
        self.c_sp_p = self.spray.get()*180
        self.c_gl_p = self.gell.get()*140
        self.c_lo_p = self.loshan.get()*180
        self.total_cosmetic_price = float(
            self.c_s_p + self.c_fc_p + self.c_fw_p + self.c_sp_p + self.c_gl_p + self.c_lo_p)
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price)*0.05, 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get()*60
        self.g_fo_p = self.food_oil.get()*180
        self.g_d_p = self.daal.get()*240
        self.g_w_p = self.wheat.get()*120
        self.g_s_p = self.sugar.get()*45
        self.g_t_p = self.tea.get()*60
        self.total_grocery_price = float(
            self.g_r_p + self.g_fo_p + self.g_d_p + self.g_w_p + self.g_s_p + self.g_t_p)
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price)*0.1, 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.cd_m_p = self.maza.get()*60
        self.cd_c_p = self.cock.get()*60
        self.cd_f_p = self.frooti.get()*45
        self.cd_th_p = self.thumbsup.get()*60
        self.cd_l_p = self.limca.get()*40
        self.cd_s_p = self.sprite.get()*60
        self.total_cold_drink_price = float(
            self.cd_m_p + self.cd_c_p + self.cd_f_p + self.cd_th_p + self.cd_l_p + self.cd_s_p)
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.cd_tax = round((self.total_cold_drink_price)*0.05, 2)
        self.cold_drink_tax.set("Rs. " + str(self.cd_tax))

        self.total_bill = (
            self.total_cosmetic_price +
            self.total_grocery_price +
            self.total_cold_drink_price +
            self.c_tax + self.g_tax + self.cd_tax
        )

    #================ Welcome Bill ================
    def welcome_bill(self):
        self.text_area.delete('1.0', END)
        self.text_area.insert(END, "\tWelcome to Brightway Retail\n")
        self.text_area.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.text_area.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.text_area.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.text_area.insert(END, "\n====================================")
        self.text_area.insert(END, "\nProduct\t\tQty\tPrice")
        self.text_area.insert(END, "\n====================================")

    #================ Generate Bill Area ================
    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer Details are Required")
            return
        if self.total_bill == 0:
            messagebox.showerror("Error", "No Products Selected")
            return
        self.welcome_bill()

        items = [
            ("Bath Soap", self.soap.get(), self.c_s_p),
            ("Face Cream", self.face_cream.get(), self.c_fc_p),
            ("Face Wash", self.face_wash.get(), self.c_fw_p),
            ("Hair Spray", self.spray.get(), self.c_sp_p),
            ("Hair Gel", self.gell.get(), self.c_gl_p),
            ("Body Lotion", self.loshan.get(), self.c_lo_p),
            ("Rice", self.rice.get(), self.g_r_p),
            ("Food Oil", self.food_oil.get(), self.g_fo_p),
            ("Daal", self.daal.get(), self.g_d_p),
            ("Wheat", self.wheat.get(), self.g_w_p),
            ("Sugar", self.sugar.get(), self.g_s_p),
            ("Tea", self.tea.get(), self.g_t_p),
            ("Maza", self.maza.get(), self.cd_m_p),
            ("Cock", self.cock.get(), self.cd_c_p),
            ("Frooti", self.frooti.get(), self.cd_f_p),
            ("Thumbs Up", self.thumbsup.get(), self.cd_th_p),
            ("Limca", self.limca.get(), self.cd_l_p),
            ("Sprite", self.sprite.get(), self.cd_s_p)
        ]

        for item, qty, price in items:
            if qty != 0:
                self.text_area.insert(END, f"\n{item}\t\t{qty}\t{price}")

        self.text_area.insert(END, "\n------------------------------------")
        self.text_area.insert(END, f"\nCosmetic Tax:\t\t{self.cosmetic_tax.get()}")
        self.text_area.insert(END, f"\nGrocery Tax:\t\t{self.grocery_tax.get()}")
        self.text_area.insert(END, f"\nCold Drink Tax:\t\t{self.cold_drink_tax.get()}")
        self.text_area.insert(END, f"\nTotal Bill:\t\tRs. {self.total_bill}")
        self.text_area.insert(END, "\n------------------------------------")

    #================ Save Bill ================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.text_area.get('1.0', END)
            path = f"G:\\py projects\\Billing Software\\{self.bill_no.get()}.txt"
            with open(path, "w") as f:
                f.write(self.bill_data)
            messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} saved successfully")

    #================ Search Bill ================
    def search_bill_func(self):
        found = False
        for i in os.listdir("G:\\py projects\\Billing Software"):
            if i.split('.')[0] == self.search_bill.get():
                with open(f"G:\\py projects\\Billing Software\\{i}", "r") as f:
                    self.text_area.delete('1.0', END)
                    self.text_area.insert(END, f.read())
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Invalid Bill No")

        #================ Reset Bill ================
    def reset_bill(self):
        op = messagebox.askyesno("Reset", "Do you really want to clear all data?")
        if op > 0:
            # Reset all variables
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)

            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    #================ Exit Application ================
    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


#================ Run the App ================
root = Tk()
obj = Bill_App(root)
root.mainloop()

