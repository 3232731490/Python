#scrapy�Ǵ�pythonʵ��һ��Ϊ����ȡ��վ���ݡ���ȡ�ṹ�����ݶ���д��Ӧ�ÿ��
#scrapyʹ����Twisted�첽����������������ͨѶ�����Լӿ����ǵ������ٶ�
'''
Spiders(����):������������Responses,���з�����ȡ���ݣ���ȡItem�ֶ���Ҫ�����ݣ�������Ҫ������URL�ύ�����棬�ٴν���Scheduler(������)
Engine(����)������Spider��ItemPipeline��Downloader��Scheduler�м��ͨѶ���źš����ݴ��ݵȡ�
Scheduler(������)��������������淢�͹�����Request���󣬲�����һ���ķ�ʽ�����������У���ӣ���������Ҫʱ�����������档
Downloader(������)����������Scrapy Engine(����)���͵�����Requests���󣬲������ȡ����Responses������Scrapy Engine(����)�������潻��Spider������
ItemPipeline(�ܵ�):��������Spider�л�ȡ����Item�������н��к��ڴ�����ϸ���������ˡ��洢�ȣ��ĵط�.
Downloader Middlewares�������м����������Ե�����һ�������Զ�����չ���ع��ܵ������
Spider Middlewares��Spider�м��������������Ϊ��һ�������Զ���չ�Ͳ��������Spider�м�
ͨ�ŵĹ���������������Spider��Responses;�ʹ�Spider��ȥ��Requests��

'''
'''
������Ŀ��scrapy startproject xxx
������Ŀ��cd xxx
�������棺scrapy genspider xxx���������� xxx.com ����ȡ��
����һ���ǹ�����������ֻ�������б仯��ǰ��������
�������棺scrapy genspider -t crawl xxx���������� xxx.com ����ȡ��
�������scrapy crawl xxx -o xxx.json
'''
'''
�������沽�裺
    �½���Ŀ��scrapy startproject xxx�� :�½�һ���µ�������Ŀ
    ��ȷĿ�꣨��дitems.py��  ����ȷ��Ҫץȡ��Ŀ��
    �������棨spider/xxxspider.py��  :�������濪ʼ��ȡ��ҳ
    �洢����(pipelines.py)  ��ƹܵ��洢��ȡ����
'''