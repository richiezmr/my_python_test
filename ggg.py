import random
import time
'''
time.strftime()
time.localtime()
time.
'''
rd=random
from openpyxl import Workbook
wb=Workbook()
sht=wb.active
for i in range(1,21):
    for e in range(1,9):
        rt=['+','-','×','÷']
        ff=rt[random.randint(0,3)]
        sht.cell(i,e).value='%d%s%d=' % (random.randint(1,100), ff, random.randint(1,100))
wb.save(f'richie_{time.strftime("%H.%M.%S", time.localtime())}.xls')
random.randint(1,100)
 
