import random as m
a=int(m.random())
print(a)
w=['1','2','3','4','5','6','7','8','9','0']

while a>2 and a<4:
    s=input()
    if s==123456787666554321:
        print('good')
        w[w%10]