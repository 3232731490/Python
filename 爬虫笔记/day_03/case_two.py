
#导入webdirver API对象，可以调用浏览器和操作页面
from selenium import webdriver
#导入Keys，可以使用操作键盘，标签、鼠标
from selenium.webdriver.common.keys import Keys
import io
import sys
from bs4 import BeautifulSoup as bs

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
#创建浏览器对象
driver=webdriver.PhantomJS()

url='https://www.douyu.com/directory/all'
url1='https://www.huya.com/l'

driver.get(url1)

#print(driver.save_screenshot('douban.png'))

#driver.find_element_by_name('form_email').send_keys('18582699881')
#driver.find_element_by_name('form_password').send_keys('20021112nl')

#driver.find_element_by_class_name('btn btn-account btn-active').click()

#print(driver.save_screenshot('douban.png'))
'''
下一页是否能点标记，true表示已到最后一页
    aria-disabled
    也可以通过判断源码里是否有这个标记来判断是否到了最后一页
    dy-Pagination-disabled dy-Pagination-next
    
div class="DyListCover-userName"  用户名
span class="DyListCover-zone"    直播板块
h3 class="DyListCover-intro"    标题  /   h3 title="换个游戏摸摸"

'''
'''
虎牙
    <i class="nick" title="霸哥">霸哥</i>
    <i class="js-num">349.9万</i>
    <a class="laypage_next" data-page="140">下一页</a>
'''
#driver.save_screenshot('huya.png')

#print(soup)
#print(type(soup))
count=0
#print(soup.find_all('a',{'class':'laypage_next'})[0].text)
while True:
    soup = bs(driver.page_source, 'html.parser')
    name_list=soup.find_all('i',{'class':'nick'})
    hot_list=soup.find_all('i',{'class':'js-num'})
    for name,hot in zip(name_list,hot_list):
        count+=1
        print(u'房间热度： '+str(hot.get_text())+u'\t房间名： ' +str(name.get_text()))
    try:
        driver.find_element_by_class_name('laypage_next').click()
    except:
        break
print("当前共有：" +str(count)+"个主播开播")