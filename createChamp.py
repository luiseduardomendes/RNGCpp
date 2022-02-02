import csv
import re
class ChampionsLol:
    champions = dict()
    championList = list()

    data = open('champions.csv')

    pattern = re.compile(r'(.+),(role),(.+),(class),(.+)')

    for line in data:
        buffer = data.readline()
        check = pattern.findall(buffer)
        for i in check:
            champions['name'] = str(i[0])
            champions['role'] = str(i[2]).split(sep=',')
            
            champions['class'] = str(i[4]).split(sep=',')
            
        print(champions)
        championList.append(champions.copy())

    championsByRole = dict()
    championsByRole['top laner'] = list()
    championsByRole['jungler'] = list()
    championsByRole['mid laner'] = list()
    championsByRole['ad carry'] = list()
    championsByRole['support'] = list()

    championsByClass = dict()
    championsByClass['tank'] = list()
    championsByClass['support'] = list()
    championsByClass['marksman'] = list()
    championsByClass['mage'] = list()
    championsByClass['rogue'] = list()
    championsByClass['enchanter'] = list()
    championsByClass['fighter'] = list()

    def splitChampionByRole(self):
        for champion in self.championList:
            for i in champion['role']:
                if self.championsByRole[i].count(champion['name']) == 0:
                    self.championsByRole[i].append(champion['name'][:])

        print(self.championsByRole['top laner'])
        print(self.championsByRole['jungler'])
        print(self.championsByRole['mid laner'])
        print(self.championsByRole['ad carry'])
        print(self.championsByRole['support'])

    def splitChampionByClass(self):
        for champion in self.championList:
            for i in champion['class']:
                if self.championsByClass[i].count(champion['name']) == 0:
                    self.championsByClass[i].append(champion['name'][:])

        print(self.championsByClass['tank'])
        print(self.championsByClass['support'])
        print(self.championsByClass['marksman'])
        print(self.championsByClass['mage'])
        print(self.championsByClass['rogue'])
        print(self.championsByClass['enchanter'])
        print(self.championsByClass['fighter'])

        

ch = ChampionsLol()
ch.splitChampionByRole()
ch.splitChampionByClass()