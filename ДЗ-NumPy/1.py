import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"
football = pd.read_csv(url)

# задание 1
# Чему равен средний возраст (Age), футболистов в наборе данных, округлённый до целого?

print(round(football.Age.mean()))

# задание 2
# Каково количество непустых строк в колонке Composure (Хладнокровие) набора данных о футболистах?

print(football.Composure.count())

# задание 3
# Каково в наборе данных о футболистах стандартное отклонение параметра коротких пасов (ShortPassing), округлённое до второго знака после запятой?

print(round(football.ShortPassing.std(),2))

# задание 4
# Какова сумма заработных плат за год (Wage) в наборе данных о футболистах?

print(football.Wage.sum())

# задание 5
# Какова минимальная стоимость футболиста (Value) в наборе данных о футболистах?

print(football.Value.min())

# задание 1
# Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых выше среднего? Ответ округлите до сотых.

print(round(football[football.Wage > football.Wage.mean()].SprintSpeed.mean(),2))

# задание 2
# Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых ниже среднего? Ответ округлите до сотых.

print(round(football[football.Wage < football.Wage.mean()].SprintSpeed.mean(),2))

# задание 3
# Какую позицию (Position) занимает футболист с самой высокой зарплатой (Wage)?

print(football[football.Wage == football.Wage.max()].Position.min())

# задание 4
# Сколько пенальти (Penalties) забили бразильские (Nationality, Brazil) футболисты за период, данные о котором представлены в датасете?

print(football[football.Nationality == "Brazil"].Penalties.sum())

# задание 5
# Укажите средний возраст (Age) игроков, у которых точность удара головой (HeadingAccuracy) > 50. Ответ округлите до сотых.

print(round(football[football.HeadingAccuracy > 50].Age.mean(),2))

# задание 6
# Укажите возраст (Age) самого молодого игрока, у которого хладнокровие (Composure) и реакция (Reactions) превышают 90% от максимального значения, представленного в датасете.

football[(football.Composure > football.Composure.max() * 0.9) &
(football.Reactions > football.Reactions.max() * 0.9)].Age.min()

# задание 7
# Определите, насколько средняя реакция (Reactions) самых взрослых игроков (т.е. игроков, чей возраст (Age) равен максимальному) больше средней реакции самых молодых игроков. Ответ округлите до сотых.

print(round(football[football.Age == football.Age.max()].Reactions.mean() / football[football.Age == football.Age.min()].Reactions.mean(),2))

# задание 8
# Из какой страны (Nationality) происходит больше всего игроков, чья стоимость (Value) превышает среднее значение?

print(football[football.Value > football.Value.mean()].Nationality.value_counts().index[0])

# задание 9
# Определите, во сколько раз средняя зарплата (Wage) голкипера (Position, GK) с максимальным значением показателя "Рефлексы" (GKReflexes) выше средней зарплаты голкипера с максимальным значением показателя "Владение мячом" (GKHandling). Ответ округлите до сотых.

print(round(football[(football.Position == "GK") & (football.GKReflexes == football.GKReflexes.max())].Wage.max() / football[(football.Position == "GK") & (football.GKHandling == football.GKHandling.max())].Wage.max(),2))

# задание 10
# Определите, во сколько раз средняя сила удара (ShotPower) самых агрессивных игроков (игроков с максимальным значением показателя "Агрессивность" (Aggression)) выше силы удара игроков с минимальной агрессией. Ответ округлите до сотых.

print(round(football[football.Aggression == football.Aggression.max()].ShotPower.mean() / football[football.Aggression == football.Aggression.min()].ShotPower.mean(),2))
