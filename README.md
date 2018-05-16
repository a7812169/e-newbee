# e-newbee
# 部署

### 1 下载源码

``mkdir test``创造文件夹test

`cd test`进入文件夹

```git clone https://github.com/a7812169/e-newbee.git```

### 2 在Ubuntu上安装python3

``apt-get install python3``

### 3 安装虚拟环境

``pip install virtualenv``

`cd test/e-newbee`

`virtualenv venv`

### 4 使用虚拟环境

`source ./venv/bin/activate`

### 5 安装依赖

`pip install -r requirements.txt`

### 6 启动程序

`python3 run.py`

这里python3是因为我自己的命令是python3 其他人可能不一样

# 接口文档

## 获取新闻/news

获取几条新闻的咨询

## 请求方式

GET

## 请求参数

无

## 响应参数

| 参数      | 类型     | 说明   |
| ------- | ------ | ---- |
| id      | int    | 自增主键 |
| author  | string | 作者姓名 |
| content | string | 文章内容 |
| href    | string | 超链接  |
| time    | string | 发布时间 |
| title   | string | 标题   |
## 示例

```

```

    "code": 1,
    "data": [
        {
            "author": "作者: 孙贵龙\r",
            "content": "5月10日-13日，由国家体育总局社会体育指导中心、中国大学生体育协会和中国中学生体育协会联合主办，广东省惠州市承办的2018年全国跳绳锦标赛在北京师范大学举行。我校跳绳队在本次比赛中荣获6金3银1铜。\n图略\n比赛现场。体育学院供图\n我校跳绳队由13名来自体育学院的学生组成，他们参加了本次比赛10个项目的角逐。在比赛中，同学们良好发挥，荣获车轮跳男子组、女子组、混合组冠军，三人交互绳男子组、女子组冠军，四人交互绳冠军，以及三人交互绳女子组第二名、四人交互绳混合组第二名，单人男子组第二名、单人女子组第三名。此外，我校跳绳队因技能精湛、作风优良，还荣获“体育道德风尚奖”，主教练孙贵龙老师被授予“全国优秀教练员”荣誉称号。\n全国跳绳锦标赛是我国跳绳运动最高级别的赛事，本次共有61支队伍700多余名运动员参赛。\n(编辑：刘虹 来源：党委宣传部）\n",
            "href": "http://www.scuec.edu.cn/s/329/t/1619/fe/72/info130674.htm",
            "time": "发布时间: 2018-05-16\r",
            "title": "[图]我校跳绳队在全国跳绳锦标赛上勇夺6金"
        },
        {
            "author": "作者: 谭艳平\r",
            "content": "5月9日上午，武陵山区特色资源植物种质保护与利用湖北省重点实验室第二届学术委员会第一次会议在我校学术交流中心召开。新一届重点实验室学术委员会主任、中国农业科学院副院长王汉中研究员，副主任、华中农业大学张端品与谢从华教授，武汉大学何光存教授、中国科学院陈凡研究员等委员，我校副校长杜冬云，科发院、生科学院等单位负责人及重点实验室全体成员参加了会议。会议由科发院副院长耿新主持。\n杜冬云致欢迎辞。他介绍了重点实验室设立的意义、运行状况以及近年来所取得的成绩等，感谢各位专家的帮助与支持，相信在新一届学术委员会的指导下，实验室会取得更丰硕的成果。\n实验室主任刘学群教授从实验室研究方向、实验基地建设、人才队伍建设、科研成果产出等方面全面汇报了重点实验室五年来的建设及运行基本情况以及今后五年的总体规划。实验室各研究方向负责人王春台、宋发军、覃瑞、刘庆华等教授先后汇报了过去五年以及未来五年的具体工作和计划。\n学术委员会审议了实验室的前期工作报告以及今后的五年规划、实验室开放课题审批和结项等议题。\n王汉中院士代表学术委员会指出，重点实验室已经取得了长足发展，今后五年要继续凝炼科研方向，加大经费投入，优化内部整合，加强平台建设，树立“链式创新”的战略意识，更加突出武陵山区“三位合一”的区域特色，推出更多具有特色的标志性科研成果。其他各位委员结合实验室发展状况，从凝炼研究方向、突出特色发展，培育标志性成果、精准结合国家战略等方面提出了众多建设性意见和建议。\n（编辑：刘虹 来源:生科学院）\n\n",
            "href": "http://www.scuec.edu.cn/s/329/t/1619/fe/5f/info130655.htm",
            "time": "发布时间: 2018-05-15\r",
            "title": "武陵山区特色资源植物种质保护与利用湖北省重..."
        }
    ],
    "msg": "请求成功"}
## 获取qa信息/qa/<int:tag>

根据发送过来的tag的值来判断返回的qa

## 请求方式

GET

## 请求参数

| 参数   | 类型   | 说明     |
| ---- | ---- | ------ |
| tag  | int  | 不同类别的值 |



## 响应参数

| 参数       | 类型     | 说明   |
| -------- | ------ | ---- |
| answer   | string | 回答   |
| id       | int    | 编号   |
| question | string | 问题   |

## 示例

    {"code": 1,
    "data": [
        {
            "answer": "asdsad",
            "id": 1,
            "question": "asdasdasd"
        },
        {
            "answer": "sd",
            "id": 2,
            "question": "a"
        },
        {
            "answer": "sdasd",
            "id": 3,
            "question": "sd"
        },
        {
            "answer": "0",
            "id": 4,
            "question": "萨沙是"
        },
        {
            "answer": "0",
            "id": 5,
            "question": "飒飒父亲为"
        },
        {
            "answer": "0",
            "id": 6,
            "question": "撒大苏打请问"
        }
    ],
    "msg": "请求成功"}
## 搜索qa信息/qa/search

根据表单的值 搜索qa信息

## 请求方式

POST

application/json

## 请求参数

| 参数       | 类型     | 说明   |
| -------- | ------ | ---- |
| question | string | 问题   |

## 响应参数

| 参数       | 类型     | 说明   |
| -------- | ------ | ---- |
| answer   | string | 回答   |
| id       | int    | 编号   |
| question | string | 问题   |

## 示例

    {"code": 1,
    "data": [
        {
            "answer": "asdsad",
            "id": 1,
            "question": "asdasdasd"
        },
        {
            "answer": "sd",
            "id": 2,
            "question": "a"
        }
    ],
    "msg": "请求成功"}
## 获取周边信息/funs/<int:tag>

根据发送过来的tag的值来判断返回的周边信息

## 请求方式

GET

## 请求参数

| 参数   | 类型   | 说明     |
| ---- | ---- | ------ |
| tag  | int  | 不同类别的值 |



## 响应参数

| 参数          | 类型     | 说明      |
| ----------- | ------ | ------- |
| content     | string | 文件地址    |
| title       | string | 文章标题    |
| url_address | string | 图片的存储地址 |

## 示例

```
{
    "code": 1,
    "data": [
        {
            "content": "C:\\Users\\DE",
            "title": "未命名文件",
            "url_address": "asd"
        },
        {
            "content": "C:\\Users\\DELL\\Desktop\\民大e新生\\app\\control\\9213b07eca806538cebb0d559ddda144.jpg",
            "title": "sadsadsadasd",
            "url_address": "asdsad"
        },
        {
            "content": "/root/test/e-newbee/app/control/timg.jpg",
            "title": "asdsadas",
            "url_address": "asdasd"
        }
    ],
    "msg": "请求成功"
}
```

## 搜索周边信息/funs/search

根据表单的值 搜索周边信息

## 请求方式

POST

application/json

## 请求参数

| 参数    | 类型     | 说明   |
| ----- | ------ | ---- |
| title | string | 标题   |

## 响应参数

| 参数          | 类型     | 说明    |
| ----------- | ------ | ----- |
| title       | string | 标题    |
| content     | string | 内容    |
| url_address | string | 图片的地址 |

## 示例

```
 {
    "code": 1,
    "data": [
        {
            "content": "qwe",
            "title": "0qwe",
            "url_address": "123wq"
        },
        {
            "content": "qwe",
            "title": "0qwe",
            "url_address": "qwe"
        },
        {
            "content": "qwe",
            "title": "0qwe",
            "url_address": "qwe"
        }
    ],
    "msg": "请求成功"
}
```

