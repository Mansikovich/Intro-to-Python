def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)


a = int(input("Введите первое неотрицительное число: "))
b = int(input("Введите второе неотрицательно число: "))
print(summa(a, b))