from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import right
from tkinter import messagebox
from PIL import Image,ImageTk   #pip3 install pillow
import random,os
import tempfile
from time import strftime

def man():
 win=Tk()
 app=Login(win)
 win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry('350x500+550+80')
        self.root.title(' L O G I N ')
        self.root.resizable(0,0)
        j=0
        r=10
        for i in range(100):
            c=str(222222+r)
            Frame(self.root,width=10,height=500,bg="#"+c).place(x=j,y=0)   
            j=j+10                                                  
            r=r+1

        Frame(self.root,width=250,height=400,bg='white').place(x=50,y=50)


        l1=Label(self.root,text='Username',bg='white')
        l=('Consolas',13)
        l1.config(font=l)
        l1.place(x=80,y=200)

#e1 entry for username entry
        e1=Entry(self.root,width=20,border=0)
        l=('Consolas',13)
        e1.config(font=l)
        e1.place(x=80,y=230)

#e2 entry for password entry
        e2=Entry(self.root,width=20,border=0,show='*')
        e2.config(font=l)
        e2.place(x=80,y=310)


        l2=Label(self.root,text='Password',bg='white')
        l=('Consolas',13)
        l2.config(font=l)
        l2.place(x=80,y=280)

        Frame(self.root,width=180,height=2,bg='#141414').place(x=80,y=332)
        Frame(self.root,width=180,height=2,bg='#141414').place(x=80,y=252)
        
        imagea=Image.open("C:\Python Programs\Tkinker programs\Billing Software\images\log.jpg")
        imagea = imagea.resize((121,137),Image.ANTIALIAS)
        self.photoimga=ImageTk.PhotoImage(imagea)
        label1 = Label(self.root,image=self.photoimga,border=0,justify=CENTER)
        label1.place(x=115,y=50)


#Command
        def cmd():
            if e1.get()=="" or e2.get()=="":
                messagebox.showerror("Error", "All fields required")
            elif e1.get()=='admin' and e2.get()=='admin':
                messagebox.showinfo("Success", "Welcome to Billing Software")
                billing_software(self)  

                
         
            else:
                messagebox.showwarning("Invalid","Invalid Username or Password")


#Button_with hover effect
        def bttn(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = ecolor #ffcc66
                myButton1['foreground']= lcolor  #000d33

            def on_leavea(e):
                myButton1['background'] = lcolor
                myButton1['foreground']= ecolor

            myButton1 = Button(self.root,text=text,width=20,height=2,fg=ecolor,border=0,bg=lcolor,activeforeground=lcolor,activebackground=ecolor,command=cmd)
                  
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)

        bttn(100,375,'L O G I N','white','#994422')

        def billing_software(self):
            self.new_window=Toplevel(self.root)
            self.app=Bill_App(self.new_window)

    






class Bill_App:
     def __init__(self,root):
         self.root=root
         self.root.state('zoomed')
         self.root.title("Billing Software")

     #     =================Variable==========================
         self.c_name=StringVar()
         self.c_phon=StringVar()
         self.bill_no=StringVar()
         z=random.randint(1000,9999)
         self.bill_no.set(z)
         self.c_email=StringVar()
         self.search_bill=StringVar()
         self.product=StringVar()
         self.prices=IntVar()
         self.qty=IntVar()
         self.sub_total=StringVar()
         self.tax_input=StringVar()
         self.total=StringVar()


         #Product Categories List
         self.Category=["Select Option","Clothing","Lifestyle","Mobiles","Restaurant"]

         #SubCatClothing
         self.SubCatClothing=["Pants","T-Shirt","Shirt"]
         self.pant=["Levis","Loto","Mufti","Denim"]
         self.price_levis=5000
         self.price_loto=700
         self.price_mufti=400
         self.price_denim=2000

         self.tshirt=["US Polo","Roaster","Ginny Jonny"]
         self.price_uspolo=1500
         self.price_roaster=900
         self.price_ginnyjonny=1200

         self.shirt=["Peter England","Louis Phillipe","Park Avenue"]
         self.price_peter=2100
         self.price_louis=2400
         self.price_park=1700

        
         #SubCatLifestyle
         self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]

         self.bathsoap = ["LifeBuoy","Lux","Santoor","Peers"]
         self.price_life=50
         self.price_lux=70
         self.price_santoor=100
         self.price_peers=120

         self.facecream=["Fair & Lovely","Ponds","Olay","Garnier"]
         self.price_fair=70
         self.price_ponds=60
         self.price_olay=90
         self.price_garnier=85


         self.hairoil=["Parachute","Jasmin","Bajaj"]
         self.price_para=25
         self.price_jasmin=22
         self.price_bajaj=30

         #SubCatMobiles
         self.SubCatMobiles=["Iphone","OnePlus","Samsung","Realme","Xiaome"]

         self.iphone = ["Iphone X","Iphone_11","Iphone_12"]
         self.price_ix=40000
         self.price_i11=60000
         self.price_i12=85000


         self.oneplus = ["OnePlus 5","OnePlus 5T","OnePlus 6"]
         self.price_one5=20000
         self.price_one5t=25000
         self.price_one6=40000

         self.samsung=["Samsung M16","Samsung M12","Samsung M21"]
         self.price_sm16=16000
         self.price_sm12=11000
         self.price_sm21=18000
         
         self.realme=["Realme 13Pro","Realme 13","Realme 12"]
         self.price_real13p=25000
         self.price_real13=22000
         self.price_real12=30000

         self.xiome=["Redme 11","Redme 12","Redme 11 Pro"]
         self.price_r11=11000
         self.price_r12=12000
         self.price_r11pro=9000

         #SubCatRestaurant
         self.SubCatRestaurant=["Veg","Non Veg","Roti","Rice","Water"]
         self.veg=["Palak Paneer","Paneer Chilli","Veg Biryani"]
         self.price_pp=120
         self.price_pac=125
         self.price_b=130

         self.nonveg=["Chicken Tikka","Mutton Mughalae","Chicken Dum Biryani"]
         self.price_ct=130
         self.price_mm=190
         self.price_cb=150

         self.roti=["Plain Roti","Butter Roti","Naan","Tandoori Roti"]
         self.price_pr=5
         self.price_br=8
         self.price_n=15
         self.price_tr=20

         self.rice=["Steam Rice","Fried Rice","Schezwan Rice"]
         self.price_sr=15
         self.price_fr=18
         self.price_scr=22
  
         self.water=["Bisleri Water","Aquafina Water","Bailley Water"]
         self.price_bw=20
         self.price_aw=20
         self.price_baw=20


         self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]
         self.SubCatMobiles=["Iphone","Samsung","Xiome","Realme","OnePlus"]
         self.SubCatRestaurant=["Veg","Non Veg","Roti","Rice","Water"]

         #Image1
         img_1 = Image.open("images/1.jpg")
         img_1 = img_1.resize((455,130),Image.ANTIALIAS)
         self.photoimg_1=ImageTk.PhotoImage(img_1)

         lb1_img=Label(self.root,image=self.photoimg_1)
         lb1_img.place(x=0,y=0,width=455,height=130)

         #Image2
         img_2 = Image.open("images/2.jpg")
         img_2 = img_2.resize((455,130),Image.ANTIALIAS)
         self.photoimg_2=ImageTk.PhotoImage(img_2)

         lb2_img=Label(self.root,image=self.photoimg_2)
         lb2_img.place(x=455,y=0,width=455,height=130)

         #Image3
         img_3 = Image.open("images/9.jpg")
         img_3 = img_3.resize((455,130),Image.ANTIALIAS)
         self.photoimg_3=ImageTk.PhotoImage(img_3)

         lb3_img=Label(self.root,image=self.photoimg_3)
         lb3_img.place(x=910,y=0,width=455,height=130)
 
         lb1_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",25,"bold"),bg="white",fg="red")
         lb1_title.place(x=0,y=130,width=1366,height=45)

         def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
        
         lbl = Label(lb1_title, font = ('times new roman',16, 'bold'),background = 'white',foreground = 'blue') 
         lbl.place(x=2,y=(-10),width=120,height=45) 
         time()


         Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
         Main_Frame.place(x=0,y=175,width=1366,height=768)



        #  Customer Label Frame
         Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
         Cust_Frame.place(x=10,y=5,width=350,height=140)

         self.lb1_mob=Label(Cust_Frame,text="Mobile No.",font=("arial",12,"bold"),bg="white")
         self.lb1_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

         self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
         self.entry_mob.grid(row=0,column=1)

         self.lb1CustName=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",bd=4)
         self.lb1CustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

         self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
         self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
 
         self.lb1Email=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Email",bd=4)
         self.lb1Email.grid(row=2,column=0,sticky=W,padx=5,pady=2)

         self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
         self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
 
         # Product Label Frame
         Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
         Product_Frame.place(x=370,y=5,width=620,height=140)

         # Category
         self.lb1Category=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Categories",bd=4)
         self.lb1Category.grid(row=0,column=0,sticky=W,padx=5,pady=2)

         self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=24,state='readonly')
         self.Combo_Category.current(0)
         self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
         self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

         # SubCategory
         self.lb1SubCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Subcategory",bd=4)
         self.lb1SubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

         self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24,state='readonly')
         self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
         self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

         # Product Name
         self.lb1product=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
         self.lb1product.grid(row=2,column=0,sticky=W,padx=5,pady=2)

         self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state='readonly')
         self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
         self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        # Price
         self.lb1Price=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Price",bd=4)
         self.lb1Price.grid(row=0,column=2,sticky=W,padx=5,pady=2)

         self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,state='readonly',width=26)
         self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

         # Qty
         self.lb1Qty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Qty",bd=4)
         self.lb1Qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

         self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=24)
         self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

         # Middle Frame
         MiddleFrame=Frame(Main_Frame)
         MiddleFrame.place(x=10,y=150,width=980,height=340)

         #Image4
         img_4 = Image.open("images/15.jpg")
         img_4 = img_4.resize((490,235),Image.ANTIALIAS)
         self.photoimg_4=ImageTk.PhotoImage(img_4)

         lb4_img=Label(MiddleFrame,image=self.photoimg_4)
         lb4_img.place(x=0,y=0,width=490,height=235)

         #Image5
         img_5 = Image.open("images/18.jpg")
         img_5 = img_5.resize((490,235),Image.ANTIALIAS)
         self.photoimg_5=ImageTk.PhotoImage(img_5)

         lb5_img=Label(MiddleFrame,image=self.photoimg_5)
         lb5_img.place(x=491,y=0,width=489,height=235)

         # Search
         Search_Frame=Frame(Main_Frame,bd=5,bg="white")
         Search_Frame.place(x=1000,y=14,width=500,height=40)

         self.lb1Bill=Label(Search_Frame,font=("arial",10,"bold"),fg="white",bg="red",text="Bill Number")
         self.lb1Bill.grid(row=0,column=0,sticky=W,padx=1)

         self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
         self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2) 

         self.BtnSearch = Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=8,cursor="hand2")
         self.BtnSearch.grid(row=0,column=2)



         # Right Frame (Bill Area)
         RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
         RightLabelFrame.place(x=1000,y=45,width=345,height=340)

         scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
         self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_y.config(command=self.textarea.yview)
         self.textarea.pack(fill=BOTH,expand=1)


         # Bill Counter  LabelFrame
         Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
         Bottom_Frame.place(x=0,y=385,width=1360,height=130)
         
         self.lb1SubTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Sub Total",bd=4)
         self.lb1SubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

         self.EntrySubTotal=ttk.Entry(Bottom_Frame,text=self.sub_total,font=("arial",10,"bold"),width=24)
         self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)    

         self.lb1_tax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Gov Tax",bd=4)
         self.lb1_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

         self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24)
         self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)     

         self.lb1AmountTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total",bd=4)
         self.lb1AmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

         self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24)
         self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2) 

         #Button Frame
         Btn_Frame = Frame(Bottom_Frame,bd=2,bg="white")
         Btn_Frame.place(x=320,y=0)

         self.BtnAddToCart = Button(Btn_Frame,command=self.AddItem,height = 2,text="Add to cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=13,cursor="hand2")
         self.BtnAddToCart.grid(row=0,column=0)

         self.Btngenerate_bill = Button(Btn_Frame,command=self.gen_bill,height = 2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=13,cursor="hand2")
         self.Btngenerate_bill.grid(row=0,column=1)

         self.BtnSave = Button(Btn_Frame,command=self.save_bill,height = 2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=13,cursor="hand2")
         self.BtnSave.grid(row=0,column=2)

         self.BtnPrint = Button(Btn_Frame,command=self.iprint,height = 2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=13,cursor="hand2")
         self.BtnPrint.grid(row=0,column=3)

         self.BtnClear = Button(Btn_Frame,height = 2,command=self.clear,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=13,cursor="hand2")
         self.BtnClear.grid(row=0,column=4)

         self.BtnExit = Button(Btn_Frame,command=self.root.destroy,height = 2,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",width=13,cursor="hand2")
         self.BtnExit.grid(row=0,column=5)
         self.welcome()

         self.l=[]
     # ======================Function Declaration=====================
     def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome To MiniMall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")
        
        self.textarea.insert(END,"\n ===================================")
        self.textarea.insert(END,"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n ===================================\n")   


     def  AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror('Error',"Please Select the Product Name") 
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))


     def gen_bill(self):
        if self.product.get()=="":
                messagebox.showerror("Error","Please Add To Cart Product") 
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n===================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t{self.total.get()}")
            self.textarea.insert(END,"\n===================================")

     def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("bills/"+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            messagebox.showinfo("Saved",f"Bill No: {self.bill_no.get()} saved Successfully")
            f1.close()

     def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,"w").write(q)
        os.startfile(filename,"print")

     def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

     def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()

 

     def Categories(self,event=""):
         if self.Combo_Category.get()=="Clothing":
              self.ComboSubCategory.config(value=self.SubCatClothing)
              self.ComboSubCategory.current(0)

         if self.Combo_Category.get()=="Lifestyle":
              self.ComboSubCategory.config(value=self.SubCatLifeStyle)
              self.ComboSubCategory.current(0)

         if self.Combo_Category.get()=="Mobiles":
              self.ComboSubCategory.config(value=self.SubCatMobiles)
              self.ComboSubCategory.current(0)

         if self.Combo_Category.get()=="Restaurant":
              self.ComboSubCategory.config(value=self.SubCatRestaurant)
              self.ComboSubCategory.current(0)

     def Product_add(self,event=""):
         if self.ComboSubCategory.get()=="Pants":
               self.ComboProduct.config(value=self.pant)
               self.ComboProduct.current(0)

         if self.ComboSubCategory.get()=="T-Shirt":
               self.ComboProduct.config(value=self.tshirt)
               self.ComboProduct.current(0)

         if self.ComboSubCategory.get()=="Shirt":
               self.ComboProduct.config(value=self.shirt)
               self.ComboProduct.current(0)
 
         #LifeStyle
         if self.ComboSubCategory.get()=="Bath Soap":
               self.ComboProduct.config(value=self.bathsoap)
               self.ComboProduct.current(0)
               
         
         if self.ComboSubCategory.get()=="Face Cream":
               self.ComboProduct.config(value=self.facecream)
               self.ComboProduct.current(0)

          
         if self.ComboSubCategory.get()=="Hair Oil":
               self.ComboProduct.config(value=self.hairoil)
               self.ComboProduct.current(0)

          #Mobile
          
         if self.ComboSubCategory.get()=="Iphone":
               self.ComboProduct.config(value=self.iphone)
               self.ComboProduct.current(0)

          
         if self.ComboSubCategory.get()=="Samsung":
               self.ComboProduct.config(value=self.samsung)
               self.ComboProduct.current(0)

          
         if self.ComboSubCategory.get()=="Xiome":
               self.ComboProduct.config(value=self.xiome)
               self.ComboProduct.current(0)

        
         if self.ComboSubCategory.get()=="Realme":
               self.ComboProduct.config(value=self.realme)
               self.ComboProduct.current(0)
         
         if self.ComboSubCategory.get()=="OnePlus":
               self.ComboProduct.config(value=self.oneplus)
               self.ComboProduct.current(0)


          #Restaurtant
          
         if self.ComboSubCategory.get()=="Veg":
               self.ComboProduct.config(value=self.veg)
               self.ComboProduct.current(0)

         if self.ComboSubCategory.get()=="Non Veg":
               self.ComboProduct.config(value=self.nonveg)
               self.ComboProduct.current(0)

 
         if self.ComboSubCategory.get()=="Roti":
               self.ComboProduct.config(value=self.roti)
               self.ComboProduct.current(0)

         if self.ComboSubCategory.get()=="Rice":
               self.ComboProduct.config(value=self.rice)
               self.ComboProduct.current(0)

         if self.ComboSubCategory.get()=="Water":
               self.ComboProduct.config(value=self.water)
               self.ComboProduct.current(0)

     def price(self,event=""):
         # Pant
         if self.ComboProduct.get()=="Levis":
              self.ComboPrice.config(value=self.price_levis)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Loto":
              self.ComboPrice.config(value=self.price_loto)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Mufti":
              self.ComboPrice.config(value=self.price_mufti)
              self.ComboPrice.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Denim":
              self.ComboPrice.config(value=self.price_denim)
              self.ComboPrice.current(0)
              self.qty.set(1)

        #T-Shirts
         if self.ComboProduct.get()=="US Polo":
              self.ComboPrice.config(value=self.price_uspolo)
              self.ComboPrice.current(0)
              self.qty.set(1)       

         if self.ComboProduct.get()=="Roaster":
              self.ComboPrice.config(value=self.price_roaster)
              self.ComboPrice.current(0)
              self.qty.set(1)     

         if self.ComboProduct.get()=="Ginny Jonny":
              self.ComboPrice.config(value=self.price_ginnyjonny)
              self.ComboPrice.current(0)
              self.qty.set(1)       

         # Shirts

         if self.ComboProduct.get()=="Peter England":
              self.ComboPrice.config(value=self.price_peter)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Louis Phillipe":
              self.ComboPrice.config(value=self.price_louis)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Park Avenue":
              self.ComboPrice.config(value=self.price_park)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         # LifeStyle-Bath Soap

         if self.ComboProduct.get()=="LifeBuoy":
              self.ComboPrice.config(value=self.price_life)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Lux":
              self.ComboPrice.config(value=self.price_lux)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Santoor":
              self.ComboPrice.config(value=self.price_santoor)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Peers":
              self.ComboPrice.config(value=self.price_peers)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         #LifeStyle - Face Cream

         if self.ComboProduct.get()=="Fair & Lovely":
              self.ComboPrice.config(value=self.price_fair)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Ponds":
              self.ComboPrice.config(value=self.price_ponds)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Olay":
              self.ComboPrice.config(value=self.price_olay)
              self.ComboPrice.current(0)
              self.qty.set(1)  
         
         if self.ComboProduct.get()=="Garnier":
              self.ComboPrice.config(value=self.price_garnier)
              self.ComboPrice.current(0)
              self.qty.set(1)  
      
         # LifeStyle-Hair Oil

         if self.ComboProduct.get()=="Parachute":
              self.ComboPrice.config(value=self.price_para)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Jasmin":
              self.ComboPrice.config(value=self.price_jasmin)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Bajaj":
              self.ComboPrice.config(value=self.price_bajaj)
              self.ComboPrice.current(0)
              self.qty.set(1)  
         
      #    Mobiles-Iphone
         if self.ComboProduct.get()=="Iphone X":
              self.ComboPrice.config(value=self.price_ix)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Iphone_11":
              self.ComboPrice.config(value=self.price_i11)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Iphone_12":
              self.ComboPrice.config(value=self.price_i12)
              self.ComboPrice.current(0)
              self.qty.set(1)  

      #   Mobiles-OnePlus

         if self.ComboProduct.get()=="OnePLus 5":
              self.ComboPrice.config(value=self.price_one5)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="OnePlus 5T":
              self.ComboPrice.config(value=self.price_one5t)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="OnePlus 6":
              self.ComboPrice.config(value=self.price_one6)
              self.ComboPrice.current(0)
              self.qty.set(1)  

      #      MObiles-Samsung

         if self.ComboProduct.get()=="Samsung M16":
              self.ComboPrice.config(value=self.price_sm16)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Samsung M12":
              self.ComboPrice.config(value=self.price_sm12)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Samsung M21":
              self.ComboPrice.config(value=self.price_sm21)
              self.ComboPrice.current(0)
              self.qty.set(1)  


      #  Mobiles - Realme

         if self.ComboProduct.get()=="Realme 13Pro":
              self.ComboPrice.config(value=self.price_real13p)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Realme 13":
              self.ComboPrice.config(value=self.price_real13)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Realme 12":
              self.ComboPrice.config(value=self.price_real12)
              self.ComboPrice.current(0)
              self.qty.set(1)  

      #  Mobiles - Xiome

         if self.ComboProduct.get()=="Redme 11":
              self.ComboPrice.config(value=self.price_r11)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Redme 12":
              self.ComboPrice.config(value=self.price_r12)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Redme 11 Pro":
              self.ComboPrice.config(value=self.price_r11pro)
              self.ComboPrice.current(0)
              self.qty.set(1)  

      #  Restaurtant - Veg

         if self.ComboProduct.get()=="Palak Paneer":
              self.ComboPrice.config(value=self.price_pp)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Paneer Chilli":
              self.ComboPrice.config(value=self.price_pac)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Veg Biryani":
              self.ComboPrice.config(value=self.price_b)
              self.ComboPrice.current(0)
              self.qty.set(1)  

      #  Restaurtant - Non Veg

         if self.ComboProduct.get()=="Chicken Tikka":
              self.ComboPrice.config(value=self.price_ct)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Mutton Mughalae":
              self.ComboPrice.config(value=self.price_mm)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Chicken Dum Biryani":
              self.ComboPrice.config(value=self.price_cb)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         #Restaurtant - Roti

         if self.ComboProduct.get()=="Plain Roti":
              self.ComboPrice.config(value=self.price_pr)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Butter Roti":
              self.ComboPrice.config(value=self.price_br)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Naan":
              self.ComboPrice.config(value=self.price_n)
              self.ComboPrice.current(0)
              self.qty.set(1)  
         
         if self.ComboProduct.get()=="Tandoori Roti":
              self.ComboPrice.config(value=self.price_tr)
              self.ComboPrice.current(0)
              self.qty.set(1)  

      #   Restaurtant - Rice

         if self.ComboProduct.get()=="Steam Rice":
              self.ComboPrice.config(value=self.price_sr)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Fried Rice":
              self.ComboPrice.config(value=self.price_fr)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Schezwan Rice":
              self.ComboPrice.config(value=self.price_scr)
              self.ComboPrice.current(0)
              self.qty.set(1)  
 
      #   Restaurtant - Water

         if self.ComboProduct.get()=="Bisleri Water":
              self.ComboPrice.config(value=self.price_bw)
              self.ComboPrice.current(0)
              self.qty.set(1)       
         
         if self.ComboProduct.get()=="Aquafina Water":
              self.ComboPrice.config(value=self.price_aw)
              self.ComboPrice.current(0)
              self.qty.set(1)  

         if self.ComboProduct.get()=="Bailey Water":
              self.ComboPrice.config(value=self.price_baw)
              self.ComboPrice.current(0)
              self.qty.set(1)  


if __name__== '__main__' :
    man()
