n = int(input())
a = [int(i) for i in input(' Введите числа списка через пробел ').split()]
set_a = set(a)

m = int(input())
b = [int(i) for i in input(' Введите числа списка через пробел ').split()]
set_b = set(b)

common_number = sorted(set_a.inter11section(set_b))
print(common_number)

# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18