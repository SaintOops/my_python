def check_delimiter(s):
    k = 0
    temp = s
    while k <= len(s)//2:
        a = temp.pop()
        b = temp.pop()
        if a+b in ["[]","{}","()"]:
            temp.prepend(a,b)
        k+=1
    if len(temp) > 0:
        k = "true"
    else:
        k = "false"
    return k
