from . import new_spider
import random
from  flask import jsonify
from .service import getNews
from .. import *
@new_spider.route('/',methods=['GET'])
def xxx():
    data=getNews()
    if data:
        return jsonify(make_success(data=data))
    else:

        return jsonify(make_error(data=None))
@new_spider.route('/get',methods=['GET'])
def abc():
    x=random.randint(0,3)
    data=[""""2017武汉欢乐谷夜场攻略

皇家转马
　　欧式双层皇家旋马精致高贵，在欢快清扬的音乐声中，无数梦幻般的灯光投在脸上,登上五彩的骏马,在童话世界里驰骋!

异度空间
　　阴森、恐怖又奇特的空间内隐藏着千年古尸、狼面人、双角饿狼和各种鬼魂……无论你害怕与否,都能在惊声尖叫中感受挑战的快乐！

Disco
　　一个大圆盘顺着弧形的轨道摇摆起来,带领人们一起跳起了经典又欢快的DISCO！圆盘随着音乐旋转并来回滑荡,大家载歌载舞,好不开心！

飓风飞椅
　　飓风来临,椅子也随着飓风旋转起来了,坐上飞椅感受征服飓风的快感！飓风咆啸的声音都被欢声笑语取代！

能量风暴
　　外型酷似八爪鱼的“能量风暴”,能在急速的旋转带动能量的爆发,难以置信的速度和双重的旋转将为您带来一段无与伦比的记忆！

尖峰时刻
　　小蚂蚁们搭起了一座的天梯,好高！不要害怕,天梯上的座椅会带着你一飞冲天,再回到地面,一起一落间上下飞舞!

桑巴气球
　　大大的气球带来桑巴舞一样的热情旋转,还能在半空中饱览卡通工厂的风光,想在空中热情舞动么？还不快来！

炫舞转杯
　　一个个的大杯子组合在一起,魔法让它们滴溜溜地转了起来,坐在杯子里,你也能跳出浪漫的圆舞曲！

小鬼当家
　　专属于小朋友和轻量级“鬼”迷的欢乐鬼屋，蓝妹妹、葫芦娃这些“安全无公害”的卡哇伊小鬼会让人忍不住合影留恋，连孩子们也愿意和他们嬉戏、玩耍。

魔术自行车
　　魔术自行车可不一般,骑着它,能让你飞腾起来！俯视卡通工厂在脚下旋转,是不是别有一番风味呢？

乐乐跳
　　坐进小小赛车中,开始神奇的"跳跳"赛车之旅吧！这里的赛车不但飞速旋转着,还上下跳动,能让你玩得不亦乐乎！

星球大战
　　全民参与的星球大战开始了,紧握手中的“弹射弹”,互相瞄准发射软软的泡泡“炸弹”,看准目标才能成为百发百中的神射手。

　　海马骑士超奇妙微型失重跳楼机
　　伴随着优美的音乐坐上可爱海马，他们上下跳动，忽高忽低，彷佛和海马一起翱翔大海，带来些许失重和眩晕感。

　　极速穿越华中首个5D过山车
　　极速穿越奇幻冒险，你就是主角！急转摆动，颠簸跌宕，感受穿梭坠落的快感，赶快来挑战！

　　奇趣飞鱼无敌空中模拟激战飞车
　　坐在小飞鱼背上旋转、飞跃，在欢乐海洋的上空飞翔，在变速转动、高低起伏中体验梦幻翱翔的乐趣。

　　冲浪勇士站立式“W”型轨道撞浪体验
　　在“W”型轨道上360°旋转运行，海风浪花迎面扑来。不去海边，也能一同感受冲浪的刺激与欢畅！

　　水上飞机华中首创双环式贴水飞行器
　　水上飞机踏浪而来，时而在天上飞舞，时而从水面掠过，溅起欢快的水花，在不断地俯冲、旋转中体验飞行的畅快！

　　音乐飞船超刺激旋转式空中飞船
　　伴随着音乐，座舱缓缓旋转，紧接着一波接一波的翻滚，瞬间提升、跌落、停止、翻滚，和爸爸妈妈一起玩转心跳！
　　除此之外，还有异灵归来、霹雳战车、4D影院、魔法大草帽、丛林迷旋、天地双雄、飞越长江7大游乐设施，让你玩到过瘾。还在等什么，赶快加入欢乐谷游玩大军，肆意玩耍吧！""",""""推荐线路一：合家欢游玩线。
　　亚马逊懒人河——玛雅水寨——酷爽SPA——合家欢滑道——小喇叭——玛雅海滩。此线路包含的游乐项目适合儿童、中老年人及全家人一起游玩。""","""推荐线路二：甜蜜爱侣线。
　　玛雅海滩——大章鱼赛道——超级大喇叭——巨兽碗——酷爽SPA——亚马逊懒人河。连线路都是个爱心型的哦!此路线刺激程度适中，适合温馨浪漫的情侣一起游玩。""",""""推荐线路三：勇敢者的乐园。
　　大回环——垂直滑道——超级龙卷风——旋风巨浪——大黄蜂——四驱迷城。此线路专为勇敢者打造，喜欢挑战的青年游客可以在此尽享水上项目的劲爽刺激。"""]
    if x==0:
        return jsonify(data=data[0])
    if x==1:
        return jsonify(data=data[1])
    if x==2:
        return jsonify(data=data[2])
    if x==3:
        return jsonify(data=data[3])
