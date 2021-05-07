import openpyxl
from openpyxl.chart import BarChart, Reference, Series

wb = openpyxl.load_workbook('四半期別売上報告書.xlsx')
ws = wb['支店別売上サマリ']

chart = BarChart()
chart.title = 'A支店とB支店の売上推移'

values = Reference(ws, min_col=1, min_row=1, max_col=3, max_row=5)
chart.add_data(values, titles_from_data=True)

xvalues = Reference(ws, min_col=1, min_row=2, max_col=1, max_row=5)
chart.set_categories(xvalues)

ws.add_chart(chart, 'A8')
wb.save('四半期別売上報告書_グラフ追加済.xlsx')
