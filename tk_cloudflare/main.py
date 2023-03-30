#-*- coding:utf-8 -*-

import os, sys
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    import CloudFlare as cloudflare
    from MyCloudFlare import  mycloudflare
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()


class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('1275x699')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame5.TLabelframe', font=('SimSun',9))
        self.style.configure('TFrame5.TLabelframe.Label', font=('SimSun',9))
        self.Frame5 = LabelFrame(self.top, text='Frame5', style='TFrame5.TLabelframe')
        self.Frame5.place(relx=0.659, rely=0.652, relwidth=0.333, relheight=0.139)

        self.style.configure('TFrame4.TLabelframe', font=('SimSun',9))
        self.style.configure('TFrame4.TLabelframe.Label', font=('SimSun',9))
        self.Frame4 = LabelFrame(self.top, text='Frame4', style='TFrame4.TLabelframe')
        self.Frame4.place(relx=0.339, rely=0.492, relwidth=0.302, relheight=0.31)

        self.style.configure('TFrame3.TLabelframe', font=('SimSun',9))
        self.style.configure('TFrame3.TLabelframe.Label', font=('SimSun',9))
        self.Frame3 = LabelFrame(self.top, text='Frame3', style='TFrame3.TLabelframe')
        self.Frame3.place(relx=0.659, rely=0.011, relwidth=0.333, relheight=0.631)

        self.style.configure('TFrame2.TLabelframe', font=('SimSun',9))
        self.style.configure('TFrame2.TLabelframe.Label', font=('SimSun',9))
        self.Frame2 = LabelFrame(self.top, text='Frame2', style='TFrame2.TLabelframe')
        self.Frame2.place(relx=0.339, rely=0.011, relwidth=0.302, relheight=0.471)

        self.style.configure('TdomainListFrame.TLabelframe', font=('SimSun',9))
        self.style.configure('TdomainListFrame.TLabelframe.Label', font=('SimSun',9))
        self.domainListFrame = LabelFrame(self.top, text='domainList', style='TdomainListFrame.TLabelframe')
        self.domainListFrame.place(relx=0.006, rely=0.011, relwidth=0.315, relheight=0.791)

        self.searchVar = StringVar(value='search')
        self.style.configure('Tsearch.TButton', font=('SimSun',9))
        self.search = Button(self.Frame5, text='search', textvariable=self.searchVar, command=self.search_Cmd, style='Tsearch.TButton')
        self.search.setText = lambda x: self.searchVar.set(x)
        self.search.text = lambda : self.searchVar.get()
        self.search.place(relx=0.433, rely=0.247, relwidth=0.209, relheight=0.258)

        self.Text4Var = StringVar(value='Text4')
        self.Text4 = Entry(self.Frame3, textvariable=self.Text4Var, font=('SimSun',9))
        self.Text4.setText = lambda x: self.Text4Var.set(x)
        self.Text4.text = lambda : self.Text4Var.get()
        self.Text4.place(relx=0.188, rely=0.816, relwidth=0.511, relheight=0.057)

        self.Combo1List = ['A','CNAME','TXT']
        self.Combo1Var = StringVar(value='A')
        self.Combo1 = Combobox(self.Frame3, textvariable=self.Combo1Var, values=self.Combo1List, font=('SimSun',9))
        self.Combo1.setText = lambda x: self.Combo1Var.set(x)
        self.Combo1.text = lambda : self.Combo1Var.get()
        self.Combo1.place(relx=0.056, rely=0.925, relwidth=0.247)

        self.Command1Var = StringVar(value='Command1')
        self.style.configure('TCommand1.TButton', font=('SimSun',9))
        self.Command1 = Button(self.Frame3, text='Command1', textvariable=self.Command1Var, command=self.add_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.772, rely=0.925, relwidth=0.191, relheight=0.057)

        self.Text3Var = StringVar(value='Text3')
        self.Text3 = Entry(self.Frame3, textvariable=self.Text3Var, font=('SimSun',9))
        self.Text3.setText = lambda x: self.Text3Var.set(x)
        self.Text3.text = lambda : self.Text3Var.get()
        self.Text3.place(relx=0.188, rely=0.744, relwidth=0.793, relheight=0.057)

       
        self.Text1 = Text(self.Frame3, font=('SimSun',9))
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.019, rely=0.036, relwidth=0.962, relheight=0.692)

        self.getdomainVar = StringVar(value='getdomain')
        self.style.configure('Tgetdomain.TButton', font=('SimSun',9))
        self.getdomain = Button(self.Frame5, text='getdomain', textvariable=self.getdomainVar, command=self.getdomain_Cmd, style='Tgetdomain.TButton')
        self.getdomain.setText = lambda x: self.getdomainVar.set(x)
        self.getdomain.text = lambda : self.getdomainVar.get()
        self.getdomain.place(relx=0.038, rely=0.577, relwidth=0.209, relheight=0.258)

        self.Label1Var = StringVar(value='Label1')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('SimSun',9))
        self.Label1 = Label(self.Frame2, text='Label1', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.042, rely=0.073, relwidth=0.917, relheight=0.878)

        self.Text2Var = StringVar(value='输入要查找的域名')
        self.Text2 = Entry(self.Frame5, textvariable=self.Text2Var, font=('SimSun',9))
        self.Text2.setText = lambda x: self.Text2Var.set(x)
        self.Text2.text = lambda : self.Text2Var.get()
        self.Text2.place(relx=0.038, rely=0.247, relwidth=0.379, relheight=0.258)



        self.Label2Var = StringVar(value='前缀')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('SimSun',9))
        self.Label2 = Label(self.Frame3, text='Label2', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.056, rely=0.762, relwidth=0.096, relheight=0.039)

        self.Label3Var = StringVar(value='解析值')
        self.style.configure('TLabel3.TLabel', anchor='w', font=('SimSun',9))
        self.Label3 = Label(self.Frame3, text='Label3', textvariable=self.Label3Var, style='TLabel3.TLabel')
        self.Label3.setText = lambda x: self.Label3Var.set(x)
        self.Label3.text = lambda : self.Label3Var.get()
        self.Label3.place(relx=0.056, rely=0.834, relwidth=0.096, relheight=0.039)

        self.Command2Var = StringVar(value='add')
        self.style.configure('TCommand2.TButton', font=('SimSun',9))
        self.Command2 = Button(self.Frame3, text='add', textvariable=self.Command2Var, command=self.add_Cmd, style='TCommand2.TButton')
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda : self.Command2Var.get()
        self.Command2.place(relx=0.565, rely=0.925, relwidth=0.191, relheight=0.057)

        self.Command3Var = StringVar(value='delete')
        self.style.configure('TCommand3.TButton', font=('SimSun',9))
        self.Command3 = Button(self.Frame5, text='delete', textvariable=self.Command3Var, command=self.Command3_Cmd, style='TCommand3.TButton')
        self.Command3.setText = lambda x: self.Command3Var.set(x)
        self.Command3.text = lambda : self.Command3Var.get()
        self.Command3.place(relx=0.301, rely=0.577, relwidth=0.191, relheight=0.258)


        #self.List1Var = StringVar(value='List1')
        self.List1Font = Font(font=('SimSun',9))
        #self.List1 = Listbox(self.domainListFrame, listvariable=self.List1Var, font=self.List1Font)
        self.List1 = Listbox(self.domainListFrame, font=self.List1Font)
        self.List1.place(relx=0.02, rely=0.029, relwidth=0.96, relheight=0.962)
        self.List1.bind('<<ListboxSelect>>', self.listbox_click)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
    # 获取全部域名 列表
    def getdomain_Cmd(self, event=None):
        domain_list=mycloudflare().get_all_domain()   
        for i in domain_list:  
            self.List1.insert("end",i)
        
    # 查询单个域名解析
    def search_Cmd(self, event=None):
        domain=self.Text2.get()
        print(domain)
        cf1=mycloudflare()
        list1=cf1.search_domain(domain)
        if list1 :
            print(list1)
            self.Label1Var.set("\n".join(list1))
        else:
            self.Label1Var.set("您的cloudflare账户上没有该域名 "+domain)


    # 列表框点击事件绑定函数  点击 域名列表
    def listbox_click(self, event=None):
        # 向文本区光标处插入列表框当前选中文本
        domain=self.List1.get(self.List1.curselection())
        cf1=mycloudflare()
        list1=cf1.search_domain(domain)
        print(list1)
        self.Label1Var.set("\n".join(list1))
    # 批量添加域名操作
    def add_Cmd(self, event=None):
        gettext=self.Text1.get("1.0",'end')
        domainlist=[i for i in gettext.split("\n") if i !=""]
        getName=self.Text3.get().split(",")
        getContent=self.Text4.get()
        getType=self.Combo1.get()
        for domain in domainlist:
            mycloudflare().addDomain(domain,getName,getType,getContent)

    
    # 删除单个域名操作
    def Command3_Cmd(self, event=None):
        domain=self.Text2.get()
        result=mycloudflare().delete_domain(domain)
        self.Label1Var.set(result)
        

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()



        #self.List1Var = StringVar(value='List1')
        ##self.List1Font = Font(font=('SimSun',9))
        #self.List1 = Listbox(self.domainListFrame, listvariable=self.List1Var, font=self.List1Font)
        ##self.List1 = Listbox(self.domainListFrame, font=self.List1Font)
        ##self.List1.place(relx=0.02, rely=0.029, relwidth=0.96, relheight=0.962)
        ##self.List1.bind('<<ListboxSelect>>', self.listbox_click)