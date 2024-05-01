'''a=int(input('请输入:'))
u=0
def m():
    while u!=a:
        for t in range(a):
            q=u+1
        print(q)
        if u==a:
            break
m()'''
a=int(input('请输入：'))
sum=0

# 1: sum=1
# 2: sum=3
# 3: sum=6
# orig: 1+2+3=6
for y in range(1, a+1):
    #print(y)
    sum=sum+y
    #print(f"current sum: {sum}")
print(f'sum: {sum}')


## 1+2+3+4+5+6......+9998 + 9999
## 5*2=10
## 7*3=21
## （9998/2） * 9999
## 10000 * （9999/2）
# 10000 + 10000 + 10000

#1 2 3 4 5

#6 * （5/2)