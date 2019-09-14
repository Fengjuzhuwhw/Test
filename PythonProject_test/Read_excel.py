import xlrd
table1 = []
# table2 = []
def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'AWL.xlsx')
    sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
    # print(sheet.nrows)
    for each_row in range(sheet.nrows):
        content = sheet.row_values(each_row)  # 获取第每行内容
        table1.append(content)
    return table1
    # print(str(tables))
    # print(type(str(tables)))
    # print(len(tables))

    # for each in range(len(table1)):
    #     for i in range(10):
    #         table2.append(table1[each][i])
    #
    # return table2


    # print(table2)
    # # print(len(table2))

if __name__ == '__main__':
    # 读取Excel
    read_excel()
    print('读取成功')