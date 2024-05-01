r=[]
for q in range(5):
    a=input('请输入成绩：')
    r.append(a)


n=input('请输入查询成绩：')
c=0
for i in range(len(r)):
    if r[i]==n:
        c+=1
print(c)

