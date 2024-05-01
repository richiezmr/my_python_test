from openpyxl import Workbook
wb=Workbook()
sht=wb.active
for i in range(1,10):
    for e in range(1,i+1):
        sht.cell(i,e).value='%d+%d=%d' % (i,e,i+e)
wb.save('richie xis')