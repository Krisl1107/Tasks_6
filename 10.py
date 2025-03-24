import math
import turtle as trtl
a=int(input())
b=int(input())
c=int(input())
d=int(input())
x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
trtl.up()
trtl.goto(x1,y2)
trtl.down()
trtl.forward(a)
trtl.left(90)
trtl.forward(b)
trtl.left(90)
trtl.forward(a)
trtl.left(90)
trtl.forward(b)
trtl.up()
trtl.goto(x2,y2)
trtl.down()
trtl.right(90)
trtl.forward(c)
trtl.left(90)
trtl.forward(d)
trtl.left(90)
trtl.forward(c)
trtl.left(90)
trtl.forward(d)
trtl.right(90)
xm1=x1+a/2
ym1=y1+b/2
xm2=x2-c/2
ym2=y2-d/2
distance=math.sqrt((xm1-xm2)**2+(ym1-ym2)**2)
if distance==(a/2+c/2):
    print('прямоугольники имеют касание')
elif distance<(a/2+c/2) and (distance>(a/2) or distance>(c/2)):
    print('прмоугольники имеют пересечение')
elif distance>(a/2+c/2):
    print('прямоугольники лежат вне друг друга не касаясь')
else:
    print('один прямоуголь
