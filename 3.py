N, M = map(int,input().split("x"))
K=int(input())
Q=N*M
if Q>K and K%N==0:
    print("успешно")
elif Q>K and K%M==0:
    print("успешно")
else:
    print("неосуществимо")
