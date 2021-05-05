import openpyxl

wb = openpyxl.load_workbook('売上報告書.xlsx', data_only=True)
sheet = wb['売上データ']

branch_list = list(sheet.columns)[2]
sales_per_quarter = [0, 0, 0, 0]

# A支店の四半期ごとの売上を集計する
for i, cell in enumerate(branch_list):
    if cell.value == "A支店":
        for j in range(4):
            sales_per_quarter[j] += sheet.cell(row=i + 1, column=4 + j).value

print('第1四半期', sales_per_quarter[0])
print('第2四半期', sales_per_quarter[1])
print('第3四半期', sales_per_quarter[2])
print('第4四半期', sales_per_quarter[3])
