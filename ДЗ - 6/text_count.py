with open('text.txt','r',encoding = "utf8") as file:
    reader = file.read()
    reader1 =reader.split('.')[0:-1]


mean_value = sum(map(len,reader1))/len(reader1)
print('среднее количество слов в расчете на пред­ложение:', mean_value)
count_u = 0
count_l = 0
count_n = 0
count_s = 0
for i in reader:
    if i.isupper():
        count_u += 1
    if i.islower():
        count_l += 1
    if i.isdigit():
        count_n += 1
    if i == ' ':
        count_s += 1
print('количество букв в файле в верхнем регистре', count_u)
print('количество букв в файле в нижнем регистре', count_l)
print('количество цифр в файле', count_n)
print('количество пробельных символов в файле', count_s)
