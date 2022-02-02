from tkinter import *
from os import system
from tkinter import font
from PIL import Image, ImageTk
import time

root = Tk()

class Aplication():

    def __init__(self):
        self.RolesAvailable = ["Qualquer role", "Top Laner", "Jungler", "Mid Laner", "Ad Carry", "Suporte"]
        self.ClassAvailable = ["Qualquer classe", "Assassino", "Mago", "Lutador", "Atirador", "Suporte", "Tanque"]
        self.img1 = ImageTk.PhotoImage(file="SummonersRift.png")
        self.root = root
        
        self.display()
        self.displayFrames()
        self.displaybuttons()
        self.showMap()
        root.mainloop()
    
    def display(self):
        self.root.title("Gerador de Composições aleatórias")
        self.root.configure(background="#2c2d31")
        self.root.geometry("1024x576")
        self.root.resizable(False, False)
        
    def displayFrames(self):
        self.frame1 = Frame(self.root)
        self.frame1.configure(background="#393842", bd=4, relief="groove")
        self.frame1.place(relx=0.005, rely=0.1, relheight=0.98, relwidth=0.395)

        self.frame2 = Frame(self.root)
        self.frame2.configure(background="#393842", bd=4, relief="groove")
        self.frame2.place(relx=0.405, rely=0.1, relheight=0.98, relwidth=0.595  )

    def displaybuttons(self):

        self.TopButtons()

        self.JgButtons()

        self.MidButtons()

        self.AdcButtons()

        self.SupButtons()

        self.buttonGenerate()

    def TopButtons(self):

        self.lb_topChampions = Label(self.frame1, text="Top Laner:", font="arial 11")
        self.lb_topChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_topChampions.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.04)

        self.vRolesTop = StringVar(root)
        self.vRolesTop.set("Roles Disponíveis Top")
        self.cb_rolesTop = OptionMenu(self.frame1, self.vRolesTop, *self.RolesAvailable)
        self.cb_rolesTop.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesTop.place(relx=0.025, rely=0.05, relwidth=0.95, relheight=0.04)

        self.vClassesTop = StringVar(root)
        self.vClassesTop.set("Classes Disponíveis Top")
        self.cb_classTop = OptionMenu(self.frame1, self.vClassesTop, *self.ClassAvailable)
        self.cb_classTop.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classTop.place(relx=0.025, rely=0.1, relwidth=0.95, relheight=0.04)

    def JgButtons(self):
        self.lb_jgChampions = Label(self.frame1, text="Jungler:", font="arial 11")
        self.lb_jgChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_jgChampions.place(relx=0.025, rely=0.15, relwidth=0.95, relheight=0.04)

        self.vRolesJg = StringVar()
        self.vRolesJg.set("Roles Disponíveis Jg")
        self.cb_rolesJg = OptionMenu(self.frame1, self.vRolesJg, *self.RolesAvailable)
        self.cb_rolesJg.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesJg.place(relx=0.025, rely=0.2, relwidth=0.95, relheight=0.04)

        self.vClassesJg = StringVar()
        self.vClassesJg.set("Classes Disponíveis Jg")
        self.cb_classJg = OptionMenu(self.frame1, self.vClassesJg, *self.ClassAvailable)
        self.cb_classJg.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classJg.place(relx=0.025, rely=0.25, relwidth=0.95, relheight=0.04)

    def MidButtons(self):
        self.lb_midChampions = Label(self.frame1, text="Mid Laners:", font="arial 11")
        self.lb_midChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_midChampions.place(relx=0.025, rely=0.3, relwidth=0.95, relheight=0.04)

        self.vRolesMid = StringVar()
        self.vRolesMid.set("Roles Disponíveis Mid")
        self.cb_rolesMid = OptionMenu(self.frame1, self.vRolesMid, *self.RolesAvailable)
        self.cb_rolesMid.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesMid.place(relx=0.025, rely=0.35, relwidth=0.95, relheight=0.04)

        self.vClassesMid = StringVar()
        self.vClassesMid.set("Classes Disponíveis Mid")
        self.cb_classMid = OptionMenu(self.frame1, self.vClassesMid, *self.ClassAvailable)
        self.cb_classMid.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classMid.place(relx=0.025, rely=0.40, relwidth=0.95, relheight=0.04)

    def AdcButtons(self):
        self.lb_adcChampions = Label(self.frame1, text="Ad Carry:", font="arial 11")
        self.lb_adcChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_adcChampions.place(relx=0.025, rely=0.45, relwidth=0.95, relheight=0.04)

        self.vRolesAdc = StringVar()
        self.vRolesAdc.set("Roles Disponíveis Adc")
        self.cb_rolesAdc = OptionMenu(self.frame1, self.vRolesAdc, *self.RolesAvailable)
        self.cb_rolesAdc.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesAdc.place(relx=0.025, rely=0.5, relwidth=0.95, relheight=0.04)

        self.vClassesAdc = StringVar()
        self.vClassesAdc.set("Classes Disponíveis Adc")
        self.cb_classAdc = OptionMenu(self.frame1, self.vClassesAdc, *self.ClassAvailable)
        self.cb_classAdc.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classAdc.place(relx=0.025, rely=0.55, relwidth=0.95, relheight=0.04)

    def SupButtons(self):
        self.lb_supChampions = Label(self.frame1, text="Suporte:", font="arial 11")
        self.lb_supChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_supChampions.place(relx=0.025, rely=0.6, relwidth=0.95, relheight=0.04)

        self.vRolesSup = StringVar()
        self.vRolesSup.set("Roles Disponíveis Sup")
        self.cb_rolesSup = OptionMenu(self.frame1, self.vRolesSup, *self.RolesAvailable)
        self.cb_rolesSup.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesSup.place(relx=0.025, rely=0.65, relwidth=0.95, relheight=0.04)

        self.vClassesSup = StringVar()
        self.vClassesSup.set("Classes Disponíveis Sup")
        self.cb_classSup = OptionMenu(self.frame1, self.vClassesSup, *self.ClassAvailable)
        self.cb_classSup.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classSup.place(relx=0.025, rely=0.70, relwidth=0.95, relheight=0.04)

    def buttonGenerate(self):
        self.btnGenerate = Button(self.frame1, text="Gerar Campeões\naleatórios", command=lambda:self.generateRandomChampions())
        self.btnGenerate.configure(font="arial 15", bg="#393842", fg="#a9a8a2", bd=5, relief="groove")
        self.btnGenerate.place(relx=0.025, rely=0.80, relwidth=0.95, relheight=0.1)

    def generateRandomChampions(self):
        self.showMap()
        for j in range (0, 5):
            if j == 0:
                for i in range (0, 5):
                    
                    if self.vRolesTop.get() == self.RolesAvailable[i]:
                        roleSelected = i - 1
                for i in range (0, 6):
                    if self.vClassesTop.get() == self.ClassAvailable[i]:
                        classSelected = i - 1
            elif j == 1:
                for i in range (0, 5):
                    if self.vRolesJg.get() == self.RolesAvailable[i]:
                        roleSelected = i - 1
                for i in range (0, 6):
                    if self.vClassesJg.get() == self.ClassAvailable[i]:
                        classSelected = i - 1

            elif j == 2:
                for i in range (0, 5):
                    if self.vRolesMid.get() == self.RolesAvailable[i]:
                        roleSelected = i - 1
                for i in range (0, 6):
                    if self.vClassesMid.get() == self.ClassAvailable[i]:
                        classSelected = i - 1

            elif j == 3:
                for i in range (0, 5):
                    if self.vRolesAdc.get() == self.RolesAvailable[i]:
                        roleSelected = i - 1
                for i in range (0, 6):
                    if self.vClassesAdc.get() == self.ClassAvailable[i]:
                        classSelected = i - 1

            elif j == 4:
                for i in range (0, 5):
                    if self.vRolesSup.get() == self.RolesAvailable[i]:
                        roleSelected = i - 1
                for i in range (0, 6):
                    if self.vClassesSup.get() == self.ClassAvailable[i]:
                        classSelected = i - 1
            system(f".\\RNG2.exe {roleSelected} {classSelected}")
            self.getChampionGenerated()
            self.showChampSelected(j)
            time.sleep(1)

        
    def getChampionGenerated(self):
        dataFile = open("output.txt")
        self.champSelected = dataFile.readline()
        dataFile.close()

    def showChampSelected(self, j):
        if j == 0:
            self.lb_championTopLane = Label(self.frame2, text=f"{self.champSelected}")
            self.lb_championTopLane.configure(font="arial 15", bg='#393842', fg="#a9a8a2")
            self.lb_championTopLane.place(relx=0.025, rely=0.01, relwidth=0.2, relheight=0.1)
        elif j == 1:
            self.lb_championTopLane = Label(self.frame2, text=f"{self.champSelected}")
            self.lb_championTopLane.configure(font="arial 15", bg='#393842', fg="#a9a8a2")
            self.lb_championTopLane.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.1)
        elif j == 2:
            self.lb_championTopLane = Label(self.frame2, text=f"{self.champSelected}")
            self.lb_championTopLane.configure(font="arial 15", bg='#393842', fg="#a9a8a2")
            self.lb_championTopLane.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
        elif j == 3:
            self.lb_championTopLane = Label(self.frame2, text=f"{self.champSelected}")
            self.lb_championTopLane.configure(font="arial 15", bg='#393842', fg="#a9a8a2")
            self.lb_championTopLane.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.1)
        elif j == 4:
            self.lb_championTopLane = Label(self.frame2, text=f"{self.champSelected}")
            self.lb_championTopLane.configure(font="arial 15", bg='#393842', fg="#a9a8a2")
            self.lb_championTopLane.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.1)
    def showMap(self):
        labelImage1 = Label(self.frame2, image=self.img1)
        labelImage1.pack()
Aplication()
