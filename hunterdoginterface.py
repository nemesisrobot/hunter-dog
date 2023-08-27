from tkinter import *
from fundos_fiis import *
import tkinter.messagebox


class WindowAdd:
    def __init__(self, master=None):
        self.master = master
        self.font = ("Calibri", "8")
        
        self.containerAddFii = Frame(self.master)
        self.containerAddFii["padx"] = 50
        self.containerAddFii["pady"] = 25
        self.containerAddFii.pack()

        self.collectorstatus = Label(self.containerAddFii,text="Nome do Fundo",font=self.font)
        self.collectorstatus.pack()
        self.containerAddFiiText = Entry(self.containerAddFii)
        self.containerAddFiiText["width"]=30
        self.containerAddFiiText["font"]=self.font
        self.containerAddFiiText.pack(side=TOP)

        self.addnewfii = Button(self.containerAddFii)
        self.addnewfii["text"] = "Salvar"
        self.addnewfii["font"] = ("Calibri", "8")
        self.addnewfii["width"] = 15
        self.addnewfii.bind("<Button-1>", self.addStock)
        self.addnewfii.pack(side=LEFT)

    def addStock(self, event):
        try:
            fii = FiisCad("base.db")
            fii.addFiis(self.containerAddFiiText.get())
            tkinter.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
        except:
            tkinter.messagebox.showinfo("Welcome to GFG.",  "Error")


class WindowBase:

    def __init__(self, master=None):
        self.master = master
        self.font = ("Calibri", "8")
        
        self.containerBaseProcess = Frame(self.master)
        self.containerBaseProcess
        self.containerBaseProcess["padx"] = 50
        self.containerBaseProcess["pady"] = 25
        self.containerBaseProcess.pack()

        self.collectorstatus = Label(self.containerBaseProcess,text="Gerar Base",font=self.font)
        self.collectorstatus.pack()

        self.cleanbase = Button(self.containerBaseProcess)
        self.cleanbase["text"] = " Limpa e Gera Base "
        self.cleanbase["font"] = ("Calibri", "8")
        self.cleanbase["width"] = 18
        self.cleanbase.bind("<Button-1>", self.cleanBase)
        self.cleanbase.pack(side=LEFT)

    def cleanBase(self, event):
        clear = DataBaseCreate()
        clear.start()



class Application:
    def __init__(self,master=None):
        self.master = master 

        #menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Gerar Base", command=self.cleanBaseData)
        fileMenu.add_command(label="Add Fiis", command=self.addFii)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="Base de Dados", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        #criando widget
        self.fontstandart = ("Arial","10")
        self.containerSettingVacancia = Frame(master)
        self.containerSettingVacancia["padx"] = 5
        self.containerSettingVacancia["pady"] = 25
        self.containerSettingVacancia.pack()


        self.containerSettingPVP = Frame(master)
        self.containerSettingPVP["padx"] = 50
        self.containerSettingPVP["pady"] = 25
        self.containerSettingPVP.pack()

        self.containerSettingLQ = Frame(master)
        self.containerSettingLQ["padx"] = 50
        self.containerSettingLQ["pady"] = 25
        self.containerSettingLQ.pack()

        self.containerStartProcess = Frame(master)
        self.containerStartProcess["padx"] = 50
        self.containerStartProcess["pady"] = 25
        self.containerStartProcess.pack()

        
        #criando labels e campos para vacancia , P/VP e Liquidez
        self.campoLabelVacancia = Label(self.containerSettingVacancia,text="Vacância % Minina:", font=self.fontstandart)
        self.campoLabelVacancia.pack(side=LEFT)
        self.vacanciavalue = Entry(self.containerSettingVacancia)
        self.vacanciavalue["width"]=20
        self.vacanciavalue["font"]=self.fontstandart
        self.vacanciavalue.pack(side=LEFT)

        self.campoLabelPVP = Label(self.containerSettingPVP,text="Min P/VP:", font=self.fontstandart)
        self.campoLabelPVP.pack(side=LEFT)
        self.pvpvaluemin = Entry(self.containerSettingPVP)
        self.pvpvaluemin["width"]=20
        self.pvpvaluemin["font"]=self.fontstandart
        self.pvpvaluemin.pack(side=LEFT)

        self.campoLabelPVP = Label(self.containerSettingPVP,text="Max P/VP:", font=self.fontstandart)
        self.campoLabelPVP.pack(side=LEFT)
        self.pvpvaluemax = Entry(self.containerSettingPVP)
        self.pvpvaluemax["width"]=20
        self.pvpvaluemax["font"]=self.fontstandart
        self.pvpvaluemax.pack(side=LEFT)

        self.campoLabelLQ = Label(self.containerSettingLQ,text="Liquidez Maior ou Igual:", font=self.fontstandart)
        self.campoLabelLQ.pack(side=LEFT)
        self.liquidezvalue = Entry(self.containerSettingLQ)
        self.liquidezvalue["width"]=30
        self.liquidezvalue["font"]=self.fontstandart
        self.liquidezvalue.pack(side=LEFT)

        self.collectorstatus = Label(self.containerStartProcess,text="Status:Aguardando", font=self.fontstandart)
        self.collectorstatus.pack()
        self.startProcess = Button(self.containerStartProcess)
        self.startProcess["text"] = "Start Coleta"
        self.startProcess["font"] = ("Calibri", "8")
        self.startProcess["width"] = 12
        self.startProcess.bind("<Button-1>", self.collectorData)
        self.startProcess.pack(side=LEFT)

        self.startAnalize = Button(self.containerStartProcess)
        self.startAnalize["text"] = "Start Analise"
        self.startAnalize["font"] = ("Calibri", "8")
        self.startAnalize["width"] = 12
        self.startAnalize.bind("<Button-1>", self.analiticDatas)
        self.startAnalize.pack(side=RIGHT)

        #self.vacancia = Entry(self.containerSetting)

    def collectorData(self, event):
        cld = ProcessCollector(self.collectorstatus)
        cld.start()

    def checknumber(self, valueparam):
        try:
            float(valueparam)
            return True
        except:
            tkinter.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
            return False

    def analiticDatas(self, event):
        vanc = self.checknumber(self.vacanciavalue.get())
        pvpmin = self.checknumber(self.pvpvaluemin.get())
        liqui = self.checknumber(self.liquidezvalue.get())
        pvpmax = self.checknumber(self.pvpvaluemax.get())

        if(vanc==True and pvpmin == True and pvpmax == True and liqui == True):
            anp = ProcessReports(self.vacanciavalue.get(),self.pvpvaluemin.get(),self.pvpvaluemax.get(),self.liquidezvalue.get(),self.collectorstatus)
            anp.start()

    def cleanBaseData(self):
        WindowBase(Tk())

    def addFii(self):
        WindowAdd(Tk())

    def exitProgram(self):
        exit()

root = Tk()
Application(root)
root.title("Hunter Dog")
root.minsize(300,300)
#root.configure(background='gray')
root.mainloop()
