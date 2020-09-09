def text_numbers(file_name):
    try:
        with open(file_name,'r',encoding = "utf8") as file:
            reader = file.read().split('\n')

        seq1 = list(range(1,len(reader)))
        seq2 = reader[0:-1]
        zipped = list(zip(seq1, seq2))
        ans = ''
        for i in zipped:
            ans += str(i[0]) + ' ' + i[1] + '\n'
            
        with open('update_text.txt','w',encoding = "utf8") as output_file:
            output_file.write(ans)
    except FileNotFoundError:
        print('Файла не существует')


text_numbers('text.txt')
