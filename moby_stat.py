import collections
with open('moby_claen.txt','r') as file:
    reader = file.read()

listt = reader.split()
dic = collections.Counter(listt)

print(dic.most_common(5))
print(dic.most_common()[:-6:-1])
