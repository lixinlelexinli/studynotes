爬取https://www.jin10.com，存入mongodb

1. 新建scrapy项目

   scrapy startproject jin10

2. 设置setting、

   * ROBOTSTXT_OBEY=False
   * 打开USER_AGENT
   * 打开DOWNLOAD_DELAY
   * 打开ITEM_PIPELINES

3. 进入项目，生成爬取的文件

   ```
   cd jin10
   scrapy genspider jinshi jin10.com
   ```

4. 编写ITEM_PIPELINES

5. 创建执行文件startrun.py  

   ```python
   from scrapy.cmdline import execute
   execute("scrapy crawl jinshi".split())
   ```


# 标题

[	]