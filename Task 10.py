import random
from random import randint
amount_coin = int(input('введите N: '))
m = 0
k = 0
coins = [0, 1]
for i in range(amount_coin):
     random.shuffle(coins)
     if int(coins[0]) == 0:
         k += 1
     if int(coins[0]) == 1:
         m += 1
if m > k:
     ans = k
else:
     ans = m
print(f"Минимум перевернуть {ans}")