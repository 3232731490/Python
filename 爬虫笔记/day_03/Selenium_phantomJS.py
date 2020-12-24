#Selenium是一个Web的自动化测试工具，它可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断页面上某些动作是否已经发生
#PhantomJS是一个基于WebKit的“无界面”浏览器，它可以把网站加载到内存并执行页面上的javas代码，因为不会展示图形界面，所以运行起来比完整的浏览器更加高效
import io
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys

#print()函数的局限就是Python默认编码的局限，因为系统是win7的，python的默认编码不是'utf-8',改一下python的默认编码成'utf-8'就行了
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

'''
selenium定位元素方法：
    find_element_by_id()
    find_element_by_name()
    find_element_by_class_name()
    find_element_by_tag_name()
    find_element_by_link_text()
    find_element_by_partial_link_text()
    find_element_by_xpath()
    find_element_by_css_selector()

网页前进后退：
    driver.back()
    driver.forward()
    
控制窗口大小：
    设置浏览器宽480、高800显示：
    driver.set_window_size(480, 800)
    
点击和输入：
    clear()： 清除文本。
        driver.find_element_by_id("kw").clear()

    send_keys (value)： 模拟按键输入。
        driver.find_element_by_id("kw").send_keys("selenium")
    
    click()： 单击元素。
        driver.find_element_by_id("su").click()
    
提交：
    submit()
        search_text = driver.find_element_by_id('kw')
        search_text.send_keys('selenium')
        search_text.submit()
    
其他常用方法：
    size： 返回元素的尺寸。
        size = driver.find_element_by_id('kw').size
        
    text： 获取元素的文本。
    get_attribute(name)： 获得属性值。
    is_displayed()： 设置该元素是否用户可见。
    
鼠标事件：
    perform()： 执行所有 ActionChains 中存储的行为；
    context_click()： 右击；
    double_click()： 双击；
    drag_and_drop()： 拖动；
    move_to_element()： 鼠标悬停。
    
        鼠标悬停操作：
            # 引入 ActionChains 类
            from selenium.webdriver.common.action_chains import ActionChains
            
            driver = webdriver.Chrome()
            driver.get("https://www.baidu.cn")

            # 定位到要悬停的元素
            above = driver.find_element_by_link_text("设置")
            # 对定位到的元素执行鼠标悬停操作
            ActionChains(driver).move_to_element(above).perform()
                
                from selenium.webdriver import ActionChains
                    导入提供鼠标操作的 ActionChains 类。

                ActionChains(driver)
                    调用 ActionChains()类， 将浏览器驱动 driver 作为参数传入。

                move_to_element(above)
                    context_click()方法用于模拟鼠标右键操作， 在调用时需要指定元素定位。

                perform()
                    执行所有 ActionChains 中存储的行为， 可以理解成是对整个操作的提交动作。


键盘操作：
    send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
    send_keys(Keys.SPACE) 空格键(Space)
    send_keys(Keys.TAB) 制表键(Tab)
    send_keys(Keys.ESCAPE) 回退键（Esc）
    send_keys(Keys.ENTER) 回车键（Enter）
    send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
    send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
    send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
    send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
    send_keys(Keys.F1) 键盘 F1
    ……
    send_keys(Keys.F12) 键盘 F12
        
        from selenium.webdriver.common.keys import Keys
        # 删除多输入的一个 m
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        # 输入空格键+“教程”
        driver.find_element_by_id("kw").send_keys(Keys.SPACE)
        driver.find_element_by_id("kw").send_keys("教程")

断言：      
    title：用于获得当前页面的标题。
    current_url：用户获得当前页面的URL。
    text：获取搜索条目的文本信息。
    
显示等待：
    WebDriverWait类是由WebDirver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。具体格式如下：
        WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
            driver ：浏览器驱动。
            timeout ：最长超时时间，默认以秒为单位。
            poll_frequency ：检测的间隔（步长）时间，默认为0.5S。
            ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。

    WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。
        until(method, message=‘’)
            调用该方法提供的驱动程序作为一个参数，直到返回值为True。
        until_not(method, message=‘’)
            调用该方法提供的驱动程序作为一个参数，直到返回值为False。
            
隐式等待：
    WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0。它的用法相对来说要简单得多。
        driver.implicitly_wait(10)
            implicitly_wait() 默认参数的单位为秒，本例中设置等待时长为10秒。首先这10秒并非一个固定的等待时间，它并不影响脚本的执行速度。
            其次，它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；
            如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。假设在第6秒定位到了元素则继续执行，
            若直到超出设置时长（10秒）还没有定位到元素，则抛出异常。
'''


'''
utf8	    所有语言
gbk	        简体中文
gb2312  	简体中文
gb18030	    简体中文
big5	    繁体中文
big5hkscs	繁体中文
'''

driver=webdriver.PhantomJS()
#如果没有添加环境变量则需要在参数中加入这个executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe'

driver.get(url="http://www.baidu.com/")

#data=driver.find_element_by_id("wrapper").text.encode('utf-8')

#打印标题
#print(driver.title)

#生成当前页面快照并保存
#driver.save_screenshot("baidu.png")

#id='kw'是百度搜索框，输入字符串“美女”
driver.find_element_by_id('kw').send_keys('美女')

#id='su'是搜索按钮，click（）是模拟点击
driver.find_element_by_id('su').click()

#driver.save_screenshot("baidu.png")

#打印页面源码
#print(driver.page_source)

#模拟回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)

#获取cookie
#print(driver.get_cookies())

#获取当前url
print(driver.current_url)

#print(data.decode('utf-8'))