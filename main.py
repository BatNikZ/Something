






x = "print('Привет')"
eval(x)

y = 'print("5 + 10 =", (5+10))'
eval(y)

c = 'print("90 * 90 =", (90*90))'
eval(c)

import struct

small = '''print('something abaot')
print('without it')'''
exec(small)

small1 = '''print('nothing more') 
print('all you can')'''
exec(small1)

d = 'print("76 + 908 =", (76 + 908))'
eval(d)

f = "print('Hi my man')"
eval(f)

len('its mean nothing')

try_list = ['okay', 'idiot', 'drakon']
print(len(try_list))

enemies_map = {'Batman' : 'Vatman',
               'superman' : 'strangelove'}
print(len(enemies_map))

fruit = ['apple', 'banano', 'cherry']
d1 = len(fruit)
for x in range(0, d1):
    print('fruit with index %s: %s' % (x, fruit[x]))

num = [5, 4, 300, 434, 900]
print(max(num))

strings = 'stringsSTRINGS'
print(max(strings))

print(max(100,2300, 2390, 498))

guess_this_num = 195
play_guess = [12, 15, 70, 1900]
if max(play_guess) > guess_this_num:
    print('you lose')
else: print('you win')

print(list(range(0, 5)))

count_by_two = list(range(500, 90, -5))
print(count_by_two)

list1 = list(range(0, 700, 50))
print(list1)
print(sum(list1))

a = abs(100) + abs(-100)
print(a)
a1 = abs(90) * abs(-90)
print(a1)
a2 = abs(-1000) + -10
print(a2)

call = 'if this opportunity for you is bad '
