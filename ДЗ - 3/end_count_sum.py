n_list=[]
while True:
    ins = input('number/stop')
    if ins.isdigit():
        n_list.append(int(ins))
    elif ins.lower() == 'stop':
        print(sum(n_list))
        break
    else:
        print('error')
