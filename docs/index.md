[TOC]



#DB组python学习技术路线 V1.1

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

> 柳真学长补充
>
> （1）pycharm:安装使用时，强烈建议安装专业版，好处是：有很多功能很好用，在社区免费版上未提供的。具体如何破解到网上找解决办法。
>
> 
> （2）git:首先，初学者自行到GitHub网站上注册一个个人账号。具体如何使用，学习一遍廖雪峰的Git教程。把里面的每个命令都上机实现一遍即可。网址链接（https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000）
>
> （3）markdown编写工具。此处建议，小组内项目合作，都可以把代码放到GitHub上，技术文档可以使用GitHub上的Wiki来存放，Wiki一般就是存放markdown格式的文档。比如db组python技术路线文档就可以放到Wiki上，到时只需要一个链接就可以在线看。
>
> 额外补充：
> 学会翻墙，作为一名程序员，首要任务要学会翻墙。一般的技术问题，首要考虑使用Google（PS：浏览器也建议使用谷歌浏览器）。翻墙有多种方式，能翻墙成功，且网络稳定就行。
> 推荐一款ShadowSocks翻墙工具。具体账号购买到网上搜索。其中ShadowSocks客户端下载到GitHub上搜索，不要使用其他搜索引擎。
>

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

> 柳真学长补充：
> （1）学习Flask框架，可以去尝试使用一下swagger工具。swagger可以根据接口文档自动生成编写接口代码，可以很快实现接口需求。缺点是稳定性可能不好，有可能出现bug, 不过对于一些小项目来说是绰绰有余。
> (2)打算学习python web方向，学会如何对后端项目配置nginx

> （3）除了Flask、Django框架外，还有高并发处理Tornado框架和底层自定义协议网络Twisted框架，有额外时间可以研究下

> （4）除了基本框架学习外，还要对数据存储方面的技术有所了解和研究。深入学习使用Redis数据库，最好能够阅读源码；学会使用rabbitmq,并能够在框架中结合使用；学会使用Celery，最好结合Redis进行使用，并整合到框架中进行使用，Celery最实用的一点就是定时任务相关功能实现。

> （5）作为数据库组成员，除了Redis键值对数据库外，还有学会设计关系型数据库，使用的话建议先上手mysql，然后再稍微研究一下Oracle。非关系型数据库，就研究一下MongoDB和Redis即可。

> （6）学习python，基础是要用好linux系统。初学者建议刚开始就从linux入门，不要图方便使用windows，有额外时间可以多研究一下linux系统相关命令，以及如何快捷高效部署后端代码。

> （7）python基础可以关注一下pythonic的写法，平常写代码要先思考，如何写的精简，代码也要学会怎样写较规范。

##### 学习成果检验

独立做出一个微信小程序并实现后台功能

or

独立开发一个自己的博客



