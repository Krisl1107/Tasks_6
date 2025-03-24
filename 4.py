pstng = input()
ltr = pstng[0]
n = int(pstng[1])
ltr_n = ord(ltr) - ord('a') + 1
if (ltr_n + n) % 2 == 0:
    print('черная')
else:
    print('белая')

