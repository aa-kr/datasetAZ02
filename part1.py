import pandas as pd

data = {
    'Имя': ['Алена', 'Сергей', 'Андрей', 'Егор', 'Ирина', 'Петр', 'Татьяна', 'Федор', 'Алексей', 'Михаил'],
    'Оценка по математике': [4, 3, 5, 5, 4, 3, 2, 4, 4, 5],
    'Оценка по физике': [3, 4, 4, 4, 3, 5, 5, 5, 3, 4],
    'Оценка по биологии':[4, 3, 3, 5, 5, 4, 3, 5, 5, 4],
    'Оценка по географии':[4, 4, 3, 5, 5, 5, 3, 3, 4, 5],
    'Оценка по химии':[3, 3, 3, 4, 5, 5, 4, 4, 5, 3, ],
}
df = pd.DataFrame(data)

print(df.head())

#Вычисляем среднюю оценку по каждому предмету
print(f"Средняя оценка по математике - {df['Оценка по математике'].mean()}")
print(f"Средняя оценка по физике - {df['Оценка по физике'].mean()}")
print(f"Средняя оценка по биологии - {df['Оценка по биологии'].mean()}")
print(f"Средняя оценка по географии - {df['Оценка по географии'].mean()}")
print(f"Средняя оценка по химии - {df['Оценка по химии'].mean()}")

#Вычисляем медианную оценку по каждому предмету
print(f"Медианная оценка по математике - {df['Оценка по математике'].median()}")
print(f"Медианная оценка по физике - {df['Оценка по физике'].median()}")
print(f"Медианная оценка по биологии - {df['Оценка по биологии'].median()}")
print(f"Медианная оценка по географии - {df['Оценка по географии'].median()}")
print(f"Медианная оценка по химии- {df['Оценка по химии'].median()}")

#Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Оценка по математике'].quantile(0.25)
Q3_math = df['Оценка по математике'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"Q1_math = {Q1_math}")
print(f"Q3_math = {Q3_math}")
print(f"IQR_math = {IQR_math}")

#Вычисляем стандартное отклонение
stdA = df['Оценка по математике'].std()
stdB = df['Оценка по физике'].std()
stdC = df['Оценка по биологии'].std()
stdD = df['Оценка по географии'].std()
stdE = df['Оценка по химии'].std()

print(f"Стандартное отклонение Оценка по математике - {stdA}")
print(f"Стандартное отклонение Оценка по физике - {stdB}")
print(f"Стандартное отклонение Оценка по биологии - {stdC}")
print(f"Стандартное отклонение Оценка по географии - {stdD}")
print(f"Стандартное отклонение Оценка по химии - {stdE}")