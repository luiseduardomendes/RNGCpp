import csv
import re
class ChampionsLol:
    champions = dict()
    championList = list()

    roles = ('top laner', 'jungler', 'mid laner', 'ad carry', 'support')
    classes = ('tank', 'support', 'marksman', 'mage', 'rogue', 'enchanter', 'fighter')

    championsByRole = dict()
    for role in roles:
        championsByRole[role] = list()
    

    championsByClass = dict()
    for c in classes:
        championsByClass[c] = list()
    

    def __init__(self):
        data = open('champions.csv')

        pattern = re.compile(r'(.+),(role),(.+),(class),(.+)')

        for line in data:
            buffer = data.readline()
            check = pattern.findall(buffer)
            for i in check:
                self.champions['name'] = str(i[0])
                self.champions['role'] = str(i[2]).split(sep=',')
                
                self.champions['class'] = str(i[4]).split(sep=',')

            self.championList.append(self.champions.copy())

    def splitChampionByRole(self):
        for champion in self.championList:
            for i in champion['role']:
                if self.championsByRole[i].count(champion['name']) == 0:
                    self.championsByRole[i].append(champion['name'][:])
    
    def showChampionsByRole(self):
        for r in self.roles:
            print(self.championsByRole[r])
        

    def splitChampionByClass(self):
        for champion in self.championList:
            for i in champion['class']:
                if self.championsByClass[i].count(champion['name']) == 0:
                    self.championsByClass[i].append(champion['name'][:])

    def showChampionsByClass(self):
        for c in self.classes:
            print(self.championsByClass[c])
        

        

ch = ChampionsLol()
ch.splitChampionByRole()
ch.splitChampionByClass()