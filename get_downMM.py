import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html

    

def get_page(url):
    
    html = url_open(url).decode('utf-8')
    
    p = r'<span class="current-comment-page">\[(\d+)\]</span>'
    page = re.findall(p, html)

    return page



def find_imgs(url):
    
    html = url_open(url).decode('utf-8')
  
    p = r'<img .*?src="([^"]*\.jpg)".*?>'
    img_addrs = re.findall(p, html)

    
    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        each = 'http:' + each
        
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)



def download_mm(folder="ooxx", pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url)[0]) + 1
    
    
    for i in range(pages):
        page_num -= 1
        page_url = url + 'page-' + str(page_num) + '#comment'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)
        
        
if __name__ == '__main__':
    download_mm()
