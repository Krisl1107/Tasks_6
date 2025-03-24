A, B = map(int,input().split("x"))
C, D, E = map(int,input().split("x"))
if A>=C and B>=D:
    print("да")
elif B>=C and A>=D:
    print("да")
elif B>=E and A>=D:
    print("да")
elif B>=E and A>=C:
    print("да")
elif A>=E and B>=D:
    print("да")
elif A>=E and B>=C:
    print("да")
else:
    print("нет")
