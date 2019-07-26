# ChinaQualityNews
本爬虫为中国质量新闻网爬虫，主要爬取检验不合格数据。

## 启动方法
1. 先安装依赖库
```bash
pip install -r requirements.txt
```

2. 创建数据库，和创建表
```bash
python init_db.py
```

3. 运行爬虫
```bash
scrapy crawl cqn
```

## 创建Scrapy爬虫的方法
```bash
scrapy startproject ChinaQualityNews
cd ChinaQualityNews
scrapy genspider -t crawl cqn 'www.cqn.com.cn'
```

## 爬虫xpath抓取调试
通过scrapy 的shell命令来开启交互式的环境进行编写Xpath调试
```bash
scrapy shell 'www.baidu.com'
```
进入交互式环境后可以通过`response`对象来获取结果。
```python
body = response.xpath('.//body')
body
```

## 爬虫缺点和改进点
- 由于页面中大多数的表格列数不一致，而且列的数据项是乱的，所以样要完全抓取有点困难。目前只抓了2019年的数据，但是目前是按照列的多少来区分的，这样会有问题，因为时间仓促，暂时先这样。
- 正确的应该是建立表格字典，将表格的字段通过表头进行映射，找到对应表格的解析方法再进行解析。这样出来的数据就相对完整。