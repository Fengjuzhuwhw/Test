import urllib.request #导入请求网页模块
import os


def url_open(url):  #打开主网站url，获取整个html字符串
    req = urllib.request.Request(url)    #请求网页数据
    req.add_header('User-Agent',           #使用add_header()添加HTTP报头，伪装为人为访问
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    response = urllib.request.urlopen(url) #得到浏览器回复
    html = response.read()   #对浏览器回复进行阅读

    return html


def get_page(url):    #分析html字符串，获得当前页数
    html = url_open(url).decode('utf-8')  #调用自定义函数url_open得到所需要的页面数据，因为python默认是Unicode编码形式，所以必须将其解码
    # print(type(html)) 输出类型为str
    a = html.find('current-comment-page') + 23  #找到此页面的页数，即<span class="current-comment-page">[8]</span>中的8，该行找到8的左边
    b = html.find(']', a)             #find（str，a,b）str为所要找的字符串，a为所要找的起始位置，b为所要找的结束位置
    # print(html)
    return html[a:b]                  #得到字符8，即页数


def find_imgs(url):     #分析html字符串，找出图片地址
    html = url_open(url).decode('utf-8')
    img_addrs = []    #设置图片地址列表，存放图片地址

    a = html.find('img src=') #找到含有'img src='字符串的起始位置

    while a != -1: #如果找得到起始地址
        b = html.find('.jpg', a, a + 255) #在（a，a+255）的范围内寻找.jpg字符串，+255因为网页地址一般没有255字符的长度
        #例如图片地址<img src="//wx2.sinaimg.cn/mw600/0076BSS5ly1g6u5d14lffj30bs0gomzb.jpg" referrerpolicy="no-referrer" style="max-width: 480px; max-height: 750px;">
        if b != -1: #如果找得到结束地址
            img_addrs.append(('http:' + html[a + 9:b + 4]))  #将找到的图片地址依次加入img_addrs列表中
        else:
            b = a + 9 #如果找不到.jpg字符串，即将查找的结束位置赋值为起始位置，即开始下一轮查找

        a = html.find('img src=', b) #下一轮查找起始位置即本轮查找的结束位置
    #print(img_addrs)
    return img_addrs #返回所要查找的所有图片地址列表


def save_imgs(folder, img_addrs): #保存图片
    for each in img_addrs:
        filename = each.split('/')[-1] #文件名为最后一个字符串
        with open(filename, 'wb') as f: #with可以不用关文件，即f.close()'wb'为二进制写入
            img = url_open(each) #打开每一个图片地址
            #print(img)
            f.write(img)        #将图片写入文件夹


def download_mm(folder='ooxx', pages=10): #主函数，下载图片，传入文件夹名’ooxx‘，默认页数为10
    os.mkdir(folder)   #创建一个文件夹，需要调用os模块
    os.chdir(folder)   #os.chdir() 方法用于改变当前工作目录到指定的路径。

    url = "http://jandan.net/ooxx/"  #输入网页地址
    page_num = int(get_page(url))     #获得当前页数

    for i in range(page_num):
        page_num -= 1
        page_url = url + 'page-' + str(page_num) + '#comments' #http://jandan.net/ooxx/page-8#comments #获得页面地址
        img_addrs = find_imgs(page_url) #从当前页面找到图片地址
        save_imgs(folder, img_addrs)   #保存当前页面图片


if __name__ == '__main__': #__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
    download_mm()
