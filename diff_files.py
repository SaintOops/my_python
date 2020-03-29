with open('text1.txt','r',encoding = "utf8") as file:
    reader1 = file.read()

with open('text2.txt','r',encoding = "utf8") as file:
    reader2 = file.read()

s1 = set(reader1.split())
s2 = set(reader2.split())

s3 = s1.intersection(s2)
s4 = s1 - s3
s5 = s2 - s3

print(s3)
print(s1.union(s2))
print(s4)
print(s5)
print(s3.union(s4))
