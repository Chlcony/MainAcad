import random
import string
# 1 task
from typing import List

lis = [z for z in range(10, 21)]
print(lis[::-1])
lis.insert(0, 21)
lis.append(9)
print(lis)
lis.pop()
del lis[2]
lis.sort()
print(lis)
united = sum(lis)
print(united)

# 2 task
lis = random.randint(10, 30)
# a = int(input('Insert integer in range from 10 to 30 - '))
print(lis)
list_1 = list(string.ascii_lowercase[:10])
list_2 = list(string.ascii_lowercase[10:])
list_3 = list(string.digits)

list_1.extend(list_2); list_1.extend(list_3)

print(list_1)
key = random.sample(list_1, lis)

print(''.join(key))

# 3 task
inp_1 = '07.06.98, 175, 65'
inp_2 = '20-09-61'
inp_1 = inp_1.split(',')
print(inp_1)
inp_2: List[str] = inp_2.split('-')
lis = (inp_1[0].split('.'))
print(lis)
inp_1 = (inp_1[1:])
print(inp_1)
inp_1.append(lis)
print(inp_1)
inp_1[2].insert(0, inp_2)
united = inp_1[2]

del inp_1[2]
lis = inp_1
print(lis, '|', united)
lis, united = united, lis
print(lis, '|', united)

# task 4
lis = random.randint(10, 99)
united = random.randint(1000, 9999)
c = random.sample(range(lis, united), 10)
print(c)

lis = c
c = lis.copy()
x = min(c)
x1 = c.index(x)
y = max(c)
y1 = c.index(y)
print(lis)
del (lis[x1]); lis.insert(x1, y)
del (lis[y1]); lis.insert(y1, x)

print(lis)

# task 5
lis = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]]
print(lis)
lis[0][0:3], lis[2][-3::] = lis[2][-3::], lis[0][0:3:]
print(lis)
lis[1].clear()
lis[1].extend(random.sample(lis[0], 5))
lis[1].extend(random.sample(lis[2], 5))

print(lis[1])
print(lis)

united = []
united.extend(lis[0])
united.extend(lis[1])
united.extend(lis[2])
print(united)
