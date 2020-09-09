from math import sqrt
l1 = [sqrt(i) for i in [2,4,9,16,25]]

l2 = list(map(sqrt,[2,4,9,16,25]))

l3 = []
for i in [2,4,9,16,25]:
    l3.append(sqrt(i))

print(l1,l2,l3)
