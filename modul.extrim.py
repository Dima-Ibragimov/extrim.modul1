a='Антон'
b='Марина'
c='Кирилл'
d='Олег'
f='Ксения'
grades = [[5, 1, 3, 2, 4, 5], [1, 1, 1, 2, 5], [4, 5, 4, 3, 1], [5, 4, 1, 2, 3], [5, 3, 2, 4, 5]]
student = { a: grades[0], b : grades[1], c : grades[2], d : grades[3],  f : grades[4]}
print(student)
avarage1 = sum(grades[0]) / len(grades[0])
avarage2 = sum(grades[1]) / (len(grades[1]))
avarage3 = sum(grades[2]) / (len(grades[2]))
avarage4 = sum(grades[3]) / (len(grades[3]))
avarage5 = sum(grades[4]) / (len(grades[4]))
print('Среднная оценка ученика')
rating = {a: avarage1, b: avarage2, c: avarage3, f: avarage4}
print(rating)