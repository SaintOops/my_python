codes = {"А" : "%" , "а" : "9" , "Б" : "@", "б" : "*"}

with open('untitled.txt','r',encoding = "utf8") as file:
    reader = file.read()
    
    trantab = str.maketrans(codes)

with open('untitled_new.txt','w',encoding = "utf8") as file:
    file.write(reader.translate(trantab))

#сразу декодирование

decodes = dict(zip(codes.values(),codes.keys()))

with open('untitled_new.txt','r',encoding = "utf8") as file:
    reader = file.read()
    
    trantab = str.maketrans(decodes)

with open('untitled.txt','w',encoding = "utf8") as file:
    file.write(reader.translate(trantab))
