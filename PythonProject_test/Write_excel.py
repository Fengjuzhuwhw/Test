import xlwt
def write_excel(path, sheet_name, value,i,j):
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    sheet.write(i,j,value)# 向表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    # print("xls格式表格写入数据成功！")