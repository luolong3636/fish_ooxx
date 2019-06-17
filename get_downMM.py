import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36')
    response = urllib.request.urlopen(req) 
    html = response.read()
    
    return html

#获取是在第几页，如【http://jandan.net/ooxx/page-16#comments】是得到整型数16
def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    
    return html[a:b]
    #print(html[a:b])

'''获取图片的地址如[http://wx2.sinaimg.cn/mw600/0076BSS5ly1g44eng0ohij30jg0t64ds.jpg
]
    返回一个包含这个页面所有图片地址的列表[img_adds]'''
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_adds = []

    a = html.find('img src=')
    

    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b !=-1:
            img_adds.append('http:' + html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=', b)

    return img_adds
'''
    for each in img_adds:
        print(each)    '''        
    

#将列表【img_addrs】里所有图片保存在文件夹【folder】里。
def save_imgs(folder, img_adds):
    for each in img_adds:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)



#默认创建ooxx文件夹，下载前10页的图片·1
def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'

    #加1是为了遍历从默认第10页[10,9,8.....1]到第一页
    page_num = int(get_page(url)) + 1

    for i in range(pages):
        page_num -= 1
        page_url = url + 'page-' + str(page_num) + '#comments'
        print(page_url)
        img_adds = find_imgs(page_url)
        save_imgs(folder, img_adds)
        
if __name__ == '__main__':
    download_mm()
