import openpyxl
from openpyxl.chart import BarChart, Reference, Series

wb = openpyxl.load_workbook('四半期別売上報告書.xlsx')
ws = wb['支店別売上サマリ']

ref_obj = Reference(ws, min_col=2, min_row=2, max_col=2, max_row=5)
series_obj = Series(ref_obj, title='A支店の売上')

chart = BarChart()
chart.title = 'A支店の売上推移'
chart.append(series_obj)

xvalues = Reference(ws, min_col=1, min_row=2, max_col=1, max_row=5)
chart.set_categories(xvalues)
chart.width = 20
chart.x_axis.scaling.max = 10000000

ws.add_chart(chart, 'A8')
wb.save('四半期別売上報告書_グラフ追加済.xlsx')
