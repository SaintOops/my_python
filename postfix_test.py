def calc(expr):

    ans = []
    for i in expr.split():
        if i.isdigit():
            ans.append(i)
        else:
            ans.append(str(eval(ans.pop() + i + ans.pop())))
    
    return ans
