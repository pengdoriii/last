A,B=map(int,input().split())
num=[0]*(A)
b=0
for b in range(A):
    num[b]=b+1

for _ in range(B):
    i,j=map(int,input().split())
    l=num[j-1]
    q=num[i-1]
    num[i-1]=l
    num[j-1]=q

for i in range(A):
    print(num[i], end=' ')


A = int(input())
B = int(input())
E=0
for i in range(1, B+1):
    C,D=map(int,input().split())
    E=E+C*D

if E==A:
    print("Yes")
else:
    print("No")

    num = [0] * 28
    for i in range(28):
        j = int(input())
        num[i] = j
    for k in range(1, 31):
        if k not in num:
            print(k)
