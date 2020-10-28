import random
import string
# 1 task
a = [z for z in range(10, 21)]
print(a[::-1])
a.insert(0, 21)
a.append(9)
print(a)
a.pop()
del a[2]
a.sort()
print(a)
b = sum(a)
print(b)

# 2 task
a = random.randint(10, 30)
# a = int(input('Insert integer in range from 10 to 30 - '))
print(a)
list_1 = list(string.ascii_lowercase[:10])
list_2 = list(string.ascii_lowercase[10:])
list_3 = list(string.digits)

list_1.extend(list_2); list_1.extend(list_3)

print(list_1)
key = random.sample(list_1, a)

print(''.join(key))

# 3 task
inp_1 = '07.06.98, 175, 65'
inp_2 = '20-09-61'
inp_1 = inp_1.split(',')
print(inp_1)
inp_2 = inp_2.split('-')
a = (inp_1[0].split('.'))
print(a)
inp_1 = (inp_1[1:])
print(inp_1)
inp_1.append(a)
print(inp_1)
inp_1[2].insert(0, inp_2)
b = inp_1[2]

del inp_1[2]
a = inp_1
print(a, '|', b)
a, b = b, a
print(a, '|', b)

# task 4
a = random.randint(10, 99)
b = random.randint(1000, 9999)
c = list( in range(10))
print(c)
