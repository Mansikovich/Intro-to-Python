from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(1, 100))
    print(numbers)

min_number = int(input())
max_number = int(input())
for i in range(len(numbers)):
    if min_number <= numbers[i] <= max_number:
        print(i)