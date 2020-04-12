import csv
import collections
with open('opendata.stat.txt','r',encoding = "utf8") as file:
    stat_regions = csv.reader(file)
    region = 'Россия'
    count = 696232
    srting = 'Количество заявок на потребительские кредиты'
    d = {}
    for row in stat_regions:
        if row[0] == srting and row[2][:4] == '2017' and row[1] == region:
            count += int(row[3])
        elif row[2][:4] == '2017' and row[0] == srting:
            d[region] = count
            region = row[1]
            count = int(row[3])
        elif row[0] == 'Средняя сумма заявки на потребительский кредит':
            d[region] = count
    d['Россия'] = 0 
    d = collections.Counter(d)
    print(d.most_common(1))
