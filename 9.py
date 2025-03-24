import math
import turtle as trtl
r1=int(input())
r2=int(input())
x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
trtl.up()
trtl.goto(x1,y1-r1)
trtl.down()
trtl.circle(r1)
trtl.up()
trtl.goto(x2,y2-r2)
trtl.down()
trtl.circle(r2)
distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
if distance > r1 + r2:
    print('Окружности лежат одна вне другой, не касаясь.')
elif distance == r1 + r2:
    print('Окружности имеют внешнее касание.')
elif abs(r1 - r2) < distance < r1 + r2:
    print('Окружности пересекаются.')
elif distance == abs(r1 - r2):
    print('Окружности имеют внутреннее касание.')
elif distance < abs(r1 - r2):
    print('Окружность лежит внутри другой, не касаясь.')
else:
    print('Неизвестное расположение.')
