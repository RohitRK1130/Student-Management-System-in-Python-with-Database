from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root = root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1900x1000+0+0")
        title= Label(self.root,text="STUDENT MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#ff9999",fg="#1a0000")
        title.pack(side=TOP,fill=X)

        #+++++++++++++++++++++++++all var++++++++++++++++++++++++++++++++++++=++++++++++++++++++++++
        self.Roll_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_cm=StringVar()
        self.search_txt=StringVar()






        #++++++++++++++++++++++++++++++++++++++++Manage_Frame++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        manage_frame= Frame(self.root,bd=4,relief=GROOVE,bg="#ffb366")
        manage_frame.place(x=20,y=100,width=700,height=880)




        m_title= Label(manage_frame,text="Manage Students",bg="#ffb366",fg="Black",font=("times new roman",35,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(manage_frame,text="Roll NO.= ",bg="#ffb366",fg="Black",font=("times new roman",25,"bold"))
        lbl_roll.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(manage_frame,textvariable=self.Roll_var,font=("times new roman",25,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(manage_frame,text="Name = ",bg="#ffb366",fg="Black",font=("times new roman",25,"bold"))
        lbl_name.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(manage_frame,textvariable=self.Name_var,font=("times new roman",25,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Email=Label(manage_frame,text="Email = ",bg="#ffb366",fg="Black",font=("times new roman",25,"bold"))
        lbl_Email.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_Emaill=Entry(manage_frame,textvariable=self.Email_var,font=("times new roman",25,"bold"),bd=5,relief=GROOVE)
        txt_Emaill.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender=Label(manage_frame,text="Gender = ",bg="#ffb366",fg="Black",font=("times new roman",25,"bold"))
        lbl_Gender.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        com_gender=ttk.Combobox(manage_frame,textvariable=self.Gender_var,font=("times new roman",24,"bold"),state='readonly')
        com_gender['values']=('Male','Female','Other')
        com_gender.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_contact=Label(manage_frame,text="Contact = ",bg="#ffb366",fg="Black",font=("times new roman",25,"bold"))
        lbl_contact.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(manage_frame,textvariable=self.Contact_var,font=("times new roman",25,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Dob = Label(manage_frame, text="D.O.B. = ", bg="#ffb366", fg="Black",font=("times new roman", 25, "bold"))
        lbl_Dob.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_Dob = Entry(manage_frame,textvariable=self.dob_var, font=("times new roman", 25, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_add = Label(manage_frame, text="Address = ", bg="#ffb366", fg="Black",font=("times new roman", 25, "bold"))
        lbl_add.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        self.txt_add = Text(manage_frame,width=20,height=4,font=("times new roman", 25))
        self.txt_add.grid(row=8, column=1, pady=10, padx=20, sticky="w")



        #++++++++++++++++++++++++++++++++button_Frame++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        btn_frame = Frame(manage_frame, bd=7, relief=RIDGE, bg="#ffb366")
        btn_frame.place(x=15, y=730, width=660)

        addbtn= Button(btn_frame,text="Add",command=self.add_students,width=10,font=("times new roman", 14, "bold")).grid(row=9, column=0, pady=10, padx=20, sticky="w")
        updatebtn = Button(btn_frame, text="Update",command=self.updateall, width=10,font=("times new roman", 14, "bold")).grid(row=9, column=1, pady=10, padx=20, sticky="w")
        deletebtn = Button(btn_frame, text="Delete",command=self.deleteall, width=10,font=("times new roman", 14, "bold")).grid(row=9, column=2, pady=10, padx=20, sticky="w")
        clerbtn = Button(btn_frame, text="Clear",command=self.clr, width=10,font=("times new roman", 14, "bold")).grid(row=9, column=4, pady=10, padx=20, sticky="w")




#+++++++++++++++++++++++++Manage_Frame=2+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        manage_frame1 = Frame(self.root, bd=4, relief=GROOVE, bg="#ffb366")
        manage_frame1.place(x=750, y=100, width=1135, height=880)



        #+++++++++++++++++++++Search_frame+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        search_frame = Frame(manage_frame1, bd=4, relief=RIDGE, bg="#ffb366")
        search_frame.place(x=15, y=10, width=1100,height=80)

        lbl_search=Label(search_frame,text="Search By = ",bg="#ffb366",fg="Black",font=("times new roman", 25, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=15, sticky="w")

        com_search = ttk.Combobox(search_frame,textvariable=self.search_cm, font=("times new roman", 15, "bold"), state='readonly')
        com_search['values'] = ('Roll_No','Name','Contact')
        com_search.grid(row=0, column=1, pady=5, padx=20, sticky="w")

        txt_search = Entry(search_frame,textvariable=self.search_txt, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        searchbtn = Button(search_frame, text="Search",command=self.search_data,width=10, font=("times new roman", 18, "bold")).grid(row=0, column=4, pady=10, padx=10, sticky="w")
        allsearchbtn = Button(search_frame, text="Search All",command=self.fh_data, width=10, font=("times new roman", 18, "bold")).grid(row=0, column=5, pady=10, padx=10,sticky="w")



        #++++++++++++++++++++++Table_frame+++++++++++++++++++++++++++++++++++++++++++++++++++++++

        table_frame = Frame(manage_frame1, bd=4, relief=RIDGE, bg="#ffb366")
        table_frame.place(x=15, y=100, width=1100,height=710)


        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns =("Roll","Name","Email","Gender","Contact","D.O.B.","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Contact", text="Contact")
        self.student_table.heading("D.O.B.", text="D.O.B.")
        self.student_table.heading("Address", text="Address")
        self.student_table['show']="headings"
        self.student_table.column("Roll",width=50)
        self.student_table.column("Name", width=100)
        self.student_table.column("Email", width=150)
        self.student_table.column("Gender", width=50)
        self.student_table.column("Contact", width=100)
        self.student_table.column("D.O.B.", width=100)
        self.student_table.column("Address", width=300)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.getall)
        self.fh_data()

    def add_students(self):
        if self.Roll_var.get()=="" and self.Name_var.get()=="":
            messagebox.showerror("Error","All Fields are Required !")
        else:
            a1=self.Roll_var.get()
            a2=self.Name_var.get()
            a3=self.Email_var.get()
            a4=self.Gender_var.get()
            a5=self.Contact_var.get()
            a6=self.dob_var.get()
            a7=self.txt_add.get('1.0', END)
            # (roll_no, name, email, gender, contact, dob, addresss)
            con = pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur = con.cursor()
            sql = "INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val =(a1,a2,a3,a4,a5,a6,a7)
            cur.execute(sql,val)
            con.commit()
            self.fh_data()
            self.clr()
            con.close()
            messagebox.showinfo("Success","Record has been Inserted")

    def fh_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def getall(self,ev):
        currow=self.student_table.focus()
        contents=self.student_table.item(currow)
        row=contents["values"]
        self.Roll_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_add.delete("1.0",END)
        self.txt_add.insert(END,row[6])

    def updateall(self):
        a1=self.Roll_var.get()
        a2=self.Name_var.get()
        a3=self.Email_var.get()
        a4=self.Gender_var.get()
        a5=self.Contact_var.get()
        a6=self.dob_var.get()
        a7=self.txt_add.get('1.0', END)
        # (roll_no, name, email, gender, contact, dob, addresss)
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        sql = "update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s"
        val =(a2,a3,a4,a5,a6,a7,a1)
        cur.execute(sql,val)
        con.commit()
        self.fh_data()
        self.clr()
        con.close()


    def deleteall(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        b1 = self.Roll_var.get()
        cur.execute("delete from students where roll_no=%s",b1)
        con.commit()
        con.close()
        self.fh_data()
        self.clr()



    def clr(self):
        self.Roll_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.dob_var.set("")
        self.txt_add.delete("1.0",END)

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        s1=self.search_cm.get()
        s2=self.search_txt.get()
        if self.search_cm.get()=="" and self.search_txt.get()=="":
            messagebox.showerror("Error", "Fields are Required !")
        else:
            cur = con.cursor()
            print(s1,s2)
            cur.execute("select * from students where "+str(s1)+" LIKE '%"+str(s2)+"%'")
            rows = cur.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
                con.commit()
            con.close()







root=Tk()
ob=student(root)
root.mainloop()