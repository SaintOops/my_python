with open('moby.txt','r') as file:
    reader = file.read()
trantab = str.maketrans(';:.,-','     ')
print(reader.translate(trantab).lower())

with open('moby_claen.txt','w') as output_file:
    output_file.write(reader.translate(trantab).lower().replace(' ','\n'))
