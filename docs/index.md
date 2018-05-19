[TOC]



#DB组python学习技术路线

###  基础知识：

* python语法掌握
* 数据库设计和实施
* http协议基础理解
* git使用
* linux简单操作
* json理解使用
* http协议理解

### 通用工具：

* pycharm 

  PyCharm是一种Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。

* postman

  *Postman*是一款功能强大的网页调试与发送网页HTTP请求的工具

* git

  版本流程控制工具

* markdown

  文档编写工具

### 书籍：

* [廖雪峰 Python 3 中文教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
* [PEP8 Python代码风格规范](https://code.google.com/p/zhong-wiki/wiki/PEP8)
* [Python 正则表达式操作指南](http://wiki.ubuntu.org.cn/Python%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97)

## python爬虫方向学习路线

#### 小白级
***
##### 常用库

* Requests 人性化python http库 功能强大
* Beautifulsoup4 解析器 用于解析得出你想要的信息
* re python 原生正则表达式库 匹配相关信息
* pymysql 连接数据库保存信息

##### 基础技术

* [http基本原理](https://germey.gitbooks.io/python3webspider/2.1-HTTP基本原理.html)


* [Web网页基础](https://germey.gitbooks.io/python3webspider/2.2-Web网页基础.html)
* [爬虫基本原理](https://germey.gitbooks.io/python3webspider/2.3-爬虫基本原理.html)


* [Session和Cookies](https://germey.gitbooks.io/python3webspider/2.4-Session和Cookies.html)


* [代理基本原理](https://germey.gitbooks.io/python3webspider/2.5-代理基本原理.html)

##### 学习成果检验

能够完成小说的内容爬取并存入数据库

#### 入门级
***
##### 常用库

*在小白基础之后*

* Selenium Web应用程序测试工具 ,爬虫中主要用来解决JavaScript渲染问题。模拟浏览器进行网页加载
* Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架

##### 技术

* Ajax数据爬取
* 非关系型数据库存储
* 动态渲染页面抓取
* 验证码的识别
* 模拟登陆

##### 书籍

* python网络爬虫实战
* Python网络数据采集

##### 学习成果检验

独立完成基于scrapy爬虫的天气数据采集



## python数据挖掘和数据可视化方向

#### 小白级

***

##### 常用库

* pandas   Pandas 是python的一个数据分析包
* Numpy 一个用python实现的科学计算包
* wordcloud 基于Python的词云生成类库
* jieba（结巴）是一个强大的分词库，完美支持中文分词
* matplotlib 使用matplotlib能够非常简单的可视化数据
* Pillow *Python*平台事实上的图像处理标准库

##### 技术

* 有自行获取数据的能力(爬虫)
* 具有一定的数学基础
* 可以灵活运用工具和搜索引擎
* 对数据进行统计和分析

##### 书籍

* [Python数据分析与挖掘实战](http://www.baidu.com/link?url=7iLugJISJFENDPN5WMuCEAlqF_yQ8HTyp61TwM447ZqUgbiMMeMIXwwF591XfxSh)


* Python网络数据采集


* 利用Python进行数据分析

##### 学习成果检验

自选任意网站，爬取信息并对数据分析，做出词云或是直方图扇形图类似

#### 入门级

***

##### 常用库

* kivy  Kivy是一个开源工具包能够让使用相同源代码创建的程序能跨平台运行
* wxPython  *wxPython*是Python的的GUI图形库,允许开发者很方便的创建GUI用户界面

##### 技术

* **能够把获取的数据通过在GUI处理并展示**

##### 书籍

暂无

##### 学习成果检验

用GUI展示词云(输入需要解析url或是长文本，显示词云)

## python web开发路线

#### 小白级

##### 常用库

* Flask  一个使用 [Python](https://baike.baidu.com/item/Python) 编写的轻量级 Web 应用框架
* Bootstrap 目前很受欢迎的前端框架 基于HTML，CSS,JavaScript
* Django Web应用框架，由Python写成。采用了MTV的框架模式，即模型M，模板T和视图V

##### 技术

* 了解并能使用前端基本内容，HTML,CSS,JavaScript
* 简单了解WSGI & uwsgi
* 能够灵活使用模板
* 了解ORM，MVC模式
* 可独立写微信小程序

##### 书籍

* Flask Web开发:基于Python的Web应用开发实战
* [Flask 扩展文档汇总](https://www.gitbook.com/book/wizardforcel/flask-extension-docs/details)

##### 学习成果检验

独立做出一个微信小程序并实现后台功能

or

独立开发一个自己的博客



