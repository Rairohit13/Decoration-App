from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# from PIL import *
# import json
# import json
import VoucherBackend

global admin_username
global admin_Password

CompanyList = [
    "SATYAM ENTERPRISES",
    "SHIVAM DECORATORS",
    "SUNDARAM EVENT MANAGEMENT",

]

Designationlist = [
    "Manager",
    "Driver",
    "Electrician",
    "Helper"

]


# screen = ""
# screen1 = ""
# screen2 = ""
# login_Username = ""
# login_Password = ""


# data={}

# global username_entry
# global password_entry
# confirm_entry = ""
# username = ""
# password = ""
# def command1(event):
#     if admin_username.get() =='admin' and admin_Password == 'secretkey':
#         screen.deiconify()
#         register_verify_screen.destroy()
def dashboard_page():
    global dashboard_Screen
    dashboard_Screen = Tk()
    dashboard_Screen.title("Dashboard screen")
    dashboard_Screen.geometry()
    dashboard_Screen.geometry(
        "{0}x{1}+0+0".format(dashboard_Screen.winfo_screenwidth(), dashboard_Screen.winfo_screenheight()))
    Mainframe = Frame(dashboard_Screen)
    Mainframe.place(x=0, y=0)
    Titleframe = Frame(Mainframe, width=1350, padx=20, bd=20, relief=RIDGE)
    Titleframe.pack(side=TOP)

    label = Label(Titleframe, width=39, font=('Arial', 40, 'bold'), text="\tSATYAM SHIVAM SUNDARAM\t", padx=12)
    label.pack()

    # Leftframe = Frame(Mainframe, bd=10, width=1350, height=600, relief=GROOVE)
    # Leftframe.pack(side=LEFT)

    # style = ttk.Style(dashboard_Screen)
    # style.configure('lefttab.TNotebook', tabposition='ws')

    style = ttk.Style()
    current_theme = style.theme_use()
    style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": {"padding": [30, 10]}}})
    style.configure('lefttab.TNotebook', tabposition='wn')

    notebook = ttk.Notebook(Mainframe, style='lefttab.TNotebook')
    frame1 = Frame(notebook, width=1000, height=700)
    frame2 = Frame(notebook, width=1000, height=700)
    frame3 = Frame(notebook, width=1000, height=700)
    frame4 = Frame(notebook, width=1000, height=700)
    frame5 = Frame(notebook, width=1000, height=700)
    frame6 = Frame(notebook, width=1000, height=700)
    # frame7 = Frame(notebook, width=1000, height=700)
    # frame8 = Frame(notebook, width=1000, height=700)
    # frame9 = Frame(notebook, width=1000, height=700)

    notebook.add(frame1, text='VOUCHER\t')
    notebook.add(frame2, text='ATTENDANCE\t')
    notebook.add(frame3, text='RENTED VEHICLES')
    notebook.add(frame4, text='  LABOUR\t')
    notebook.add(frame5, text='  STOCKS\t')
    notebook.add(frame6, text='* * BILLS * *\t')
    # notebook.add(frame7, text='\t BILL \t')
    # notebook.add(frame7, text='Tab 7')
    # notebook.add(frame8, text='Tab 8')
    # notebook.add(frame9, text='Tab 9')

    # notebook.pack(padx=50)

    notebook.pack(side=LEFT)

    # grid(row=0, column=0, sticky="sw")

    def cash_payment():
        cheque_frame.place_forget()
        cash_frame.place(x=70, y=125)
        # cash_frame.grid_forget()
        # cheque_frame.grid(row=1, column=0)

    def cheque_payment():
        cash_frame.place_forget()
        cheque_frame.place(x=70, y=125)

    option = IntVar()
    rad1 = Radiobutton(frame1, text="Cash payment ", font=('Arial', 20, 'bold'), variable=option, value=1,
                       command=cash_payment)
    rad1.place(x=200, y=35)
    rad1.select()
    rad2 = Radiobutton(frame1, text="Cheque payment", font=('Arial', 20, 'bold'), variable=option, value=2,
                       command=cheque_payment)
    rad2.place(x=450, y=35)

    cash_frame = Frame(frame1, width=500, height=400, bg="lightgreen")
    cash_frame.place(x=70, y=125)

    variable1 = StringVar(cash_frame)
    variable1.set(CompanyList[0])
    selectcompany = OptionMenu(cash_frame, variable1, *CompanyList)
    selectcompany.config(width=30, height=2, font=('Helvetica', 8))
    selectcompany.place(x=180, y=5)
    # selectcompany.place(x=10, y=10)
    complbl = Label(cash_frame, text="COMPANY NAME :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    complbl.place(x=5, y=10)

    cheque_frame = Frame(frame1, width=500, height=425, bg="lightblue")
    variable2 = StringVar(cheque_frame)
    variable2.set(CompanyList[0])
    selectcompany = OptionMenu(cheque_frame, variable2, *CompanyList)
    selectcompany.config(width=30, height=2, font=('Helvetica', 8))
    selectcompany.place(x=180, y=5)
    complbl = Label(cheque_frame, text="COMPANY NAME :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    complbl.place(x=5, y=10)

    debitorlbl = Label(cash_frame, text="DEBITOR: ", font=('Arial', 10, 'bold'), padx=5, pady=5)  # creates ident labels
    creditorlbl = Label(cash_frame, text="CREDITOR: ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    amountlbl = Label(cash_frame, text="AMOUNT: ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    amountinwordslbl = Label(cash_frame, text="AMOUNT IN WORDS: ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    reasonlbl = Label(cash_frame, text="REASON: ", font=('Arial', 10, 'bold'), padx=5, pady=5)

    debtlbl = Label(cheque_frame, text="DEBITOR : ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    chenolbl = Label(cheque_frame, text="CHEQUE NUMBER: ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    crnalbl = Label(cheque_frame, text="CREDITOR NAME : ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    cracnolbl = Label(cheque_frame, text="CREDITOR ACC NO : ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    crgstlbl = Label(cheque_frame, text="CREDITOR GST NO : ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    amount1lbl = Label(cheque_frame, text="AMOUNT : ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    amwordslbl = Label(cheque_frame, text="AMOUNT IN WORDS : ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    reason1lbl = Label(cheque_frame, text="REASON : ", font=('Arial', 10, 'bold'), padx=5, pady=5)

    #
    global debitortxtvar
    global creditorvar
    global amounttvar
    global amountinwordstxtvar

    debitortxtvar = StringVar()
    creditorvar = StringVar()
    amounttvar = StringVar()
    amountinwordstxtvar = StringVar()

    # cash frame label
    debitortxt = Entry(cash_frame, width=30, textvariable=debitortxtvar)  # creates entry boxes
    creditortxt = Entry(cash_frame, width=30, textvariable=creditorvar)
    amounttxt = Entry(cash_frame, width=30, textvariable=amounttvar)
    amountinwordstxt = Entry(cash_frame, width=30, textvariable=amountinwordstxtvar)
    reasontxt = Text(cash_frame, width=23, height=3)

    # cheque frame entry
    global debttxtvar
    global chenotxtvar
    global crnatxtvar
    global cracnotxtvar
    global crgsttxtvar
    global amount1txtvar
    global amwordstxtvar

    debttxtvar = StringVar()
    chenotxtvar = StringVar()
    crnatxtvar = StringVar()
    cracnotxtvar = StringVar()
    crgsttxtvar = StringVar()
    amount1txtvar = StringVar()
    amwordstxtvar = StringVar()

    debttxt = Entry(cheque_frame, width=30, textvariable=debttxtvar)
    chenotxt = Entry(cheque_frame, width=30, textvariable=chenotxtvar)
    crnatxt = Entry(cheque_frame, width=30, textvariable=crnatxtvar)
    cracnotxt = Entry(cheque_frame, width=30, textvariable=cracnotxtvar)
    crgsttxt = Entry(cheque_frame, width=30, textvariable=crgsttxtvar)
    amount1txt = Entry(cheque_frame, width=30, textvariable=amount1txtvar)
    amwordstxt = Entry(cheque_frame, width=30, textvariable=amwordstxtvar)
    reason1txt = Text(cheque_frame, width=23, height=3)

    # cash frame label
    debitorlbl.place(x=10, y=60)  # assigns grid positions (preferred to pack for precise layout)
    creditorlbl.place(x=10, y=100)
    amountlbl.place(x=10, y=140)
    amountinwordslbl.place(x=10, y=180)
    reasonlbl.place(x=10, y=220)

    # cheque frame label
    debtlbl.place(x=10, y=60)
    chenolbl.place(x=10, y=95)
    crnalbl.place(x=10, y=130)
    cracnolbl.place(x=10, y=165)
    crgstlbl.place(x=10, y=200)
    amount1lbl.place(x=10, y=235)
    amwordslbl.place(x=10, y=270)
    reason1lbl.place(x=10, y=305)

    # cash frame entry
    debitortxt.place(x=180, y=60)
    creditortxt.place(x=180, y=100)
    amounttxt.place(x=180, y=140)
    amountinwordstxt.place(x=180, y=180)
    reasontxt.place(x=180, y=220)

    # cheque frame entry
    debttxt.place(x=180, y=60)
    chenotxt.place(x=180, y=95)
    crnatxt.place(x=180, y=130)
    cracnotxt.place(x=180, y=165)
    crgsttxt.place(x=180, y=200)
    amount1txt.place(x=180, y=235)
    amwordstxt.place(x=180, y=270)
    reason1txt.place(x=180, y=305)

    def submitbutton_CashFrame():
        print(variable1.get(), debitortxt.get(), creditortxt.get(), amounttxt.get(), amountinwordstxt.get(),
              reasontxt.get("1.0", END))

    def submitbutton_ChequeFrame():
        print(variable2.get(), debttxt.get(), chenotxt.get(), crnatxt.get(), cracnotxt.get(), crgsttxt.get(),
              amount1txt.get(), amwordstxt.get(),
              reason1txt.get("1.0", END))

    def Resetbutton_Cashframe():
        variable1.set(CompanyList[0])
        debitortxtvar.set("")
        creditorvar.set("")
        amounttvar.set("")
        amountinwordstxtvar.set("")
        reasontxt.delete(1.0, END)

    def Resetbutton_Chequeframe():
        variable2.set(CompanyList[0])
        debttxtvar.set("")
        chenotxtvar.set("")
        crnatxtvar.set("")
        cracnotxtvar.set("")
        crgsttxtvar.set("")
        amount1txtvar.set("")
        amwordstxtvar.set("")
        reason1txt.delete(1.0, END)

    submit_CashFrame = Button(cash_frame, text="Submit", width=15, height=1, font=6, command=submitbutton_CashFrame)
    submit_CashFrame.place(x=20, y=300)
    Reset_CashFrame = Button(cash_frame, text="Reset", width=15, height=1, font=6, command=Resetbutton_Cashframe)
    Reset_CashFrame.place(x=200, y=300)

    submit_ChequeFrame = Button(cheque_frame, text="Submit", width=15, height=1, font=6,
                                command=submitbutton_ChequeFrame)
    submit_ChequeFrame.place(x=20, y=370)
    Reset_ChequeFrame = Button(cheque_frame, text="Reset", width=15, height=1, font=6, command=Resetbutton_Chequeframe)
    Reset_ChequeFrame.place(x=200, y=370)

    # Switch Tabs
    #
    # Selected_Tab = ""
    #
    # def SwitchTabs(value):
    #     # global Selected_Tab
    #     Selected_Tab = value
    #

    # attendance tab

    def show_AddNewEmpFrame(event):
        defaultframe.place_forget()
        emplistframe.place_forget()
        manempframe.place_forget()
        markattframe.place_forget()
        monsureframe.place_forget()
        addempframe.place(x=300, y=60)

        deptentryvar = StringVar()
        nameentryvar = StringVar()
        # desigvar
        emailentryvar = StringVar()
        # maritial
        addresstxtvar = StringVar()
        dobentryvar = StringVar()
        datejntentryvar = StringVar()
        # gender
        contactentryvar = StringVar()
        cityentryvar = StringVar()
        aadharentryvar = StringVar()
        panentryvar = StringVar()

        def submit_AddEmpframe(event):
            print(deptentry.get(), nameentry.get(), desigvar.get(), emailentry.get(), addresstxt.get('1.0', END),
                  maritial.get(),
                  dobentry.get(), datejntentry.get(), gender.get(), contactentry.get(), cityentry.get(),
                  aadharentry.get(), panentry.get())

        deptlabel = Label(addempframe, text="Department ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        namelabel = Label(addempframe, text="Name ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        desiglabel = Label(addempframe, text="Designation ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        emaillabel = Label(addempframe, text="Email ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        # addresslabel = Label(addempframe, text="Address: ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        marstlabel = Label(addempframe, text="Maritial status ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        dobtlabel = Label(addempframe, text="D.O.B (yyyy-mm-dd) ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        datejnlabel = Label(addempframe, text="D.O.J (yyyy-mm-dd) ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        genderlabel = Label(addempframe, text="Gender ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        contactlabel = Label(addempframe, text="Contact ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        aadharlabel = Label(addempframe, text="Aadhar No ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        panlabel = Label(addempframe, text="Pan No ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        addresslabel = Label(addempframe, text="Address ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        citylabel = Label(addempframe, text="City ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        Salarylabel = Label(addempframe, text="Salary ", font=('Arial', 10, 'bold'), padx=5, pady=5)

        deptlabel.place(x=25, y=50)
        namelabel.place(x=25, y=85)
        desiglabel.place(x=25, y=110)
        emaillabel.place(x=25, y=145)
        # addresslabel.place(x=25, y=150)
        marstlabel.place(x=25, y=170)
        dobtlabel.place(x=25, y=205)
        datejnlabel.place(x=25, y=230)
        genderlabel.place(x=25, y=255)
        contactlabel.place(x=350, y=205)
        citylabel.place(x=350, y=230)
        aadharlabel.place(x=350, y=50)
        panlabel.place(x=350, y=85)
        addresslabel.place(x=350, y=110)
        Salarylabel.place(x=350, y=255)

        # department = StringVar()
        # name = StringVar()
        # name = StringVar()

        global deptentry
        global nameentry
        global desigvar
        global emailentry
        global addresstxt
        global maritial
        global dobentry
        global datejntentry
        global gender
        global contactentry
        global cityentry
        global aadharentry
        global panentry
        global addresstxt

        deptentry = Entry(addempframe, width=28, textvariable=deptentryvar)
        nameentry = Entry(addempframe, width=28, textvariable=nameentryvar)
        # designentry = Entry(addempframe, width=28)
        emailentry = Entry(addempframe, width=28, textvariable=emailentryvar)
        # addressentry = Entry(addempframe, width=28, textvariable=deptentryvar)
        # marstentry = Entry(addempframe, width=28, textvariable=maritial)
        dobentry = Entry(addempframe, width=25, textvariable=dobentryvar)
        datejntentry = Entry(addempframe, width=25, textvariable=datejntentryvar)
        # genderentry = Entry(addempframe, width=28, textvariable=deptentryvar)
        contactentry = Entry(addempframe, width=28, textvariable=contactentryvar)
        cityentry = Entry(addempframe, width=28, textvariable=cityentryvar)
        aadharentry = Entry(addempframe, width=28, textvariable=aadharentryvar)
        panentry = Entry(addempframe, width=28, textvariable=panentryvar)
        addresstxt = Text(addempframe, width=21, height=4)
        Salaryentry = Entry(addempframe, width=28, textvariable=panentryvar)

        deptentry.place(x=145, y=53)
        nameentry.place(x=145, y=88)
        # designentry.place(x=145, y=90)
        emailentry.place(x=145, y=148)
        # addressentry.place(x=145, y=150)
        # marstentry.place(x=145, y=150)
        dobentry.place(x=160, y=208)
        datejntentry.place(x=160, y=233)
        # genderentry.place(x=145, y=225)
        contactentry.place(x=450, y=208)
        cityentry.place(x=450, y=233)
        aadharentry.place(x=450, y=53)
        panentry.place(x=450, y=88)
        addresstxt.place(x=450, y=113)
        Salaryentry.place(x=450, y=258)

        # deptentryvar = StringVar()
        # nameentryvar = StringVar()
        # # desigvar
        # emailentryvar = StringVar()
        # addresstxtvar = StringVar()
        # # maritial
        # dobentryvar = StringVar()
        # datejntentryvar = StringVar()
        # # gender
        # contactentryvar = IntVar()
        # cityentryvar = StringVar()
        # aadharentryvar = StringVar()
        # panentryvar = StringVar()

        global maritial
        maritial = StringVar()
        Mstatus1 = Radiobutton(addempframe, text="Single", variable=maritial, value="Single")
        Mstatus1.place(x=150, y=173)
        Mstatus1.select()
        Mstatus2 = Radiobutton(addempframe, text="Married", variable=maritial, value="Married")
        Mstatus2.place(x=215, y=173)

        global gender
        gender = StringVar()
        Gstatus1 = Radiobutton(addempframe, text="Male", variable=gender, value="Male")
        Gstatus1.place(x=150, y=258)
        Gstatus1.select()
        Gstatus2 = Radiobutton(addempframe, text="Female", variable=gender, value="Female")
        Gstatus2.place(x=215, y=258)

        global desigvar
        desigvar = StringVar(addempframe)
        desigvar.set(Designationlist[0])
        desig = OptionMenu(addempframe, desigvar, *Designationlist)
        desig.config(width=22)
        desig.place(x=140, y=110)

        # def reset_AddEmployee():
        #     deptentry.set

        submitbutton = Button(addempframe, text="Submit", width=12, height=1, font=6)
        submitbutton.place(x=165, y=310)
        submitbutton.bind("<Return>", submit_AddEmpframe)
        submitbutton.bind("<Button-1>", submit_AddEmpframe)

        def reset_AddEmployee(event):
            deptentryvar.set("")
            nameentryvar.set("")
            desigvar.set(Designationlist[0])
            emailentryvar.set("")
            addresstxt.delete("1.0", END)
            Mstatus1.select()
            dobentryvar.set("")
            datejntentryvar.set("")
            Gstatus1.select()
            contactentryvar.set("")
            cityentryvar.set("")
            aadharentryvar.set("")
            panentryvar.set("")

        resetbutton = Button(addempframe, text="Reset", width=12, height=1, font=6)
        resetbutton.place(x=305, y=310)
        resetbutton.bind("<Return>", reset_AddEmployee)
        resetbutton.bind("<Button-1>", reset_AddEmployee)

    def show_EmpList(event):
        defaultframe.place_forget()
        addempframe.place_forget()
        manempframe.place_forget()
        markattframe.place_forget()
        monsureframe.place_forget()
        emplistframe.place(x=300, y=60)

        treev = ttk.Treeview(emplistframe)
        style = ttk.Style(emplistframe)
        style.configure('Treeview', rowheight=38)
        treev.place(x=40, y=40)

        EmpList_scrollbar = ttk.Scrollbar(emplistframe, orient="vertical", command=treev.yview)
        EmpList_scrollbar.place(x=603, y=45, height=350)

        # verticalscrlbar = ttk.Scrollbar(treev, orient="vertical", command=treev.yview)
        # verticalscrlbar.config(command=treev.yview)
        # verticalscrlbar.place(x=0, y=145)

        # verticalscrlbar = Scrollbar(emplistframe)
        # verticalscrlbar.place(x=25, y=140)
        # verticalscrlbar.config(command=treev.yview)

        # verticalscrlbar.place(x=25,y=140)

        # treev.configure(yscrollcommand=verticalscrlbar.set, height=10)
        treev["columns"] = ("1", "2", "3", "4")

        treev['show'] = 'headings'
        treev.column("1", width=140, anchor='c')
        treev.column("2", width=140, anchor='c')
        treev.column("3", width=140, anchor='c')
        treev.column("4", width=140, anchor='c')

        treev.heading("1", text="Name")
        treev.heading("2", text="Designation")
        treev.heading("3", text="E-mail")
        treev.heading("4", text="Contact")

        treev.insert("", 'end', text="L1",
                     values=("Nidhi", "F", "25", "1234"))
        treev.insert("", 'end', text="L2",
                     values=("Nisha", "F", "23", "5678"))
        treev.insert("", 'end', text="L3",
                     values=("Preeti", "F", "27", "9012"))
        treev.insert("", 'end', text="L4",
                     values=("Rahul", "M", "20", "123456"))
        treev.insert("", 'end', text="L5",
                     values=("Nidhi", "F", "25"))
        treev.insert("", 'end', text="L6",
                     values=("Nisha", "F", "23"))
        treev.insert("", 'end', text="L7",
                     values=("Preeti", "F", "27"))
        treev.insert("", 'end', text="L8",
                     values=("Rahul", "M", "20"))
        treev.insert("", 'end', text="L9",
                     values=("Nidhi", "F", "25"))
        treev.insert("", 'end', text="L10",
                     values=("Nisha", "F", "23"))
        treev.insert("", 'end', text="L11",
                     values=("Preeti", "F", "27"))
        treev.insert("", 'end', text="L12",
                     values=("Rahul", "M", "20"))

    def show_ManageEmp(event):
        defaultframe.place_forget()
        addempframe.place_forget()
        emplistframe.place_forget()
        markattframe.place_forget()
        monsureframe.place_forget()
        manempframe.place(x=260, y=40)

        EmpNameLbl_ManageEmp = Label(manempframe, text="Employee Name ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        EmpContactLbl_ManageEmp = Label(manempframe, text="Contact Number ", font=('Arial', 10, 'bold'), padx=5, pady=5)

        EmpNameLbl_ManageEmp.place(x=20, y=25)
        EmpContactLbl_ManageEmp.place(x=330, y=25)

        EmpNameEnt_ManageEmp = Entry(manempframe, width=20)
        EmpContactEnt_ManageEmp = Entry(manempframe, width=20)

        EmpNameEnt_ManageEmp.place(x=160, y=29)
        EmpContactEnt_ManageEmp.place(x=480, y=29)

        SearchManageEmployee = Button(manempframe, text="Search", width=15)
        SearchManageEmployee.place(x=170, y=80)

        ClearManageEmployee = Button(manempframe, text="Clear", width=15)
        ClearManageEmployee.place(x=320, y=80)

        ManageEmployeeTree = ttk.Treeview(manempframe)
        ManageEmployeeTree.place(x=40, y=120)
        style = ttk.Style(monsureframe)
        style.configure('Treeview', rowheight=10)

        ManageEmp_scrollbar = ttk.Scrollbar(manempframe, orient="vertical", command=ManageEmployeeTree.yview)
        ManageEmp_scrollbar.place(x=643, y=119, height=132)

        ManageEmployeeTree["columns"] = ("1", "2", "3", "4", "5")

        ManageEmployeeTree['show'] = 'headings'
        ManageEmployeeTree.column("1", width=120, anchor='c')
        ManageEmployeeTree.column("2", width=120, anchor='c')
        ManageEmployeeTree.column("3", width=120, anchor='c')
        ManageEmployeeTree.column("4", width=120, anchor='c')
        ManageEmployeeTree.column("5", width=120, anchor='c')

        ManageEmployeeTree.heading("1", text="Name")
        ManageEmployeeTree.heading("2", text="Department")
        ManageEmployeeTree.heading("3", text="E-mail")
        ManageEmployeeTree.heading("4", text="Address")
        ManageEmployeeTree.heading("5", text="Contact")

        DepartmentLbl_ManageEmp = Label(manempframe, text="Department ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        DepartmentLbl_ManageEmp.place(x=40, y=290)
        EmailLbl_ManageEmp = Label(manempframe, text="E-mail ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        EmailLbl_ManageEmp.place(x=340, y=290)

        DepartmentEnt_ManageEmp = Entry(manempframe, width=20)
        DepartmentEnt_ManageEmp.place(x=140, y=294)
        EmailEnt_ManageEmp = Entry(manempframe, width=20)
        EmailEnt_ManageEmp.place(x=420, y=294)

        AddressLbl_ManageEmp = Label(manempframe, text="Address ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        AddressLbl_ManageEmp.place(x=40, y=320)
        Address_ManageEmployee = Text(manempframe, width=30, height=3)
        Address_ManageEmployee.place(x=140, y=324)

        ContactLbl_ManageEmp = Label(manempframe, text="Contact ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        ContactLbl_ManageEmp.place(x=40, y=385)
        ContactEnt_ManageEmp = Entry(manempframe, width=20)
        ContactEnt_ManageEmp.place(x=140, y=389)

        Updatebutton_ManageEmp = Button(manempframe, text="Update", width=15)
        Updatebutton_ManageEmp.place(x=60, y=435)

        Deletebutton_ManageEmp = Button(manempframe, text="Delete", width=15)
        Deletebutton_ManageEmp.place(x=220, y=435)

        Clearbutton_ManageEmp = Button(manempframe, text="Clear", width=15)
        Clearbutton_ManageEmp.place(x=360, y=435)

    def show_MarkAttendance(event):
        defaultframe.place_forget()
        addempframe.place_forget()
        emplistframe.place_forget()
        manempframe.place_forget()
        monsureframe.place_forget()
        markattframe.place(x=300, y=60)

        def Submit_MarkAttendance(event):
            print(employeenameent.get(), employeenument.get(), DateMarkAttendentry.get(),
                  ReasonForLeave.get('1.0', END), STATUS.get())

        global EmployeenameVar
        global EmployeenumVar
        global DateMarkVar
        global ReasonVar
        global StatusVar

        EmployeenameVar = StringVar()
        EmployeenumVar = StringVar()
        DateMarkVar = StringVar()
        ReasonVar = StringVar()
        StatusVar = StringVar()

        def Reset_MarkAttendance(event):
            print(EmployeenameVar.set(""), EmployeenumVar.set(""), DateMarkVar.set(""),
                  ReasonForLeave.delete('1.0', END),
                  Presentobj.select())
            ReasonLbl.place_forget(), ReasonForLeave.place_forget()

        suggestion = Label(markattframe, text="MARK  EMPLOYEES  ATTENDANCE  HERE", font=('Arial', 10, 'bold'))
        suggestion.place(x=170, y=5)

        Employeename = Label(markattframe, text="Employee Name  ", font=('Arial', 10, 'bold'))
        Employeename.place(x=50, y=60)
        employeenameent = Entry(markattframe, width=30, textvariable=EmployeenameVar)
        employeenameent.place(x=210, y=60)

        Employeenum = Label(markattframe, text="Contact Number  ", font=('Arial', 10, 'bold'))
        Employeenum.place(x=50, y=100)
        employeenument = Entry(markattframe, width=30, textvariable=EmployeenumVar)
        employeenument.place(x=210, y=100)

        DateMarkAttend = Label(markattframe, text="Date (DD-MM-YYYY) ", font=('Arial', 10, 'bold'))
        DateMarkAttend.place(x=50, y=140)
        DateMarkAttendentry = Entry(markattframe, width=30, textvariable=DateMarkVar)
        DateMarkAttendentry.place(x=210, y=140)

        AttendanceStatus = Label(markattframe, text="STATUS  :", font=('Arial', 10, 'bold'))
        AttendanceStatus.place(x=50, y=200)
        ReasonLbl = Label(markattframe, text="Reason : ", font=('Arial', 10, 'bold'))
        ReasonForLeave = Text(markattframe, width=30, height=3)

        global STATUS
        STATUS = StringVar()

        # def Forget_absentReason():
        #     print("present ", STATUS.get())
        #     ReasonLbl.place_forget()
        #     ReasonForLeave.place_forget()
        #     Submit_AttendanceEmp.place_forget()
        #     Clear_AttendanceEmp.place_forget()
        #     Submit_AttendanceEmp.place(x=100, y=230)
        #     Clear_AttendanceEmp.place(x=270, y=230)
        #
        # def absentReason():
        #     print("absent ", STATUS.get())
        #     Submit_AttendanceEmp.place_forget()
        #     Clear_AttendanceEmp.place_forget()
        #     ReasonLbl.place(x=50, y=200)
        #     ReasonForLeave.place(x=190, y=200)
        #     Submit_AttendanceEmp.place(x=100, y=290)
        #     Clear_AttendanceEmp.place(x=240, y=290)

        def Status_Absent_Present():
            print("Status: -", STATUS.get())
            # Submit_AttendanceEmp.place_forget()
            # Clear_AttendanceEmp.place_forget()
            if STATUS.get() == "Absent" or STATUS.get() == "Leave":
                # Submit_AttendanceEmp.place_forget()
                # Clear_AttendanceEmp.place_forget()
                ReasonLbl.place(x=50, y=240)
                ReasonForLeave.place(x=190, y=240)
                # Submit_AttendanceEmp.place(x=100, y=290)
                # Clear_AttendanceEmp.place(x=240, y=290)
            else:
                # Submit_AttendanceEmp.place_forget()
                # Clear_AttendanceEmp.place_forget()
                ReasonLbl.place_forget()
                ReasonForLeave.place_forget()
                # Submit_AttendanceEmp.place(x=100, y=230)
                # Clear_AttendanceEmp.place(x=270, y=230)

        Presentobj = Radiobutton(markattframe, text="Present", variable=STATUS, value="Present",
                                 command=Status_Absent_Present)
        Presentobj.place(x=140, y=200)
        Presentobj.select()
        Absentobj = Radiobutton(markattframe, text="Absent", variable=STATUS, value="Absent",
                                command=Status_Absent_Present)
        Absentobj.place(x=240, y=200)
        Leaveobj = Radiobutton(markattframe, text="Leave", variable=STATUS, value="Leave",
                               command=Status_Absent_Present)
        Leaveobj.place(x=340, y=200)

        Submit_AttendanceEmp = Button(markattframe, text="Submit", width=15, height=2)
        Submit_AttendanceEmp.bind("<Return>", Submit_MarkAttendance)
        Submit_AttendanceEmp.bind("<Button-1>", Submit_MarkAttendance)
        # Submit_AttendanceEmp.place(x=100, y=290)
        Clear_AttendanceEmp = Button(markattframe, text="Clear", width=15, height=2)
        Clear_AttendanceEmp.bind("<Return>", Reset_MarkAttendance)
        Clear_AttendanceEmp.bind("<Button-1>", Reset_MarkAttendance)
        Submit_AttendanceEmp.place(x=100, y=330)
        Clear_AttendanceEmp.place(x=240, y=330)

    def show_MonthlyReport(event):
        defaultframe.place_forget()
        addempframe.place_forget()
        emplistframe.place_forget()
        manempframe.place_forget()
        markattframe.place_forget()
        monsureframe.place(x=300, y=60)

        emppnamelbl = Label(monsureframe, text="Employee Name ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        empnolbl = Label(monsureframe, text="Contact Number ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        # totpresentlbl = Label(monsureframe, text="Total Present: ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        # totleavelbl = Label(monsureframe, text="Total Leave: ", font=('Arial', 10, 'bold'), padx=5, pady=5)
        # totdayslbl = Label(monsureframe, text="Total days: ", font=('Arial', 10, 'bold'), padx=5, pady=5)

        emppnamelbl.place(x=20, y=40)
        empnolbl.place(x=330, y=40)
        # totpresentlbl.place(x=20, y=120)
        # totleavelbl.place(x=20, y=160)
        # totdayslbl.place(x=20, y=200)

        emppnameentry = Entry(monsureframe, width=20)
        empnoentry = Entry(monsureframe, width=20)
        # totpresententry = Entry(monsureframe, width=30)
        # totleaveentry = Entry(monsureframe, width=30)
        # totdaysentry = Entry(monsureframe, width=30)

        emppnameentry.place(x=160, y=44)
        empnoentry.place(x=480, y=44)
        # totpresententry.place(x=145, y=120)
        # totleaveentry.place(x=145, y=160)
        # totdaysentry.place(x=145, y=200)

        SubmitMonthlyReport = Button(monsureframe, text="Submit", width=15)
        SubmitMonthlyReport.place(x=170, y=100)
        # SubmitMonthlyReport.bind("<Return>", Reset_MarkAttendance)
        # SubmitMonthlyReport.bind("<Button-1>", Reset_MarkAttendance)
        ClearMonthlyReport = Button(monsureframe, text="Clear", width=15)
        ClearMonthlyReport.place(x=320, y=100)
        # ClearMonthlyReport.bind("<Return>", Reset_MarkAttendance)
        # ClearMonthlyReport.bind("<Button-1>", Reset_MarkAttendance)

        MonthlyrepTree = ttk.Treeview(monsureframe)
        MonthlyrepTree.place(x=40, y=140)
        Monthly_style = ttk.Style(monsureframe)
        Monthly_style.configure('Treeview', rowheight=22)

        MonthlyrepTree_scrollbar = ttk.Scrollbar(monsureframe, orient="vertical", command=MonthlyrepTree.yview)
        MonthlyrepTree_scrollbar.place(x=603, y=135, height=255)

        MonthlyrepTree["columns"] = ("1", "2", "3", "4")

        MonthlyrepTree['show'] = 'headings'
        MonthlyrepTree.column("1", width=140, anchor='c')
        MonthlyrepTree.column("2", width=140, anchor='c')
        MonthlyrepTree.column("3", width=140, anchor='c')
        MonthlyrepTree.column("4", width=140, anchor='c')

        MonthlyrepTree.heading("1", text="Name")
        MonthlyrepTree.heading("2", text="Present")
        MonthlyrepTree.heading("3", text="Absent")
        MonthlyrepTree.heading("4", text="Total days")

    f1 = Button(frame2, text="Add new employees", width=25, height=2)
    f1.place(x=60, y=120)
    f1.bind("<Return>", show_AddNewEmpFrame)
    f1.bind("<Button-1>", show_AddNewEmpFrame)

    f2 = Button(frame2, text="Employee list", width=25, height=2)
    f2.place(x=60, y=160)
    f2.bind("<Return>", show_EmpList)
    f2.bind("<Button-1>", show_EmpList)

    f3 = Button(frame2, text="Mark attendance", width=25, height=2)
    f3.place(x=60, y=200)
    f3.bind("<Return>", show_MarkAttendance)
    f3.bind("<Button-1>", show_MarkAttendance)

    f4 = Button(frame2, text="Monthly summary report", width=25, height=2)
    f4.place(x=60, y=240)
    f4.bind("<Return>", show_MonthlyReport)
    f4.bind("<Button-1>", show_MonthlyReport)

    f5 = Button(frame2, text="Manage employees", width=25, height=2)
    f5.place(x=60, y=280)
    f5.bind("<Return>", show_ManageEmp)
    f5.bind("<Button-1>", show_ManageEmp)

    # attendance frame inside frames

    defaultframe = LabelFrame(frame2, text="Welcome", height=420, width=650)
    defaultframe.place(x=300, y=60)

    addempframe = LabelFrame(frame2, text="Add New Employee", height=420, width=650)
    # addempframe.place(x=300, y=60)

    global emplistframe
    emplistframe = LabelFrame(frame2, text="Employee's list", height=420, width=650)
    # emplistframe.place(x=300, y=60)

    markattframe = LabelFrame(frame2, text="Mark Attendance", height=420, width=650)
    # manempframe.place(x=300, y=60)

    monsureframe = LabelFrame(frame2, text="Monthly Report", height=420, width=650)
    # markattframe.place(x=300, y=60)

    manempframe = LabelFrame(frame2, text="Manage Employee", height=520, width=715)
    # monsureframe.place(x=300, y=60)

    # optvalue = IntVar()
    # Employee list frame  Treeview

    # rented vehicles tab label
    RentedVehicles_Tab = LabelFrame(frame3, text="Rented Vehicles :", width=900, height=500)
    RentedVehicles_Tab.place(x=50, y=50)

    namelbl = Label(RentedVehicles_Tab, text="Name ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    vehnalbl = Label(RentedVehicles_Tab, text="Vehicle Name ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    vehnolbl = Label(RentedVehicles_Tab, text="Vehicle No ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    drvnalbl = Label(RentedVehicles_Tab, text="Driver Name ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    fromlbl = Label(RentedVehicles_Tab, text="From  ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    tolbl = Label(RentedVehicles_Tab, text="To  ", font=('Arial', 10, 'bold'), padx=5, pady=5)
    datelbl = Label(RentedVehicles_Tab, text="Date  ", font=('Arial', 10, 'bold'), padx=5, pady=5)

    # rented vehicle tab textbox

    global nametxtvar
    global vehnatxtvar
    global vehnotxtvar
    global drvnatxtvar
    global fromtxtvar
    global totxtvar
    global datetxtvar

    nametxtvar = StringVar()
    vehnatxtvar = StringVar()
    vehnotxtvar = StringVar()
    drvnatxtvar = StringVar()
    fromtxtvar = StringVar()
    totxtvar = StringVar()
    datetxtvar = StringVar()



    nametxt = Entry(RentedVehicles_Tab, width=30, textvariable=nametxtvar)
    vehnatxt = Entry(RentedVehicles_Tab, width=30, textvariable=vehnatxtvar)
    vehnotxt = Entry(RentedVehicles_Tab, width=30, textvariable=vehnotxtvar)
    drvnatxt = Entry(RentedVehicles_Tab, width=30, textvariable=drvnatxtvar)
    fromtxt = Entry(RentedVehicles_Tab, width=30, textvariable=fromtxtvar)
    totxt = Entry(RentedVehicles_Tab, width=30, textvariable=totxtvar)
    datetxt = Entry(RentedVehicles_Tab, width=30, textvariable=datetxtvar)

    namelbl.place(x=90, y=60)
    vehnalbl.place(x=90, y=100)
    vehnolbl.place(x=90, y=140)
    drvnalbl.place(x=90, y=180)
    fromlbl.place(x=90, y=220)
    tolbl.place(x=90, y=260)
    datelbl.place(x=90, y=300)

    nametxt.place(x=230, y=60)
    vehnatxt.place(x=230, y=100)
    vehnotxt.place(x=230, y=140)
    drvnatxt.place(x=230, y=180)
    fromtxt.place(x=230, y=220)
    totxt.place(x=230, y=260)
    datetxt.place(x=230, y=300)

    def Get_Submit_Rented():
        print(nametxt.get(), vehnatxt.get(), vehnotxt.get(), drvnatxt.get(), fromtxt.get(), totxt.get(), datetxt.get())


    Submit_RentedVehicles = Button(RentedVehicles_Tab, text="Submit", font=('Arial', 10, 'bold'), width=15, height=2, command=Get_Submit_Rented)
    Submit_RentedVehicles.place(x=120, y=350)


    def Clear_Clear_RentedVehicles():
        nametxtvar.set(""), vehnatxtvar.set(""), vehnotxtvar.set(""),drvnatxtvar.set(""),fromtxtvar.set(""), totxtvar.set(""),datetxtvar.set("")



    Clear_RentedVehicles = Button(RentedVehicles_Tab, text="Clear", font=('Arial', 10, 'bold'), width=15, height=2, command=Clear_Clear_RentedVehicles)
    Clear_RentedVehicles.place(x=290, y=350)

    # LABOUR Frame

    Anewframe = LabelFrame(frame4, text="Anew frame", width=900, height=530)
    Anewframe.place(x=50, y=10)

    global NameEnt_LabourFvar
    global InformEnt_LabourFvar
    global TimeEnt_LabourFvar
    global DateEnt_LabourFvar
    global PlaceEnt_LabourFvar
    global WagesEnt_LabourFvar
    global AdvanceEnt_LabourFvar

    NameEnt_LabourFvar = StringVar()
    InformEnt_LabourFvar = StringVar()
    TimeEnt_LabourFvar = StringVar()
    DateEnt_LabourFvar = StringVar()
    PlaceEnt_LabourFvar = StringVar()
    WagesEnt_LabourFvar = StringVar()
    AdvanceEnt_LabourFvar = StringVar()


    Companylbl_LabourF = Label(Anewframe, text="COMPANY NAME :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Companylbl_LabourF.place(x=130, y=30)

    Company_LabourVar = StringVar(Anewframe)
    Company_LabourVar.set(CompanyList[0])
    selectcompany = OptionMenu(Anewframe, Company_LabourVar, *CompanyList)
    selectcompany.config(width=30, height=2, font=('Helvetica', 8))
    selectcompany.place(x=280, y=20)

    NameLbl_LabourF = Label(Anewframe, text="Employee Name :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    NameLbl_LabourF.place(x=130, y=80)

    NameEnt_LabourF = Entry(Anewframe, width=35, textvariable=NameEnt_LabourFvar)
    NameEnt_LabourF.place(x=280, y=85)

    InformLbl_LabourF = Label(Anewframe, text="Informer :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    InformLbl_LabourF.place(x=130, y=120)

    InformEnt_LabourF = Entry(Anewframe, width=35, textvariable=InformEnt_LabourFvar)
    InformEnt_LabourF.place(x=280, y=125)
    #
    # timeLbl1 = Label(Anewframe, text="9AM - 6PM :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    # timeLbl1.place(x=130, y=140)
    #
    # global Radioobject
    # Radioobject1 = StringVar()
    # PresentRadio = Radiobutton(Anewframe, text="Present", variable=Radioobject1, value="Present")
    # PresentRadio.place(x=280, y=140)
    # PresentRadio.select()
    # AbsentRadio = Radiobutton(Anewframe, text="Absent", variable=Radioobject1, value="Absent")
    # AbsentRadio.place(x=380, y=140)
    #
    # timeLbl2 = Label(Anewframe, text="6PM - 9PM :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    # timeLbl2.place(x=130, y=180)
    #
    # global Radioobject2
    # Radioobject2 = StringVar()
    # PresentRadio = Radiobutton(Anewframe, text="Present", variable=Radioobject2, value="Present")
    # PresentRadio.place(x=280, y=180)
    # AbsentRadio = Radiobutton(Anewframe, text="Absent", variable=Radioobject2, value="Absent")
    # AbsentRadio.place(x=380, y=180)
    # AbsentRadio.select()
    #
    # timeLbl3 = Label(Anewframe, text="9PM - 12AM :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    # timeLbl3.place(x=130, y=220)
    #
    # global Radioobject3
    # Radioobject3 = StringVar()
    # PresentRadio = Radiobutton(Anewframe, text="Present", variable=Radioobject3, value="Present")
    # PresentRadio.place(x=280, y=220)
    # AbsentRadio = Radiobutton(Anewframe, text="Absent", variable=Radioobject3, value="Absent")
    # AbsentRadio.place(x=380, y=220)
    # AbsentRadio.select()
    #
    # FullnightLbl = Label(Anewframe, text="Full Night :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    # FullnightLbl.place(x=130, y=260)
    #
    # global Radioobject4
    # Radioobject4 = StringVar()
    # PresentRadio = Radiobutton(Anewframe, text="Present", variable=Radioobject4, value="Present")
    # PresentRadio.place(x=280, y=260)
    # AbsentRadio = Radiobutton(Anewframe, text="Absent", variable=Radioobject4, value="Absent")
    # AbsentRadio.place(x=380, y=260)
    # AbsentRadio.select()

    Timebl_LabourF = Label(Anewframe, text="Time :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Timebl_LabourF.place(x=130, y=160)

    TimeEnt_LabourF = Entry(Anewframe, width=35, textvariable=TimeEnt_LabourFvar)
    TimeEnt_LabourF.place(x=280, y=165)

    DateLbl_LabourF = Label(Anewframe, text="Date (DD-MM-YYYY) :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    DateLbl_LabourF.place(x=130, y=200)

    DateEnt_LabourF = Entry(Anewframe, width=35, textvariable=DateEnt_LabourFvar)
    DateEnt_LabourF.place(x=280, y=205)

    PlaceLbl_LabourF = Label(Anewframe, text="Place :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    PlaceLbl_LabourF.place(x=130, y=240)

    PlaceEnt_LabourF = Entry(Anewframe, width=35, textvariable=PlaceEnt_LabourFvar)
    PlaceEnt_LabourF.place(x=280, y=245)

    WagesLbl_LabourF = Label(Anewframe, text="Wages :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    WagesLbl_LabourF.place(x=130, y=280)

    WagesEnt_LabourF = Entry(Anewframe, width=35, textvariable=WagesEnt_LabourFvar)
    WagesEnt_LabourF.place(x=280, y=285)

    AdvanceLbl_LabourF = Label(Anewframe, text="Advance :", font=('Arial', 10, 'bold'), padx=5, pady=5)
    AdvanceLbl_LabourF.place(x=130, y=320)

    AdvanceEnt_LabourF = Entry(Anewframe, width=35, textvariable=AdvanceEnt_LabourFvar)
    AdvanceEnt_LabourF.place(x=280, y=325)

    def Get_Submit_LabourF():
        print(Company_LabourVar.get(), NameEnt_LabourF.get(), InformEnt_LabourF.get(), TimeEnt_LabourF.get(), DateEnt_LabourF.get(), PlaceEnt_LabourF.get(),
              WagesEnt_LabourF.get(), AdvanceEnt_LabourF.get())

    Submit_LabourF = Button(Anewframe, text="Submit", font=('Arial', 10, 'bold'), width=15, height=2, command=Get_Submit_LabourF)
    Submit_LabourF.place(x=170, y=380)

    def clear_Clear_LabourF():
        NameEnt_LabourFvar.set("")
        InformEnt_LabourFvar.set("")
        TimeEnt_LabourFvar.set("")
        DateEnt_LabourFvar.set("")
        PlaceEnt_LabourFvar.set("")
        WagesEnt_LabourFvar.set("")
        AdvanceEnt_LabourFvar.set("")
        Company_LabourVar.set(CompanyList[0])


    Clear_LabourF = Button(Anewframe, text="Clear", font=('Arial', 10, 'bold'), width=15, height=2, command=clear_Clear_LabourF)
    Clear_LabourF.place(x=340, y=380)

    # Stocks Frame

    tabcontrol = ttk.Notebook(frame5)

    Stock_tab1 = Frame(tabcontrol)
    Stock_tab2 = Frame(tabcontrol)
    Stock_tab3 = Frame(tabcontrol)
    Stock_tab4 = Frame(tabcontrol)

    tabcontrol.add(Stock_tab1, text="Item Master")
    tabcontrol.add(Stock_tab2, text="Incoming")
    tabcontrol.add(Stock_tab3, text="Outcoming")
    tabcontrol.add(Stock_tab4, text="Reports")

    tabcontrol.pack(expand=1, fill="both")

    # Item master Tab
    ItemNo_Stock = Label(Stock_tab1, text="Item No", font=('Arial', 10, 'bold'), padx=5, pady=5)
    ItemNo_Stock.place(x=50, y=40)
    Description_Stock = Label(Stock_tab1, text="Description", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Description_Stock.place(x=330, y=40)
    Unit_Stock = Label(Stock_tab1, text="Unit", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Unit_Stock.place(x=650, y=40)

    ItemNoEntry_Stock = Entry(Stock_tab1, width=25)
    ItemNoEntry_Stock.place(x=130, y=44)
    DescriptionEntry_Stock = Entry(Stock_tab1, width=25)
    DescriptionEntry_Stock.place(x=440, y=44)
    UnitEntry_Stock = Entry(Stock_tab1, width=25)
    UnitEntry_Stock.place(x=720, y=44)

    Add_buttonStock = Button(Stock_tab1, text="Add", width=13, height=1)
    Add_buttonStock.place(x=300, y=100)

    Delete_buttonStock = Button(Stock_tab1, text="Delete", width=13, height=1)
    Delete_buttonStock.place(x=470, y=100)

    Stock_treev = ttk.Treeview(Stock_tab1)
    style_stock = ttk.Style(Stock_tab1)
    style_stock.configure('Treeview', rowheight=30)
    Stock_treev.place(x=50, y=150)

    StockItem_scrollbar = ttk.Scrollbar(Stock_tab1, orient="vertical", command=Stock_treev.yview)
    StockItem_scrollbar.place(x=933, y=187, height=235)

    # Stock_treev.configure(yscrollcommand=verticalscrlbar.set, height=10)
    Stock_treev["columns"] = ("1", "2", "3", "4")

    Stock_treev['show'] = 'headings'
    Stock_treev.column("1", width=220, anchor='c')
    Stock_treev.column("2", width=220, anchor='c')
    Stock_treev.column("3", width=220, anchor='c')
    Stock_treev.column("4", width=220, anchor='c')

    Stock_treev.heading("1", text="Sr.No")
    Stock_treev.heading("2", text="Item No")
    Stock_treev.heading("3", text="Description")
    Stock_treev.heading("4", text="Unit")

    # Incoming Tab

    Select_ItemFrame_Incoming = LabelFrame(Stock_tab2, text="Select Item", heigh=520, width=170)
    Select_ItemFrame_Incoming.place(x=0, y=10)

    Incoming_ItemFrame = LabelFrame(Stock_tab2, text="Incoming Item", height=210, width=810)
    Incoming_ItemFrame.place(x=172, y=10)

    Treeview_IncomingItem = LabelFrame(Stock_tab2, text="Details", height=260, width=810)
    Treeview_IncomingItem.place(x=172, y=220)

    #Select_ItemFrame Incoming
    listbox_Incoming = Listbox(Select_ItemFrame_Incoming, width=26, height=31)
    listbox_Incoming.insert(1, "Python")
    listbox_Incoming.insert(2, "Perl")
    listbox_Incoming.insert(3, "C")
    listbox_Incoming.insert(4, "PHP")
    listbox_Incoming.insert(5, "JSP")
    listbox_Incoming.insert(6, "Ruby")
    listbox_Incoming.place(x=0, y=0)



    #Incoming_ItemFrame
    Date_LblIncoming = Label(Incoming_ItemFrame, text="Date (DD-MM-YYYY)", font=('Arial', 10, 'bold'), padx=5, pady=5)
    ItemCode_LblIncoming = Label(Incoming_ItemFrame, text="Item Code", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Description_LblIncoming = Label(Incoming_ItemFrame, text="Description", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Unit_LblIncoming = Label(Incoming_ItemFrame, text="Unit", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Rate_LblIncoming = Label(Incoming_ItemFrame, text="Rate", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Quantity_LblIncoming = Label(Incoming_ItemFrame, text="Quantity", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Remarks_LblIncoming = Label(Incoming_ItemFrame, text="Remarks", font=('Arial', 10, 'bold'), padx=5, pady=5)

    Date_LblIncoming.place(x=45, y=5)
    ItemCode_LblIncoming.place(x=45, y=38)
    Description_LblIncoming.place(x=45, y=73)
    Unit_LblIncoming.place(x=45, y=108)
    Rate_LblIncoming.place(x=400, y=5)
    Quantity_LblIncoming.place(x=400, y=38)
    Remarks_LblIncoming.place(x=400, y=73)

    Date_EntIncoming = Entry(Incoming_ItemFrame, width=25)
    ItemCode_EntIncoming = Entry(Incoming_ItemFrame, width=25)
    Description_EntIncoming = Entry(Incoming_ItemFrame, width=25)
    Unit_EntIncoming = Entry(Incoming_ItemFrame, width=25)
    Rate_EntIncoming = Entry(Incoming_ItemFrame, width=25)
    Quantity_EntIncoming = Entry(Incoming_ItemFrame, width=25)
    Remarks_EntIncoming = Entry(Incoming_ItemFrame, width=25)

    Date_EntIncoming.place(x=180, y=7)
    ItemCode_EntIncoming.place(x=180, y=40)
    Description_EntIncoming.place(x=180, y=75)
    Unit_EntIncoming.place(x=180, y=110)
    Rate_EntIncoming.place(x=470, y=5)
    Quantity_EntIncoming.place(x=470, y=40)
    Remarks_EntIncoming.place(x=470, y=75)

    Cancel_buttonIncoming = Button(Incoming_ItemFrame, text="Cancel", width=10)
    Cancel_buttonIncoming.place(x=200, y=150)

    Save_buttonIncoming = Button(Incoming_ItemFrame, text="Save", width=10)
    Save_buttonIncoming.place(x=350, y=150)

    Incoming_treev = ttk.Treeview(Treeview_IncomingItem)
    style1 = ttk.Style(Treeview_IncomingItem)
    style1.configure('Treeview', rowheight=10)
    Incoming_treev.place(x=20, y=5)

    In_scrollbar = ttk.Scrollbar(Treeview_IncomingItem, orient="vertical", command=Incoming_treev.yview)
    In_scrollbar.place(x=783, y=5, height=233)

    # Incoming_treev.configure(yscrollcommand=verticalscrlbar.set, height=10)
    Incoming_treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    Incoming_treev['show'] = 'headings'
    Incoming_treev.column("1", width=95, anchor='c')
    Incoming_treev.column("2", width=95, anchor='c')
    Incoming_treev.column("3", width=95, anchor='c')
    Incoming_treev.column("4", width=95, anchor='c')
    Incoming_treev.column("5", width=95, anchor='c')
    Incoming_treev.column("6", width=95, anchor='c')
    Incoming_treev.column("7", width=95, anchor='c')
    Incoming_treev.column("8", width=95, anchor='c')

    Incoming_treev.heading("1", text="Sr.No")
    Incoming_treev.heading("2", text="Date")
    Incoming_treev.heading("3", text="Item Code")
    Incoming_treev.heading("4", text="Description")
    Incoming_treev.heading("5", text="Unit")
    Incoming_treev.heading("6", text="Rate")
    Incoming_treev.heading("7", text="Quantity")
    Incoming_treev.heading("8", text="Remark")

    Incoming_treev.insert("", 'end', text="L1",
                 values=("Nidhi", "F", "25", "1234","rohit",234,"trty",9))
    Incoming_treev.insert("", 'end', text="L2",
                 values=("Nisha", "F", "23", "5678"))
    Incoming_treev.insert("", 'end', text="L3",
                 values=("Preeti", "F", "27", "9012"))
    Incoming_treev.insert("", 'end', text="L4",
                 values=("Rahul", "M", "20", "123456"))
    Incoming_treev.insert("", 'end', text="L5",
                 values=("Nidhi", "F", "25"))
    Incoming_treev.insert("", 'end', text="L6",
                 values=("Nisha", "F", "23"))
    Incoming_treev.insert("", 'end', text="L7",
                 values=("Preeti", "F", "27"))
    Incoming_treev.insert("", 'end', text="L8",
                 values=("Rahul", "M", "20"))
    Incoming_treev.insert("", 'end', text="L9",
                 values=("Nidhi", "F", "25"))
    Incoming_treev.insert("", 'end', text="L10",
                 values=("Nisha", "F", "23"))
    Incoming_treev.insert("", 'end', text="L11",
                 values=("Preeti", "F", "27"))
    Incoming_treev.insert("", 'end', text="L12",
                 values=("Rahul", "M", "20"))

    Deletetree_buttonIncoming = Button(Stock_tab2, text="Cancel", width=10)
    Deletetree_buttonIncoming.place(x=470, y=490)

    Edittree_buttonIncoming = Button(Stock_tab2, text="Save", width=10)
    Edittree_buttonIncoming.place(x=590, y=490)

    # Outgoing Frame in Outgoing Tab

    Select_ItemFrame_Outcoming = LabelFrame(Stock_tab3, text="Select Item", heigh=520, width=170)
    Select_ItemFrame_Outcoming.place(x=0, y=10)

    #Select_ItemFrame Incoming
    listbox_Incoming = Listbox(Select_ItemFrame_Outcoming, width=26, height=31)
    listbox_Incoming.insert(1, "Python")
    listbox_Incoming.insert(2, "Perl")
    listbox_Incoming.insert(3, "C")
    listbox_Incoming.insert(4, "PHP")
    listbox_Incoming.insert(5, "JSP")
    listbox_Incoming.insert(6, "Ruby")
    listbox_Incoming.place(x=0, y=0)

    Outgoing_ItemFrame = LabelFrame(Stock_tab3, text="Outgoing Item", height=210, width=810)
    Outgoing_ItemFrame.place(x=172, y=10)

    Treeview_OutgoingItem = LabelFrame(Stock_tab3, text="Details", height=260, width=810)
    Treeview_OutgoingItem.place(x=172, y=220)

    Date_LblIncoming = Label(Outgoing_ItemFrame, text="Date (DD-MM-YYYY)", font=('Arial', 10, 'bold'), padx=5, pady=5)
    ItemCode_LblIncoming = Label(Outgoing_ItemFrame, text="Item Code", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Description_LblIncoming = Label(Outgoing_ItemFrame, text="Description", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Unit_LblIncoming = Label(Outgoing_ItemFrame, text="Unit", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Rate_LblIncoming = Label(Outgoing_ItemFrame, text="Rate", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Quantity_LblIncoming = Label(Outgoing_ItemFrame, text="Quantity", font=('Arial', 10, 'bold'), padx=5, pady=5)
    Remarks_LblIncoming = Label(Outgoing_ItemFrame, text="Remarks", font=('Arial', 10, 'bold'), padx=5, pady=5)

    Date_LblIncoming.place(x=45, y=5)
    ItemCode_LblIncoming.place(x=45, y=38)
    Description_LblIncoming.place(x=45, y=73)
    Unit_LblIncoming.place(x=45, y=108)
    Rate_LblIncoming.place(x=400, y=5)
    Quantity_LblIncoming.place(x=400, y=38)
    Remarks_LblIncoming.place(x=400, y=73)

    Date_EntIncoming = Entry(Outgoing_ItemFrame, width=25)
    ItemCode_EntIncoming = Entry(Outgoing_ItemFrame, width=25)
    Description_EntIncoming = Entry(Outgoing_ItemFrame, width=25)
    Unit_EntIncoming = Entry(Outgoing_ItemFrame, width=25)
    Rate_EntIncoming = Entry(Outgoing_ItemFrame, width=25)
    Quantity_EntIncoming = Entry(Outgoing_ItemFrame, width=25)
    Remarks_EntIncoming = Entry(Outgoing_ItemFrame, width=25)

    Date_EntIncoming.place(x=180, y=7)
    ItemCode_EntIncoming.place(x=180, y=40)
    Description_EntIncoming.place(x=180, y=75)
    Unit_EntIncoming.place(x=180, y=110)
    Rate_EntIncoming.place(x=470, y=5)
    Quantity_EntIncoming.place(x=470, y=40)
    Remarks_EntIncoming.place(x=470, y=75)

    Cancel_buttonIncoming = Button(Outgoing_ItemFrame, text="Cancel", width=10)
    Cancel_buttonIncoming.place(x=200, y=150)

    Save_buttonIncoming = Button(Outgoing_ItemFrame, text="Save", width=10)
    Save_buttonIncoming.place(x=350, y=150)

    Outgoing_treev = ttk.Treeview(Treeview_OutgoingItem)
    style2 = ttk.Style(Treeview_OutgoingItem)
    style2.configure('Treeview', rowheight=10)
    Outgoing_treev.place(x=20, y=5)

    out_scrollbar = ttk.Scrollbar(Treeview_OutgoingItem, orient="vertical", command=Outgoing_treev.yview)
    out_scrollbar.place(x=783, y=5, height=233)

    # Incoming_treev.configure(yscrollcommand=verticalscrlbar.set, height=10)
    Outgoing_treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    Outgoing_treev['show'] = 'headings'
    Outgoing_treev.column("1", width=95, anchor='c')
    Outgoing_treev.column("2", width=95, anchor='c')
    Outgoing_treev.column("3", width=95, anchor='c')
    Outgoing_treev.column("4", width=95, anchor='c')
    Outgoing_treev.column("5", width=95, anchor='c')
    Outgoing_treev.column("6", width=95, anchor='c')
    Outgoing_treev.column("7", width=95, anchor='c')
    Outgoing_treev.column("8", width=95, anchor='c')

    Outgoing_treev.heading("1", text="Sr.No")
    Outgoing_treev.heading("2", text="Date")
    Outgoing_treev.heading("3", text="Item Code")
    Outgoing_treev.heading("4", text="Description")
    Outgoing_treev.heading("5", text="Unit")
    Outgoing_treev.heading("6", text="Rate")
    Outgoing_treev.heading("7", text="Quantity")
    Outgoing_treev.heading("8", text="Remark")

    Outgoing_treev.insert("", 'end', text="L1",
                          values=("Nidhi", "F", "25", "1234", "rohit", 234, "trty", 9))
    Outgoing_treev.insert("", 'end', text="L2",
                          values=("Nisha", "F", "23", "5678"))
    Outgoing_treev.insert("", 'end', text="L3",
                          values=("Preeti", "F", "27", "9012"))
    Outgoing_treev.insert("", 'end', text="L4",
                          values=("Rahul", "M", "20", "123456"))
    Outgoing_treev.insert("", 'end', text="L5",
                          values=("Nidhi", "F", "25"))
    Outgoing_treev.insert("", 'end', text="L6",
                          values=("Nisha", "F", "23"))
    Outgoing_treev.insert("", 'end', text="L7",
                          values=("Preeti", "F", "27"))
    Outgoing_treev.insert("", 'end', text="L8",
                          values=("Rahul", "M", "20"))
    Outgoing_treev.insert("", 'end', text="L9",
                          values=("Nidhi", "F", "25"))
    Outgoing_treev.insert("", 'end', text="L10",
                          values=("Nisha", "F", "23"))
    Outgoing_treev.insert("", 'end', text="L11",
                          values=("Preeti", "F", "27"))
    Outgoing_treev.insert("", 'end', text="L12",
                          values=("Rahul", "M", "20"))

    Deletetree_buttonIncoming = Button(Stock_tab3, text="Cancel", width=10)
    Deletetree_buttonIncoming.place(x=470, y=490)

    Edittree_buttonIncoming = Button(Stock_tab3, text="Save", width=10)
    Edittree_buttonIncoming.place(x=590, y=490)

    # Stock report

    StockReport_Lbl = Label(Stock_tab4, text="STOCK REPORT", font=('Arial', 16, 'bold'), padx=5, pady=5)
    StockReport_Lbl.place(x=400, y=30)

    Reports_treev = ttk.Treeview(Stock_tab4)
    style3 = ttk.Style(Stock_tab4)
    style3.configure('Treeview', rowheight=30)
    Reports_treev.place(x=40, y=80)
    #
    # Stocksscrlbar = ttk.Scrollbar(emplistframe)
    # Stocksscrlbar.place(x=25, y=140)
    # Stocksscrlbar.config(yscrollcommand=Reports_treev.yview)

    # disyscroll = ttk.Scrollbar(Stock_tab4, command=Reports_treev.yview)
    # disyscroll.pack(side='left', fill='y')
    # Reports_treev.config(yscrollcommand=disyscroll.set)

    # Stocksscrlbar.place(x=25,y=140)

    vsb = ttk.Scrollbar(Stock_tab4, orient="vertical", command=Reports_treev.yview)
    vsb.place(x=943, y=83, height=333)

    # Incoming_treev.configure(yscrollcommand=verticalscrlbar.set, height=10)
    Reports_treev["columns"] = ("1", "2", "3", "4", "5", "6", "7")

    Reports_treev['show'] = 'headings'
    Reports_treev.column("1", width=50, anchor='c')
    Reports_treev.column("2", width=100, anchor='c')
    Reports_treev.column("3", width=150, anchor='c')
    Reports_treev.column("4", width=150, anchor='c')
    Reports_treev.column("5", width=150, anchor='c')
    Reports_treev.column("6", width=150, anchor='c')
    Reports_treev.column("7", width=150, anchor='c')

    Reports_treev.heading("1", text="Sr.No")
    Reports_treev.heading("2", text="Item Code")
    Reports_treev.heading("3", text="Description")
    Reports_treev.heading("4", text="Unit")
    Reports_treev.heading("5", text="IN")
    Reports_treev.heading("6", text="OUT")
    Reports_treev.heading("7", text="Balance")

    Export_btn = Button(Stock_tab4, text="Export", width=20)
    Export_btn.place(x=400, y=420)

    dashboard_Screen.mainloop()


def condition_register(event):
    # username1 = admin_username.get()
    # password1 = admin_Password.get()
    if admin_username.get() == "admin" and admin_Password.get() == "admin":
        # messagebox.showinfo(title="Success...!",message="verification Success for admin..!",default=Register)
        response = messagebox.askokcancel("Are you sure", "OK or Cancel?")
        if response:
            Register()
            register_verify_screen.destroy()

        # print(response)
        # register_verify_success()
    else:
        # register_verify_deny
        messagebox.showerror(title="Error", message="Please check your username and password")


def register_verify(event):
    global admin_username
    global admin_Password
    global register_verify_screen

    admin_username = StringVar()
    admin_Password = StringVar()

    register_verify_screen = Toplevel()
    register_verify_screen.title("Admin verification")
    register_verify_screen.geometry("300x150+500+200")
    # Label(screen2,text="Username :",font=("calibre",13)).place(x=20,y=15)
    register_verify_screen.resizable(False, False)
    Label(register_verify_screen, text='Username', font=('calibre', 10, 'bold')).place(x=20, y=15)

    admin_username = Entry(register_verify_screen)
    admin_username.place(x=120, y=15)
    admin_username.focus_set()

    Label(register_verify_screen, text='Password', font=('calibre', 10, 'bold')).place(x=20, y=45)

    admin_Password = Entry(register_verify_screen, show="*")
    admin_Password.place(x=120, y=45)
    admin_Password.bind("<Return>", condition_register)

    register_verify_SubmitBtn = Button(register_verify_screen, text="Submit", width=12)
    register_verify_SubmitBtn.place(x=50, y=90)
    register_verify_SubmitBtn.bind("<Return>", condition_register)
    register_verify_SubmitBtn.bind("<Button-1>", condition_register)
    Button(register_verify_screen, text="Cancel", width=12, command=register_verify_screen.destroy).place(x=150, y=90)

    # admin_Password.bind('<Return>',command1)


def register_user():
    data = {}

    screen1.destroy()
    username_info = username.get()
    password_info = password.get()
    # data[username_info] = []
    data[username_info] = {
        "Username": username_info,
        "Password": password_info
    }

    # file = open("Credentials" + ".txt", "a")
    # file.write(username_info+"\n")
    # file.write(password_info)
    # json.dump(data, file)
    # file.write(",")
    # file.write("\n")
    # file.close()
    # data.clear()

    # username_entry.delete(0, END)
    # password_entry.delete(0, END)
    # confirm_entry.delete(0,END)

    messagebox.showinfo("Success", "Registration Success")

    # Label(screen2, text="Registration Success", fg="green", font=("calibri", 11)).place(x=45,y=200)


def login_verification(event):
    try:
        if VoucherBackend.user_login(login_Username.get(), login_Password.get()):
            print("success")
            screen.destroy()
            dashboard_page()

        else:
            messagebox.showerror("Error", "Invalid User and Password...!")
            screen2.destroy()
            print("DATA NOT FOUND")
    except:
        messagebox.showerror("Error", "Sorry User Not found...!")

    # login_U = StringVar()
    # login_P = StringVar()
    # print("In Login Varification function.")
    # username_verify = login_U.get()
    # password_verify = login_P.get()
    # try:
    # file = open("Credentials.txt", "r")
    # print(file.read())
    # if username_verify in file:
    #     # file=open("Credentials.txt","r")
    #     verify = file.read()
    #     if password_verify in verify:
    #         messagebox.showinfo(title="Success...!", message="verification Success... !")
    #         else:
    #             print("password has not been recognized")
    #     else:
    #         print("username not found")
    #
    #     file.close()
    #
    # except Exception as e:
    #     print("ERROR RAISED HERE: -", e)

    # finally:
    #     print("file closed")

    # list_of_files = os.listdir()

    # for i in file:
    # print("data: -",i)
    # print(file.read())

    # file.close()


def login(event):
    global login_Username
    global login_Password
    global screen2

    login_U = StringVar()
    login_P = StringVar()

    # print("Login here ")
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x150+500+200")
    screen2.resizable(False, False)
    # Label(screen2,text="Username :",font=("calibre",13)).place(x=20,y=15)
    Label(screen2, text='Username', font=('calibre', 10, 'bold')).place(x=20, y=15)

    login_Username = Entry(screen2, textvariable=login_U)
    login_Username.place(x=120, y=15)
    login_Username.focus_set()

    Label(screen2, text='Password', font=('calibre', 10, 'bold')).place(x=20, y=45)

    login_Password = Entry(screen2, show="*", textvariable=login_P)
    login_Password.place(x=120, y=45)
    login_Password.bind("<Return>", login_verification)

    login_SubmitBtn = Button(screen2, text="Login", width=12)
    login_SubmitBtn.place(x=50, y=90)
    login_SubmitBtn.bind("<Return>", login_verification)
    login_SubmitBtn.bind("<Button-1>", login_verification)

    Button(screen2, text="Cancel", width=12, command=screen2.destroy).place(x=150, y=90)


def register_valid(event):
    # register_user()
    if username_entry.get() == "" and password_entry.get() == "" and confirm_entry.get() == "":
        messagebox.showinfo(title="Warning...!", message="Something is missing!")
        print("in if")
    elif password_entry.get() != confirm_entry.get():
        messagebox.showinfo(title="Warning...!", message="Renetered password is incorrect!")
        print(" in elif")
    else:
        print(f"in else Values: - {type(username_entry.get())}, and {type(password_entry.get())}")
        VoucherBackend.register_user(username_entry.get(), password_entry.get())
        register_user()


def Register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Registration")
    screen1.geometry("300x250+500+200")
    global username
    global password
    global username_entry
    global password_entry
    global confirm_entry

    username = StringVar()
    password = StringVar()
    confirm_pass = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()

    username_lable = Label(screen1, text="Username * ")
    username_lable.place(x=20, y=50)

    username_entry = Entry(screen1, textvariable=username)
    username_entry.place(x=140, y=50)
    username_entry.focus_set()

    password_lable = Label(screen1, text="Password * ")
    password_lable.place(x=20, y=90)

    password_entry = Entry(screen1, textvariable=password, show='*')
    password_entry.place(x=140, y=90)

    confirm_lable = Label(screen1, text="Confirm password * ")
    confirm_lable.place(x=20, y=130)

    confirm_entry = Entry(screen1, textvariable=confirm_pass, show='*')
    confirm_entry.place(x=140, y=130)
    confirm_entry.bind("<Return>", register_valid)

    Register_SubmitBtn = Button(screen1, text="Register", width=12)
    Register_SubmitBtn.place(x=45, y=180)
    Register_SubmitBtn.bind("<Return>", register_valid)
    Register_SubmitBtn.bind("<Button-1>", register_valid)
    Button(screen1, text="Cancel", width=12, command=screen1.destroy).place(x=155, y=180)


def startPage():
    global screen1
    global admin_username
    global admin_Password
    global screen
    screen = Tk()
    label = Label(screen, text="Om Shree Ganeshaya namah...!", width="45", height="2", fg="green",
                  font=("calibre", 13)).pack()
    # label.place(x=0,y=5)

    bg_image = PhotoImage(file="ganpati-bappa003.png")
    x = Label(image=bg_image)
    x.place(x=40, y=40)

    loginbtn = Button(screen, text="Login", width=20)
    loginbtn.place(x=80, y=300)
    loginbtn.focus_set()

    loginbtn.bind("<Return>", login)
    loginbtn.bind("<Button-1>", login)

    registerbtn = Button(screen, text="Register", width=20)
    registerbtn.place(x=80, y=340)
    registerbtn.bind("<Return>", register_verify)
    registerbtn.bind("<Button-1>", register_verify)

    screen.title("Make Virtual Vouchers")

    print(f"Width: - {screen.winfo_reqwidth()} and Height: - {screen.winfo_reqheight()}")

    width = "300"
    height = "400"
    screen.geometry(f"{width}x{height}+500+100")
    screen.resizable(False, False)
    screen.iconify()
    screen.mainloop()


startPage()

# Flow of the program:-
# login function>login_verification function>dashboard_page function
# register function>register_verify function>condition_register function>Register function>register_valid function>
# register_user function
