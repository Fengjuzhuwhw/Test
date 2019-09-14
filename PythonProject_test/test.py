# #1
# str='wuhaiwen'
# print(str.find('i'))
# #2
# img_addrs='D:\Python3.7.4\project'
# filename = img_addrs.split('\\')[-1]
# print(filename)

#3
# import xlrd
# arrayNum = 6
# #array = {'L1':'','L2':'','L3':'','L4':'','Question':'','Answer':''}
# tables = []
# newTables = []
#
# def read_excel():
#     # 打开文件
#     workbook = xlrd.open_workbook(r'AWL.xlsx')
#     # 获取所有sheet
#     sheet_name = workbook.sheet_names()[0]
#     # print(sheet_name)
#     # 根据sheet索引或者名称获取sheet内容
#     sheet = workbook.sheet_by_index(0) # sheet索引从0开始
#     # sheet = workbook.sheet_by_name('Sheet1')
#
#     #print (workboot.sheets()[0])
#     # sheet的名称，行数，列数
#     print (sheet.name,sheet.nrows,sheet.ncols)
#
#     # 获取整行和整列的值（数组）
#     rows = sheet.row_values(1) # 获取第2行内容
#     # cols = sheet.col_values(2) # 获取第3列内容
#     print (rows)
#     # print (cols)
#
#     for rown in range(sheet.nrows):
#        array = {'L1':'','L2':'','L3':'','L4':'','Question':'','Answer':''}
#        array['L1'] = sheet.cell_value(rown,0)
#        array['L2'] = sheet.cell_value(rown,1)
#        array['L3'] = sheet.cell_value(rown,2)
#        array['L4'] = sheet.cell_value(rown,3)
#        array['Question'] = sheet.cell_value(rown,4)
#        array['Answer'] = sheet.cell_value(rown,5)
#        tables.append(array)
#
#     print (len(tables))
#     #print (tables)
#     #print (tables[5])
# if __name__ == '__main__':
#     # 读取Excel
#     read_excel();
#     print ('读取成功')
# import string
#
# print(type(string))
# print(type(str))
import os
from multiprocessing import Process
def run_proc(name):
    print('Child process %s(%s)Running...'%(name,os.getpid()))
if __name__=='__main__':
    print("Parent process %s." % os.getpid())
    for i in range(5):
        p=Process(target=run_proc,args=(str(i),))
        print('Process will start.')
        p.start()
    p.join()
    print('Process end')

