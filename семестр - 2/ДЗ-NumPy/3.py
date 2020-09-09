import pandas as pd

url = 'https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv'

football = pd.read_csv(url)
football.head()

# задание 1
# Посчитайте среднюю зарплату (Wage) и цену (Value) игроков разных позиций (Position). Представители какой позиции имеют самую высокую среднюю цену?

print(football.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Value'], ascending=False))
print(football.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Value'], ascending=False).head(1))

# задание 2
# Посчитайте среднюю (mean) и медианную (median) зарплату (Wage) футболистов из разных клубов (Club). В скольких клубах средняя и медианная зарплаты совпадают?

t = football.groupby(['Club'])['Wage'].agg(['mean', 'median'])
print(t, t[t['median'] == t['mean']].index)

# задание 1
# С помощью функции groupby посчитайте сумму зарплат (Wage) футболистов клуба (Club) "Chelsea".

print(football.groupby(['Club'])['Wage'].sum()['Chelsea'])

# задание 2
# Определите максимальную зарплату футболиста национальности (Nationality) Аргентина ("Argentina") в возрасте 20 лет.

print(football[(football.Nationality == "Argentina") & (football.Age == 20)].Wage.max())

# задание 3
# Определите максимальную зарплату футболиста национальности (Nationality) Аргентина ("Argentina") в возрасте 30 лет.

print(football[(football.Nationality == "Argentina") & (football.Age == 30)].Wage.max())

# задание 4
# Определите минимальную зарплату футболиста национальности (Nationality) Аргентина ("Argentina") в возрасте 30 лет.

print(football[(football.Nationality == "Argentina") & (football.Age == 30)].Wage.min())

# задание 5
# Определите максимальную силу (Strength) и баланс (Balance) среди игроков клуба (Club) "FC Barcelona" из Аргентины ("Argentina"). Ответ через точку с запятой без пробела.

football[(football.Nationality == "Argentina") & (football.Club == "FC Barcelona")][['Strength','Balance']].max()
