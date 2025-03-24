K=int(input())
if K<100:
    lst=K%10
elif 1000>K>100:
    lst_1=K%100

if K<=5 and K%5==0 or K<=5 and K%7==0:
    print("да")
elif K>7 and lst==7 or K>7 and lst==2 and (K-7)%5==0:
    print("да")
elif K>14 and lst==4 and (K-14)%5==0:
    print("да")
elif K>21 and lst==1 and (K-21)%5==0:
    print("да")
elif K>28 and lst==8 and (K-28)%5==0:
    print("да")
elif K>49 and lst==9 and (K-49)%5==0:
    print("да")
elif K>56 and lst==4 and (K-56)%5==0:
    print("да")
elif K>63 and lst==3 and (K-63)%5==0:
    print("да")
else:
    print("нет")
