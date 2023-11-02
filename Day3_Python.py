Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cars = ['toyota','honda','benz']
cars.append('byd')
print(cars)
['toyota', 'honda', 'benz', 'byd']
cars.remove('honda')
print(cars)
['toyota', 'benz', 'byd']
cars.insert(0,'tesla')
print(cars)
['tesla', 'toyota', 'benz', 'byd']
print(car{0])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
print(cars[0])
tesla
for c in cars
SyntaxError: incomplete input
for c in cars:
    print(c)

    
tesla
toyota
benz
byd
print(*cars)
tesla toyota benz byd
for i,c in enumerate(cars):
    print(i,c)

    
0 tesla
1 toyota
2 benz
3 byd
for i,c in enumerate(cars, star=0):
    print('ลำดับที่ {} {}'.format(i,c))

    
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for i,c in enumerate(cars, star=0):
TypeError: 'star' is an invalid keyword argument for enumerate()
for i,c in enumerate(cars, star=0):
    print('ลำดับที่ {} {}'.format(i,c))

    
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    for i,c in enumerate(cars, star=0):
TypeError: 'star' is an invalid keyword argument for enumerate()
for i,c in enumerate(cars, start=0):
    print('ลำดับที่ {} {}'.format(i,c))

    
ลำดับที่ 0 tesla
ลำดับที่ 1 toyota
ลำดับที่ 2 benz
ลำดับที่ 3 byd
for i,c in enumerate(cars, start=1):
    print('ลำดับที่ {} {}'.format(i,c))
... 
...     
ลำดับที่ 1 tesla
ลำดับที่ 2 toyota
ลำดับที่ 3 benz
ลำดับที่ 4 byd
>>> sort(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sort(c)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> cars.sort()
>>> 
>>> print(c)
byd
>>> 
>>> print(cars)
['benz', 'byd', 'tesla', 'toyota']
>>> ord('ก')
3585
>>> for i in rang(3585,10):
...     print(char(i))
... 
...     
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for i in rang(3585,10):
NameError: name 'rang' is not defined. Did you mean: 'range'?
>>> for i in range(3585,10):
...     print(char(i))
... 
...     
>>> 
>>> for i in range(3585,3590):
...     print(char(i))
... 
...     
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    print(char(i))
NameError: name 'char' is not defined. Did you mean: 'chr'?
