s = "У лукоморья 123 дуб зелёный 456"
if s.find('я') > 0:
    print(s.index('я'))
print(s.count('у'))
if not s.isalpha():
    print(s.upper())
if len(s) > 4:
    print(s.lower())
print(s.replace(s[0],'O'))
