#scrapy是纯python实现一个为了爬取网站数据、提取结构性数据而编写的应用框架
#scrapy使用了Twisted异步网络框架来处理网络通讯，可以加快我们的下载速度
'''
Spiders(爬虫):它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)
Engine(引擎)：负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。
Scheduler(调度器)：它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。
Downloader(下载器)：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理
ItemPipeline(管道):它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.
Downloader Middlewares（下载中间件）：你可以当作是一个可以自定义扩展下载功能的组件。
Spider Middlewares（Spider中间件）：你可以理解为是一个可以自定扩展和操作引擎和Spider中间
通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）

'''
'''
创建项目：scrapy startproject xxx
进入项目：cd xxx
基本爬虫：scrapy genspider xxx（爬虫名） xxx.com （爬取域）
还有一条是规则爬虫的命令，只是这条有变化，前俩条不变
规则爬虫：scrapy genspider -t crawl xxx（爬虫名） xxx.com （爬取域）
运行命令：scrapy crawl xxx -o xxx.json
'''
'''
制作爬虫步骤：
    新建项目（scrapy startproject xxx） :新建一个新的爬虫项目
    明确目标（编写items.py）  ：明确你要抓取的目标
    制作爬虫（spider/xxxspider.py）  :制作爬虫开始爬取网页
    存储数据(pipelines.py)  设计管道存储爬取内容
'''