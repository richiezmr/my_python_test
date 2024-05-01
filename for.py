import random
num=random.randint(1,10)
for i in range(5):
    a=int(input('输入'))
    if a > num:
        print('太大')
    elif a <num:
        print('太小')
    else:
        print('对了！！！')
        break
    if i==2:
        print('恭喜你答错了,答案是:'+str(num))
