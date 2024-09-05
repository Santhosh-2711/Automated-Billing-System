from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def _init_(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Sri Balaji Home Needs")
        title=Label(self.root,text="Sri Balaji Home Needs",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#69a0bd",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.almirah=IntVar()
        self.sofaset=IntVar()
        self.diningtable=IntVar()
        self.doublecot=IntVar()
        self.chairs=IntVar()
        self.coffetable=IntVar()
        self.dressingtable=IntVar()
        self.fridge=IntVar()
        self.ironbox=IntVar()
        self.fan=IntVar()
        self.mixergrinder=IntVar()
        self.oven=IntVar()
        self.cooker=IntVar()
        self.geaser=IntVar()
        self.stick=IntVar()
        self.knife=IntVar()
        self.cutter=IntVar()
        self.bottle=IntVar()
        self.glass=IntVar()
        self.plate=IntVar()
        self.hanger=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#69a0bd",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#69a0bd",fg="white").grid(row=0,column=0,padx=15)
        
        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)
        
        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#69a0bd",fg="white").grid(row=0,column=2,padx=10)
        
        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)
        
        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#69a0bd",fg="white").grid(row=0,column=4,padx=10)
        
        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Furniture label frame=================================================================
        Furniture=LabelFrame(self.root,text="Furniture",font=("Arial Black",12),bg="#FFA74F",fg="#6C3483",relief=GROOVE,bd=10)
        Furniture.place(x=5,y=180,height=380,width=325)
        
        item1=Label(Furniture,text="Almirah",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(Furniture,borderwidth=2,width=15,textvariable=self.almirah).grid(row=0,column=1,padx=10)

        item2=Label(Furniture,text="Sofaset",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(Furniture,borderwidth=2,width=15,textvariable=self.sofaset).grid(row=1,column=1,padx=10)

        item3=Label(Furniture,text="Dining table",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(Furniture,borderwidth=2,width=15,textvariable=self.diningtable).grid(row=2,column=1,padx=10)

        item4=Label(Furniture,text="Double cot",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(Furniture,borderwidth=2,width=15,textvariable=self.doublecot).grid(row=3,column=1,padx=10)

        item5=Label(Furniture,text= "Chairs",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(Furniture,borderwidth=2,width=15,textvariable=self.chairs).grid(row=4,column=1,padx=10)

        item6=Label(Furniture,text="Coffetable",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(Furniture,borderwidth=2,width=15,textvariable=self.coffetable).grid(row=5,column=1,padx=10)

        item7=Label(Furniture,text="Dressing table",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(Furniture,borderwidth=2,width=15,textvariable=self.dressingtable).grid(row=6,column=1,padx=10)
        #===================================Electricalappliances=====================================================================================
        Electricalappliances=LabelFrame(self.root,text="Electricalappliances",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#FFA74F",fg="#6C3483")
        Electricalappliances.place(x=340,y=180,height=380,width=325)

        item8=Label(Electricalappliances,text="Fridge",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(Electricalappliances,borderwidth=2,width=15,textvariable=self.fridge).grid(row=0,column=1,padx=10)

        item9=Label(Electricalappliances,text="Ironbox",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(Electricalappliances,borderwidth=2,width=15,textvariable=self.ironbox).grid(row=1,column=1,padx=10)

        item10=Label(Electricalappliances,text="Fan",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(Electricalappliances,borderwidth=2,width=15,textvariable=self.fan).grid(row=2,column=1,padx=10)

        item11=Label(Electricalappliances,text="Mixer grinder",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(Electricalappliances,borderwidth=2,width=15,textvariable=self.mixergrinder).grid(row=3,column=1,padx=10)

        item12=Label(Electricalappliances,text="Microwave oven",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(Electricalappliances,borderwidth=2,width=15,textvariable=self.oven).grid(row=4,column=1,padx=10)

        item13=Label(Electricalappliances,text="Electrical Rice Cooker",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(Electricalappliances,borderwidth=2,width=15,textvariable=self.cooker).grid(row=5,column=1,padx=10)

        item14=Label(Electricalappliances,text="Geaser",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(Electricalappliances,borderwidth=2,width=15,textvariable=self.geaser).grid(row=6,column=1,padx=10)
        #========================================Homeneeds===============================================================================
        hygine=LabelFrame(self.root,text="Homeneeds",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#FFA74F",fg="#6C3483")
        hygine.place(x=677,y=180,height=380,width=325)

        item15=Label(hygine,text="Broom stick",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.stick).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Knife",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.knife).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Vegetable cutter",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.cutter).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Water Bottles",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.bottle).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Glasses",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.glass).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Plates",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.plate).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Hanger",font=("Arial Black",11),bg="#FFA74F",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.hanger).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#FFA74F")
        billarea.place(x=1010,y=188,width=330,height=372)
        
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#FFA74F",fg="#6C3483").pack(fill=X)
        
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#69a0bd",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)
        
        total_Furniture=Label(billing_menu,text="Total Furniture Price",font=("Arial Black",11),bg="#69a0bd",fg="white").grid(row=0,column=0)
        total_Furniture_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)
        
        total_Electricalappliances=Label(billing_menu,text="Total Electricalappliances Price",font=("Arial Black",11),bg="#69a0bd",fg="white").grid(row=1,column=0)
        total_Electricalappliances_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)

        
        total_hygine=Label(billing_menu,text="Total Homeneeds Price",font=("Arial Black",11),bg="#69a0bd",fg="white").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)

        tax_Furniture=Label(billing_menu,text="Furniture Tax",font=("Arial Black",11),bg="#69a0bd",fg="white").grid(row=0,column=2)
        tax_Furniture_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)
        
        tax_Electricalappliances=Label(billing_menu,text="Electricalappliances Tax",font=("Arial Black",11),bg="#69a0bd",fg="white").grid(row=1,column=2)
        tax_Electricalappliances_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)

        
        tax_hygine=Label(billing_menu,text="Homeneeds Tax",font=("Arial Black",11),bg="#69a0bd",fg="white").grid(row=2,column=2)
        tax_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)
        
        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#FFA74F",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#FFA74F",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#FFA74F",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu=self.almirah.get()*25000
    self.no=self.sofaset.get()*30000
    self.la=self.diningtable.get()*20000
    self.ore=self.doublecot.get()*40000
    self.mu=self.chairs.get()*2000
    self.si=self.coffetable.get()*15000
    self.na=self.dressingtable.get()*25000
    total_Furniture_Price=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)          
    self.total_sna.set(str(total_Furniture_Price)+" Rs")
    self.a.set(str(round(total_Furniture_Price*0.05,3))+" Rs")

    self.at=self.fridge.get()*80000
    self.pa=self.ironbox.get()*2000
    self.oi=self.mixergrinder.get()*7500
    self.ri=self.fan.get()*5000
    self.su=self.oven.get()*20000
    self.te=self.geaser.get()*15000
    self.da=self.cooker.get()*4000
    total_Electricalappliances_Price=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)
        
    self.total_gro.set(str(total_Electricalappliances_Price)+" Rs")
    self.b.set(str(round(total_Electricalappliances_Price*0.01,3))+" Rs")

    self.so=self.stick.get()*150
    self.sh=self.knife.get()*250
    self.cr=self.bottle.get()*150
    self.lo=self.cutter.get()*2200
    self.fo=self.glass.get()*150
    self.ma=self.plate.get()*250
    self.sa=self.hanger.get()*350
    
    total_hygine_Price=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)
        
    self.total_hyg.set(str(total_hygine_Price)+" Rs")
    self.c.set(str(round(total_hygine_Price*0.10,3))+" Rs")
    self.total_all_bill=(total_Furniture_Price+
                total_Electricalappliances_Price+
                total_hygine_Price+
                (round(total_Electricalappliances_Price*0.01,3))+
                (round(total_hygine_Price*0.10,3))+
                (round(total_Furniture_Price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO BALAJI HOME NEEDS\n\tPhone-No.8919279035")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.almirah.get()!=0:
        self.txtarea.insert(END,f"almirah\t\t {self.almirah.get()}\t{self.nu}\n")
    if self.sofaset.get()!=0:
        self.txtarea.insert(END,f"sofaset\t\t {self.sofaset.get()}\t{self.no}\n")
    if self.diningtable.get()!=0:
        self.txtarea.insert(END,f"diningtable\t\t {self.diningtable.get()}\t{self.la}\n")
    if self.doublecot.get()!=0:
        self.txtarea.insert(END,f"doublecot\t\t {self.doublecot.get()}\t{self.ore}\n")
    if self.chairs.get()!=0:
        self.txtarea.insert(END,f"chairss\t\t {self.chairs.get()}\t{self.mu}\n")
    if self.coffetable.get()!=0:
        self.txtarea.insert(END,f"coffetable\t\t {self.coffetable.get()}\t{self.si}\n")
    if self.dressingtable.get()!=0:
        self.txtarea.insert(END,f"dressingtable\t\t {self.dressingtable.get()}\t{self.na}\n")
    if self.fridge.get()!=0:
        self.txtarea.insert(END,f"fridge\t\t {self.fridge.get()}\t{self.at}\n")
    if self.ironbox.get()!=0:
        self.txtarea.insert(END,f"ironbox\t\t {self.ironbox.get()}\t{self.pa}\n")
    if self.fan.get()!=0:
        self.txtarea.insert(END,f"fan\t\t {self.fan.get()}\t{self.ri}\n")
    if self.mixergrinder.get()!=0:
        self.txtarea.insert(END,f"mixergrinder\t\t {self.mixergrinder.get()}\t{self.oi}\n")
    if self.oven.get()!=0:
        self.txtarea.insert(END,f"oven\t\t {self.oven.get()}\t{self.su}\n")
    if self.cooker.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t {self.cooker.get()}\t{self.da}\n")
    if self.geaser.get()!=0:
        self.txtarea.insert(END,f"geaser\t\t {self.geaser.get()}\t{self.te}\n")
    if self.stick.get()!=0:
        self.txtarea.insert(END,f"stick\t\t {self.stick.get()}\t{self.so}\n")
    if self.knife.get()!=0:
        self.txtarea.insert(END,f"knife\t\t {self.knife.get()}\t{self.sh}\n")
    if self.cutter.get()!=0:
        self.txtarea.insert(END,f"cutter\t\t {self.cutter.get()}\t{self.lo}\n")
    if self.bottle.get()!=0:
        self.txtarea.insert(END,f"bottle\t\t {self.bottle.get()}\t{self.cr}\n")
    if self.glass.get()!=0:
        self.txtarea.insert(END,f"glass\t\t {self.glass.get()}\t{self.fo}\n")
    if self.plate.get()!=0:
        self.txtarea.insert(END,f"plate\t\t {self.plate.get()}\t{self.ma}\n")
    if self.hanger.get()!=0:
        self.txtarea.insert(END,f"hanger\t\t {self.hanger.get()}\t{self.sa}\n")
        
    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Furniture Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Electricalappliances Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Beauty&Hygine Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.almirah.set(0)
        self.sofaset.set(0)
        self.diningtable.set(0)
        self.doublecot.set(0)
        self.chairs.set(0)
        self.coffetable.set(0)
        self.dressingtable.set(0)
        self.fridge.set(0)
        self.ironbox.set(0)
        self.fan.set(0)
        self.mixergrinder.set(0)
        self.oven.set(0)
        self.cooker.set(0)
        self.geaser.set(0)
        self.stick.set(0)
        self.knife.set(0)
        self.cutter.set(0)
        self.bottle.set(0)
        self.glass.set(0)
        self.plate.set(0)
        self.hanger.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()
            
root=Tk()
obj=Bill_App(root)
root.mainloop()