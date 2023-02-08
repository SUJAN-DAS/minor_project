from tkinter import *
from tkinter import ttk
# import mysql.connector

from PIL import Image, ImageTk


class Criminal:
    def __init__(self,root):
        self.root = root
        # self.root.geometry('1920*1080+0+0')
        self.root.title('Crime Management System')

        # variables
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()










        lb1_title = Label(self.root , text="CRIME MANAGEMENT SYSTEM SOFTWARE", font =('Times new roman' , 40, 'bold'),bg='black',fg='gold')
        lb1_title.place(x=0 ,y=0 ,width =1530 ,height=70)
        img_logo = Image.open('images/logo.jpg')
        img_logo = img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        self.logo =Label(self.root , image = self.photo_logo )
        self.logo.place(x=90 ,y=5 ,width=60 ,height=60)

        #Img_Frame
        img_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        img1 = Image.open('images/police.jpg')
        img1 = img1.resize((540,260), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)
        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)

      # 2nd
        img_2 = Image.open('images/police car.jpg')
        img_2 = img_2.resize((540, 260), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img_2)
        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)

        # 3rd
        img_3 = Image.open('images/hjhj.jpg')
        img_3 = img_3.resize((540, 260), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img_3)
        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1080, y=0, width=540, height=160)

        Main_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10 , y=200 , width=1500, height=560)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE,text="Criminal Information", font =('Times new roman' , 11, 'bold'),fg='red',bg='white')
        upper_frame.place(x=10, y=10, width=1480, height=270)

        #label entry


        #case id
        caseid=Label(upper_frame,text='Case ID:', font=('arial', 11, 'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,pady=7,sticky=W)
        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial', 11, 'bold'))
        caseentry.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        # Criminal No
        lb1_Criminal=Label(upper_frame,text='Criminal NO. :',font=('arial', 11, 'bold'),bg='white')
        lb1_Criminal.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        lb1entry = ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22, font=('arial', 11, 'bold'))
        lb1entry.grid(row=0, column=3, padx=2,pady=7, sticky=W)

        # Criminal Type
        lb2_Criminal = Label(upper_frame, text='Crime Type:', font=('arial', 11, 'bold'), bg='white')
        lb2_Criminal.grid(row=0, column=4, padx=2,pady=7, sticky=W)

        lb2entry = ttk.Entry(upper_frame,textvariable=self.var_crime_type, width=22, font=('arial', 11, 'bold'))
        lb2entry.grid(row=0, column=5, padx=2,pady=7, sticky=W)

        # Criminal Name
        lb3_Criminal = Label(upper_frame, text='Criminal Name:', font=('arial', 11, 'bold'), bg='white')
        lb3_Criminal.grid(row=1, column=0, padx=2,pady=7, sticky=W)

        lb3entry = ttk.Entry(upper_frame,textvariable=self.var_name, width=22, font=('arial', 11, 'bold'))
        lb3entry.grid(row=1, column=1, padx=2,pady=7, sticky=W)

        # NickName
        lb4_Criminal = Label(upper_frame, text='Nick Name:', font=('arial', 11, 'bold'), bg='white')
        lb4_Criminal.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        lb4entry = ttk.Entry(upper_frame,textvariable=self.var_nickname, width=22, font=('arial', 11, 'bold'))
        lb4entry.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # Father Name
        lb4_Criminal = Label(upper_frame, text='Father Name:', font=('arial', 11, 'bold'), bg='white')
        lb4_Criminal.grid(row=1, column=4, padx=2, pady=7, sticky=W)

        lb4entry = ttk.Entry(upper_frame,textvariable=self.var_father_name, width=22, font=('arial', 11, 'bold'))
        lb4entry.grid(row=1, column=5, padx=2, pady=7, sticky=W)

        # Arrest date
        lb5_Criminal = Label(upper_frame, text='Arrest Date:', font=('arial', 11, 'bold'), bg='white')
        lb5_Criminal.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        lb5entry = ttk.Entry(upper_frame,textvariable=self.var_arrest_date, width=22, font=('arial', 11, 'bold'))
        lb5entry.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # Date of Crime
        lb6_Criminal = Label(upper_frame, text='Date Of Crime :', font=('arial', 11, 'bold'), bg='white')
        lb6_Criminal.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        lb6entry = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width=22, font=('arial', 11, 'bold'))
        lb6entry.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Gender
        lb7_Criminal = Label(upper_frame, text='Gender:', font=('arial', 11, 'bold'), bg='white')
        lb7_Criminal.grid(row=2, column=4, padx=2, pady=7, sticky=W)

        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=713, y=80, width=182, height=30)

        male = Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=("arial",9,"bold"),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        female = Radiobutton(radio_frame_gender,variable=self.var_gender, text='Female', value='female', font=("arial", 9, "bold"), bg='white')
        female.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Address
        lb8_Criminal = Label(upper_frame, text='Address :', font=('arial', 11, 'bold'), bg='white')
        lb8_Criminal.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        lb8entry = ttk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
        lb8entry.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # Age
        lb9_Criminal = Label(upper_frame, text='Age:', font=('arial', 11, 'bold'), bg='white')
        lb9_Criminal.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        lb9entry = ttk.Entry(upper_frame,textvariable=self.var_age, width=22, font=('arial', 11, 'bold'))
        lb9entry.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Most Wanted

        lb10_Criminal = Label(upper_frame, text='Most Wanted:', font=('arial', 11, 'bold'), bg='white')
        lb10_Criminal.grid(row=3, column=4, padx=2, pady=7,sticky=W)

        radio_frame_wanted = Frame(upper_frame,bd=2,relief = RIDGE ,bg='white')
        radio_frame_wanted.place(x=713, y=120, width=182, height=30)

        yes = Radiobutton(radio_frame_wanted,variable=self.var_wanted, text='Yes', value='yes', font=("arial", 9, "bold"), bg='white')
        yes.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        no = Radiobutton(radio_frame_wanted,variable=self.var_wanted,
                         text='No', value='no', font=("arial", 9, "bold"), bg='white')
        no.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Occupation
        lb11_Criminal = Label(upper_frame, text='Occupation:', font=('arial', 11, 'bold'), bg='white')
        lb11_Criminal.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        lb11entry = ttk.Entry(upper_frame,textvariable=self.var_occupation, width=22, font=('arial', 11, 'bold'))
        lb11entry.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # Birth Mark
        lb12_Criminal = Label(upper_frame, text='Birth Mark:', font=('arial', 11, 'bold'), bg='white')
        lb12_Criminal.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        lb12entry = ttk.Entry(upper_frame,textvariable=self.var_birthMark, width=22, font=('arial', 11, 'bold'))
        lb12entry.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        # Buttons

        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)

        # add button
        btn_add = Button(button_frame, text='Save ', font=('arial', 11, 'bold'),width=14,bg="blue",fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5, sticky=W)

        # Update
        btn_update = Button(button_frame, text='Update ', font=('arial', 11, 'bold'), width=14, bg="blue", fg='white')
        btn_update.grid(row=0, column=1, padx=3, pady=5, sticky=W)

        # Delete
        btn_delete = Button(button_frame, text='Delete ', font=('arial', 11, 'bold'), width=14, bg="blue", fg='white')
        btn_delete.grid(row=0, column=2, padx=3, pady=5, sticky=W)

        # Clear
        btn_clear = Button(button_frame, text='Clear ', font=('arial', 11, 'bold'), width=14, bg="blue", fg='white')
        btn_clear.grid(row=0, column=3, padx=3, pady=5, sticky=W)


        # background right side image
        img_crime = Image.open('images/crime.jpg')
        img_crime = img_crime.resize((470, 245), Image.ANTIALIAS)
        self.photocrime = ImageTk.PhotoImage(img_crime)
        self.img_3 = Label(upper_frame, image=self.photocrime)
        self.img_3.place(x=1000, y=0, width=470, height=245)

        # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text="Criminal Information Table",
                                 font=('Times new roman', 11, 'bold'), fg='red', bg='white')
        down_frame.place(x=10, y=280, width=1480, height=270)

        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text="Search Criminal Record",
                                 font=('Times new roman', 11, 'bold'), fg='red', bg='white')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(search_frame, text='Search By:', font=('arial', 11, 'bold'), bg='red',fg='white')
        search_by.grid(row=0, column=0, padx=2,pady=2, sticky=W)

        combo_search_box = ttk.Combobox(search_frame, font=('arial',11,"bold"),width=18,state='readonly')
        combo_search_box['value'] = ('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, padx=2,pady=2, sticky=W)

        search_txt = ttk.Entry(search_frame, width=18, font=('arial', 11, 'bold'))
        search_txt.grid(row=0, column=2, padx=2, pady=2, sticky=W)

        # Search Button
        btn_search = Button(search_frame, text='Search ', font=('arial', 11, 'bold'), width=14, bg="blue", fg='white')
        btn_search.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        # All Button
        btn_all = Button(search_frame, text='Show All', font=('arial', 11, 'bold'), width=14, bg="blue", fg='white')
        btn_all.grid(row=0, column=4, padx=3, pady=5, sticky=W)

        crimeagency = Label(search_frame, font=('arial', 30, 'bold'), text='NATIONAL CRIME AGENCY',bg='white',fg='crimson')
        crimeagency.grid(row=0, column=5, padx=50,pady=0, sticky=W)

        # Table frame
        table_frame=Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='CrimeNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='CrimeOfDate')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show'] = 'headings'
        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)
















        self.criminal_table.pack(fill=BOTH,expand=1)






















if __name__=="__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
