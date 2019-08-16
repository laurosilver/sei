import xlrd


workbook = xlrd.open_workbook('365_contratos.xlsm')
worksheet = workbook.sheet_by_name('RC')

valor = worksheet.cell(1,0).value
credor = worksheet.cell(1,1).value
obs = worksheet.cell(1,2).value.strip()
ig = (worksheet.cell(1,4).value).strip()
total_linhas = worksheet.nrows
total_colunas = worksheet.ncols

table = list()
record = list()





'''for x in range(total_colunas):
    for y in range(total_linhas):
        record.append(worksheet.cell(y,x).value)
        valor = worksheet.cell(y, x).value
        print(valor)
    table.append(record)
    record = []
    y += 1'''
x = 0
y = 0


for x in range(total_linhas):
    for y in range(total_colunas):
        if y == 0:
            valor = worksheet.cell(x,y).value
            valor = str(valor).strip().upper()
        elif y == 1:
            credor = worksheet.cell(x,y).value
            credor = str(credor).strip().upper()
        elif y == 2:
            obs = worksheet.cell(x, y).value
            obs = str(obs).strip().upper()
        elif y == 4:
            ig = worksheet.cell(x, y).value
            ig = str(ig).strip().upper()

    print(valor)










'''print(valor)
print(credor)
print(obs)
print(ig)
print(total_linhas)'''