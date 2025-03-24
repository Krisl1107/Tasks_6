pstn = input()
ltr1 = pstn[0]
n1 = int(pstn[1])
ltr2 = pstn[3]
n2 = int(pstn[4])
ltr_1 = ord(ltr1) - ord('a') + 1
ltr_2 = ord(ltr2) - ord('a') + 1
if (abs(ltr_1 - ltr_2) == 1 and
    abs(n1 - n2) == 2) or (abs(ltr_1 - ltr_2) == 2 and
                                     n1 - n2 == 1):
    print('верно')
else:
    print('ошибка')
