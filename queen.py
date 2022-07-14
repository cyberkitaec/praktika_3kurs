n = 8
x = [] #
y = [] # создаем два пустых списка
# заполнение списков с помощью цикла for
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
correct = True
# если при проверке условия, окажется, что ферзи бьют друг друга, то зна-чение флага correct будет изменено с true на false 
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
# вывод ответа
if correct:
    print('NO')
else:
    print('YES')
