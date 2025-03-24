pstng = input()
ltr = pstn[0]
n = int(positioning[1])
ltr_n = ord(ltr) - ord('a') + 1
if (ltr_n + n) % 2 == 0:
    print('черная')
else:
    print('белая')

