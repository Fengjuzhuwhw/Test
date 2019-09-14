import urllib.request
import urllib.parse
import json  # 基于JavaScript语言的轻量级的数据交换格式(JavaScript Object Notation)
import time
import Read_excel
import xlrd
import Write_excel
from xlutils.copy import copy

def translation(word):
    # while True:
    content = word  # input("请输入与要翻译的内容(输入q退出)：")
    # if content == 'q':
    #     break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '15679066560285',
            'sign': '16d1e7415bb0de1c1d43f641e81aea35',
            'ts': '1567906656028',
            'bv': 'bbb3ed55971873051bc2ff740579bb49',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'
            }
    '''
    第一种加head的方式，只能通过urllib.request.Request(url,data,head)添加，避免网站监测出是代码进行访问
    head={}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    '''
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data)
    # 第二种添加head的方法
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8') #把“utf-8”解码成python默认的unicode编码形式


    target = json.loads(html)
    # print(type(html))
    # print(type(target))


    # json.load()  # 将一个存储在文件中的json对象（str）转化为相对应的python对象
    # json.loads()  # 将一个json对象（str）转化为相对应的python对象
    # 如果你要处理的是文件而不是字符串，你可以使用json.dump() 和json.load()来编码和解码JSON数据
    # json.dump()  # 将python的对象转化为对应的json对象（str),并存放在文件中
    # json.dumps()  # 将python的对象转化为对应的json对象（str)
    return target['translateResult'][0][0]['tgt']
    # print("翻译的结果是：%s" % (target['translateResult'][0][0]['tgt']))



result=[]

if __name__ == '__main__':
    worlds = Read_excel.read_excel()
    # print(worlds)
    # print(len(worlds))
    # for i in range(len(worlds)):
    #         print(len(worlds[i]))
    # for i in range(len(worlds)):
    #     for j in range(len(worlds[i])):
    #         print(worlds[i][j])
    for i in range(len(worlds)):
        for j in range(len(worlds[i])):
            # result.append(translation(worlds[i][j]))
            # Write_excel.write_excel(r'result.xls', "工作表一", translation(worlds[i][j]), i,j)
            #write_excel()并不能追加数据，所以此方法不成立
            workbook = xlrd.open_workbook(r'result.xls')  # 打开工作簿
            sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
            new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
            new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
            new_worksheet.write(i, j, translation(worlds[i][j]))  # 追加写入数据
            # time.sleep(1)  # 为了避免代码频繁的访问浏览器，导致被拒绝访问
            # print(translation(worlds[i][j]))
            new_workbook.save(r'result.xls')  # 保存工作簿



# translation('word')
#     # print(result)
