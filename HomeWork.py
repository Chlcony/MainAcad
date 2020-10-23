print('Hello, my name is')
name = 'Anton'
return_1 ='Hello, my name is ' + name
age = '22'
return_1 += '. I\'m ' + age
gender = 'male'
return_1 += ' and I\'m a ' + gender + '.'
# print(return_1)

return_2 = 'Hello, my name is {}. I\'m {} and I\'m a {}.'.format(name, age, gender)
# print(return_2)

return_3 = (f'Hello, my name is {name}. I\'m {age} and I\'m a {gender}.')

about_me_list = ((return_3).split('.'))
print((about_me_list))