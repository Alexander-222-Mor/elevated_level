k = int(input('Введите число: '))
for i in range(1, k // 2 + 1):
    for j in range(i + 1, k):
        if k % (i + j) == 0:
            print(i,j)


