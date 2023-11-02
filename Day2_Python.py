Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
type(tao)
<class 'turtle.Turtle'>
tao.shape('turtle')
tao.color('red')
tao.forward(100)
tao.lef(90)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tao.lef(90)
AttributeError: 'Turtle' object has no attribute 'lef'. Did you mean: 'left'?
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.reset()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
for i in range(8):
    tao.forward(100)
    tao.left(45)

    
tao.list = []
tao.reset()
for i in range(8):
    tao.forward(100)
    tao.left(45)

tao.down()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.reset()
tao.list = []
tao1 = turtle.Pen()
>>> tao2 = turtle.Pen()
>>> taolist.append(tao)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    taolist.append(tao)
NameError: name 'taolist' is not defined
>>> taolist.append(tao)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    taolist.append(tao)
NameError: name 'taolist' is not defined
>>> taolist = []
... tao1 = turtle.Pen()
... tao2 = turtle.Pen()
... taolist.append(tao)
SyntaxError: multiple statements found while compiling a single statement
>>> taolist = []
>>> tao1 = turtle.Pen()
>>> tao2 = turtle.Pen()
>>> taolist.append(tao)
>>> taolist.append(tao1)
>>> taolist.append(tao2)
>>> print(taolist)
[<turtle.Turtle object at 0x0000020345C7A120>, <turtle.Turtle object at 0x0000020348475CD0>, <turtle.Turtle object at 0x0000020348475EE0>]
>>> taolist[0].forward(200)
>>> taolist[1].backward(200)
>>> taolist[2].color('red')

import totou