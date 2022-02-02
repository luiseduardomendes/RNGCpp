import csv
import re

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
    championList.append(champions)