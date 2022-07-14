
import numpy as np


def sev_zap(a_, b_, c_):
    a = np.copy(a_)
    b = np.copy(b_)
    c = np.copy(c_)
    # Проверяем условие замкнутости:
    if a.sum() > b.sum():
        b = np.hstack((b, [a.sum() - b.sum()]))
        c = np.hstack((c, np.zeros(len(a)).reshape(-1, 1)))
    elif a.sum() < b.sum():
        a = np.hstack((a, [b.sum() - a.sum()]))
        c = np.vstack((c, np.zeros(len(b))))

    m = len(a)
    n = len(b)
    i = 0
    j = 0
    funk = 0
    x = np.zeros((m, n), dtype=int)
    while (i < m) and (j < n):  # повторяем цикл до сходимости метода
        x_ij = min(a[i], b[j])  # проверяем минимальность a_i и b_j
        funk += c[i, j] * min(a[i], b[j])  # записываем в итоговую функцию элемент трат
        a[i] -= x_ij  #
        b[j] -= x_ij  # обновляем векторы a и b
        x[i, j] = x_ij  # добавляем элемент x_ij в матрицу x

        if a[i] > b[j]:  # делаем сдвиги при выполнении условий
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            i += 1
            j += 1
    return x, funk  # возращаем матрицу x и целевую функцию
