import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"
football = pd.read_csv(url)

# вопрос 1
# Сколько футбольных клубов представлено в датасете?
print(len(football.Club.unique()))

# вопрос 2
# Как называется футбольный клуб, представленный наименьшим количеством игроков в датасете?
print(football.Club.value_counts().index[-1])

# вопрос 3
# Данные об игроках каких позиций (Position) занимают более 10% датасета?
s = football.Position.value_counts(normalize=True)
print(s.loc[s > 0.1].reset_index())

# вопрос 4
# Данные об игроках каких позиций (Position) занимают менее 1% датасета?

print(s.loc[s < 0.01].reset_index())

# вопрос 5
# В каких пределах находятся худшие 20% показателей точности ударов ногой (FKAccuracy)?

print(football.FKAccuracy.value_counts(bins = 5).index[0].left,"~~", football.FKAccuracy.value_counts(bins = 5).index[0].right)

# вопрос 6
# Какие показатели точности ударов ногой демонстрирует большинство футболистов?

print(football.FKAccuracy.value_counts().index[0])

# задание 1
# У какого процента испанских специалистов (Nationality = 'Spain') зарплата (Wage) находится в пределах 25% минимума от наблюдаемого уровня зарплат? Ответ в виде целого числа (округлите полученный результат) без знака %.

x = football[football.Nationality == 'Spain'].Wage.value_counts(bins = 4).unique()
print(round(x[0] / sum(x),2)*100)

# задание 2
# Укажите количество уникальных сборных (Nationality), к которым относятся футболисты, выступающие за клуб (Club) "Manchester United".

print(len(football[football.Club == "Manchester United"].Nationality.unique()))

# задание 3
# С помощью функции unique определите двух футболистов из Бразилии (Nationality = 'Brazil'), выступающих за клуб (Club) 'Juventus'. Перечислите их имена (Name, как в датафрейме) через запятую в алфавитном порядке.

football[(football.Nationality == 'Brazil') & (football.Club == 'Juventus')].Name.reset_index()

# задание 4
# Укажите, какой из клубов (Club) насчитывает большее количество футболистов возрастом (Age) старше 35 лет

print(football[football.Age > 35].Club.value_counts().index[0])

# задание 5
# С помощью функции value_counts с параметром bins разбейте всех футболистов сборной (Nationality) Аргентины ('Argentina') на 4 равные группы. Укажите, сколько футболистов в возрасте от 34.75 до 41 года в сборной Аргентины.

print(football[football.Nationality == 'Argentina'].reset_index().index.value_counts(bins = 4).reset_index())
print(len(football[(football.Age < 41) & (football.Age > 34.75)].index))

# задание 6
# Сколько процентов футболистов из Испании (Nationality = 'Spain') имеют возраст (Age) 21 год? Введите с точностью до 2 знаков после запятой без указания знака % (например, 12.35).

print(round(len(football[(football.Nationality == 'Spain') & (football.Age == 21)].index) * 100 / len(football[football.Nationality == 'Spain'].index),2))
