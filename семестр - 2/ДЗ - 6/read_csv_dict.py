def read_csv_dict(file_name):
    try:      
        with open(file_name,'r',encoding = "utf8") as file:
            reader = file.read().split('\n')[1:-1]
        ans = []    
        for i in reader:
            temp = i.split(',')
            ans.append({'name':temp[0],'age':temp[1],'address':temp[2]})
        return ans
    except FileNotFoundError:
        print('Файла не существует')
