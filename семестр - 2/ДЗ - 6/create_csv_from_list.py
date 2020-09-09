def create_csv_from_list(data):
    try:
        ans = 'name,address,age\n'
        for i in data:
            ans += ','.join(i) + '\n'
        with open('data.txt','w') as file:
            file.write(ans)
    
    except TypeError:
        print('Неправильный ввод типа')
    except NameError:
        print('Неправильный ввод имени')
