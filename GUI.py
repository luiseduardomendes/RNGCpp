import string
from tkinter import *
from os import system
from tkinter import font
from PIL import Image, ImageTk
import time

from createChamp import ChampionsLol

root = Tk()

class Aplication():

    roles = {   "Qualquer role" : 'any', 
                "Top Laner" : 'top laner', 
                "Jungler" : 'jungler', 
                "Mid Laner" : 'mid laner', 
                "Ad Carry" : 'ad carry', 
                "Suporte" : 'support'}
    classes = { "Qualquer role" : 'any', 
                "Tanque" : 'tank',
                "Suporte" : 'support',
                "Atirador" : 'marksman', 
                "Mago" : 'mage', 
                "Assassino" : 'rogue', 
                "Encantador" : 'enchanter', 
                "Lutador" : 'fighter'}

    def __init__(self):
        self.RolesAvailable = ["Qualquer role", "Top Laner", "Jungler", "Mid Laner", "Ad Carry", "Suporte"]
         

        self.ClassAvailable = ["Qualquer classe", "Assassino", "Mago", "Lutador", "Atirador", "Suporte", "Tanque", "Encantador"]
        self.img1 = ImageTk.PhotoImage(file="SummonersRift.png")
        self.root = root
        
        self.display()
        self.displayFrames()
        self.buttons()
        self.labels()
        self.showMap()
        self.buttonGenerateChamps()
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

    def showMap(self):
        labelImage1 = Label(self.frame2, image=self.img1)
        labelImage1.pack()


    def buttons(self):
        self.optMenu1 = dict()
        self.vRoles = dict()
        self.notSelectedRole = dict()

        for i, laneBtn in enumerate(self.RolesAvailable[1:]):
            self.notSelectedRole[laneBtn] = f"Roles Disponíveis {laneBtn}"
            
            self.vRoles[laneBtn] = StringVar(root)
            self.vRoles[laneBtn].set(f"Roles Disponíveis {laneBtn}")
            self.optMenu1[laneBtn] = OptionMenu(self.frame1, self.vRoles[laneBtn], *self.RolesAvailable)
            self.optMenu1[laneBtn].configure(font="arial 10", bg="#393842", fg="#a9a8a2")
            self.optMenu1[laneBtn].place(relx=0.025, rely=0.05+0.15*i, relwidth=0.95, relheight=0.04)
    
        self.optMenu2 = dict()
        self.vClasses = dict()
        self.notSelectedClass = dict()
        
        for i, laneBtn in enumerate(self.RolesAvailable[1:]):
            self.notSelectedClass[laneBtn] = f"Classes Disponíveis {laneBtn}"
            
            self.vClasses[laneBtn] = StringVar(root)
            self.vClasses[laneBtn].set(f"Classes Disponíveis {laneBtn}")
            self.optMenu2[laneBtn] = OptionMenu(self.frame1, self.vClasses[laneBtn], *self.ClassAvailable)
            self.optMenu2[laneBtn].configure(font="arial 10", bg="#393842", fg="#a9a8a2")
            self.optMenu2[laneBtn].place(relx=0.025, rely=0.1+0.15*i, relwidth=0.95, relheight=0.04)
            

    def labels(self):
        self.lbls = dict()
        
        for i, laneLbl in enumerate(self.RolesAvailable[1:]):

            self.lbls[laneLbl] = Label(self.frame1, text=f"{laneLbl}:", font="arial 11")
            self.lbls[laneLbl].configure(bg="#393842", fg="#a9a8a2")
            self.lbls[laneLbl].place(relx=0.025, rely=0.01+0.15*i, relwidth=0.95, relheight=0.04)

    def showChamps(self):
        self.championsSelected = list()
        for i in self.RolesAvailable[1:]:
            
            if self.vRoles[i].get() != self.notSelectedRole[i] and self.vClasses[i].get() != self.notSelectedClass[i]:
                self.championsSelected.append(ChampionsLol.showRandomChampion(ChampionsLol, self.roles[self.vRoles[i].get()], self.classes[self.vClasses[i].get()]))
            else:  
                self.championsSelected.append(ChampionsLol.showRandomChampion(ChampionsLol, 'any', 'any'))

        self.showChampions()
    
    def buttonGenerateChamps(self):
        self.btnGenerate = Button(self.frame1, text="Gerar Campeões\naleatórios", 
        command=lambda:self.showChamps())
        self.btnGenerate.configure(font="arial 15", bg="#393842", fg="#a9a8a2", bd=5, relief="groove")
        self.btnGenerate.place(relx=0.025, rely=0.80, relwidth=0.95, relheight=0.1)
    
    def showChampions(self):
        self.lb_champion = dict()
        cont = 0

        for i in self.RolesAvailable[1:]:
            self.lb_champion[i] = Label(self.frame2, text=f"{self.championsSelected[cont]}")
            self.lb_champion[i].configure(font="arial 15", bg='#393842', fg="#a9a8a2")
            self.lb_champion[i].place(relx=0.1+0.15*cont, rely=0.1+0.15*cont, relwidth=0.2, relheight=0.1)
            cont = cont + 1

Aplication()