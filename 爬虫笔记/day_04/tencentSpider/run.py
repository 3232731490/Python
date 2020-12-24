import sys
import os

from scrapy.cmdline import execute

#命令行执行需要将当前目录加到pythonpath中
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","tencent"])