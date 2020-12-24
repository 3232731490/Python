import urllib.request as ur
import os
import random
def open_url(url):
    req = ur.Request(url)
    response = ur.urlopen(req)
    html = response.read()
    return html

def get_img_urls(url):
    html=open_url(url).decode('utf--8')

    a=html.find('img src=')

    img_urls=[]
    while a!=-1:
        b = html.find('.jpg', a, a + 100)
        if b!=-1:
            print(html[a+9:b+4])
            img_urls.append(html[a+9:b+4])
        else:
            b=a+9
        a=html.find('img src=',b)
    return img_urls

def save_picture(img_url):
    file_name=img_url.split('/')[-1]
    response=open_url(img_url)

    with open(file_name,'wb') as f:
        f.write(response)
def download_mm(floader='mm',pages=3):
    os.mkdir(floader)
    os.chdir(floader)
    url='https://www.ivsky.com/tupian/'
    img_urls=get_img_urls(url)

    for each in range(pages):
        save_picture('https:'+random.choice(img_urls))


download_mm('随便爬取的图3',10)