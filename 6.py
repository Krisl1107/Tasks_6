N, K, M = map(int,input().split())
if N%K==0:
 time=N//K*M*2
else:
    time = N // K * M * 2 + M * 2
print(time)
