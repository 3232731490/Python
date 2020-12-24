import urllib.parse as up
import urllib.request as ur

def dowload_page( url, filename):
    print("正在下载"+filename)
    request=ur.Request(url,headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"})
    return ur.urlopen(request).read()

def ful_url(url,start,end):
    pn=(end-start)*50
    fulurl=url+"&pn="+str(pn)
    for page in range(start,end+1):
        filename="第"+str(page)+"页.html"
        html=dowload_page(fulurl,filename)
        write_page(html,filename)

def write_page(html,filename):

    print("正在保存",filename)
    with open(filename,"wb") as f:
        f.write(html)
    print("-"*50)


if __name__ == "__main__":
    str1=input("请输入您要爬取哪个贴吧的页面：")
    start_page=int(input("请输入起始页面"))
    end_page=int(input("请输入结束页"))

    url="https://tieba.baidu.com/f?"
    key={"kw":str1}
    key=up.urlencode(key)
    fulurl=url+key
    ful_url(fulurl,start_page,end_page)