line = "пара-ра-рам рам-пам-папам па-ра-па-да"
lines = line.split()
 
lst = [sum(x in 'а' for x in line) for line in lines]
 
if len(set(lst)) == 1 :
    res = "Парам пам-пам"  
else: res = "Пам парам"
 
print(res)