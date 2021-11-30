from tkinter import *

root = Tk()

class Aplication():

    def __init__(self):
        self.root = root
        self.display()
        self.displayFrames()
        self.displaybuttons()
        root.mainloop()
    
    def display(self):
        self.root.title("Gerador de Composições aleatórias")
        self.root.configure(background="#2c2d31")
        self.root.geometry("1024x576")
        self.root.resizable(False, False)
        
    def displayFrames(self):
        self.frame1 = Frame(self.root)
        self.frame1.configure(background="#393842", bd=4, relief="groove")
        self.frame1.place(relx=0.005, rely=0.1, relheight=0.98, relwidth=0.245)

        self.frame2 = Frame(self.root)
        self.frame2.configure(background="#393842", bd=4, relief="groove")
        self.frame2.place(relx=0.255, rely=0.1, relheight=0.98, relwidth=0.74)

    def displaybuttons(self):

        self.TopButtons()

        self.JgButtons()

        self.MidButtons()

        self.AdcButtons()

        self.SupButtons()

    def TopButtons(self):

        self.lb_topChampions = Label(self.frame1, text="Top Laner:", font="arial 11")
        self.lb_topChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_topChampions.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.04)

        RolesAvailableTop = ["Qualquer role", "Top Laner", "Jungler", "Mid Laner", "Ad Carry", "Suporte"]
        vRolesTop = StringVar()
        vRolesTop.set("Roles Disponíveis Top")
        self.cb_rolesTop = OptionMenu(self.frame1, vRolesTop, *RolesAvailableTop)
        self.cb_rolesTop.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesTop.place(relx=0.025, rely=0.05, relwidth=0.95, relheight=0.04)

        ClassAvailableTop = ["Qualquer classe", "Assassino", "Mago", "Lutador", "Atirador", "Suporte", "Tanque"]
        vClassesTop = StringVar()
        vClassesTop.set("Classes Disponíveis Top")
        self.cb_classTop = OptionMenu(self.frame1, vClassesTop, *ClassAvailableTop)
        self.cb_classTop.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classTop.place(relx=0.025, rely=0.1, relwidth=0.95, relheight=0.04)

    def JgButtons(self):
        self.lb_jgChampions = Label(self.frame1, text="Jungler:", font="arial 11")
        self.lb_jgChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_jgChampions.place(relx=0.025, rely=0.2, relwidth=0.95, relheight=0.04)

        RolesAvailableJg = ["Qualquer role", "Top Laner", "Jungler", "Mid Laner", "Ad Carry", "Suporte"]
        vRolesJg = StringVar()
        vRolesJg.set("Roles Disponíveis Jg")
        self.cb_rolesJg = OptionMenu(self.frame1, vRolesJg, *RolesAvailableJg)
        self.cb_rolesJg.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesJg.place(relx=0.025, rely=0.24, relwidth=0.95, relheight=0.04)

        ClassAvailableJg = ["Qualquer classe", "Assassino", "Mago", "Lutador", "Atirador", "Suporte", "Tanque"]
        vClassesJg = StringVar()
        vClassesJg.set("Classes Disponíveis Jg")
        self.cb_classJg = OptionMenu(self.frame1, vClassesJg, *ClassAvailableJg)
        self.cb_classJg.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classJg.place(relx=0.025, rely=0.29, relwidth=0.95, relheight=0.04)

    def MidButtons(self):
        self.lb_midChampions = Label(self.frame1, text="Mid Laners:", font="arial 11")
        self.lb_midChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_midChampions.place(relx=0.025, rely=0.39, relwidth=0.95, relheight=0.04)

        RolesAvailableMid = ["Qualquer role", "Top Laner", "Jungler", "Mid Laner", "Ad Carry", "Suporte"]
        vRolesMid = StringVar()
        vRolesMid.set("Roles Disponíveis Mid")
        self.cb_rolesMid = OptionMenu(self.frame1, vRolesMid, *RolesAvailableMid)
        self.cb_rolesMid.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesMid.place(relx=0.025, rely=0.43, relwidth=0.95, relheight=0.04)

        ClassAvailableMid = ["Qualquer classe", "Assassino", "Mago", "Lutador", "Atirador", "Suporte", "Tanque"]
        vClassesMid = StringVar()
        vClassesMid.set("Classes Disponíveis Mid")
        self.cb_classMid = OptionMenu(self.frame1, vClassesMid, *ClassAvailableMid)
        self.cb_classMid.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classMid.place(relx=0.025, rely=0.48, relwidth=0.95, relheight=0.04)

    def AdcButtons(self):
        self.lb_adcChampions = Label(self.frame1, text="Ad Carry:", font="arial 11")
        self.lb_adcChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_adcChampions.place(relx=0.025, rely=0.56, relwidth=0.95, relheight=0.04)

        RolesAvailableAdc = ["Qualquer role", "Top Laner", "Jungler", "Mid Laner", "Ad Carry", "Suporte"]
        vRolesAdc = StringVar()
        vRolesAdc.set("Roles Disponíveis Adc")
        self.cb_rolesAdc = OptionMenu(self.frame1, vRolesAdc, *RolesAvailableAdc)
        self.cb_rolesAdc.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesAdc.place(relx=0.025, rely=0.6, relwidth=0.95, relheight=0.04)

        ClassAvailableAdc = ["Qualquer classe", "Assassino", "Mago", "Lutador", "Atirador", "Suporte", "Tanque"]
        vClassesAdc = StringVar()
        vClassesAdc.set("Classes Disponíveis Adc")
        self.cb_classAdc = OptionMenu(self.frame1, vClassesAdc, *ClassAvailableAdc)
        self.cb_classAdc.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classAdc.place(relx=0.025, rely=0.65, relwidth=0.95, relheight=0.04)

    def SupButtons(self):
        self.lb_supChampions = Label(self.frame1, text="Suporte:", font="arial 11")
        self.lb_supChampions.configure(bg="#393842", fg="#a9a8a2")
        self.lb_supChampions.place(relx=0.025, rely=0.75, relwidth=0.95, relheight=0.04)

        RolesAvailableSup = ["Qualquer role", "Top Laner", "Jungler", "Mid Laner", "Ad Carry", "Suporte"]
        vRolesSup = StringVar()
        vRolesSup.set("Roles Disponíveis Sup")
        self.cb_rolesSup = OptionMenu(self.frame1, vRolesSup, *RolesAvailableSup)
        self.cb_rolesSup.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_rolesSup.place(relx=0.025, rely=0.79, relwidth=0.95, relheight=0.04)

        ClassAvailableSup = ["Qualquer classe", "Assassino", "Mago", "Lutador", "Atirador", "Suporte", "Tanque"]
        vClassesSup = StringVar()
        vClassesSup.set("Classes Disponíveis Sup")
        self.cb_classSup = OptionMenu(self.frame1, vClassesSup, *ClassAvailableSup)
        self.cb_classSup.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_classSup.place(relx=0.025, rely=0.84, relwidth=0.95, relheight=0.04)

Aplication()
