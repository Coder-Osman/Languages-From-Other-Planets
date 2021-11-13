from cnradical import Radical, RunOption
from pypinyin import lazy_pinyin
from random import randint
s = """是非曲直 难以论说
但史家无不注意到
正是在这个古战场上
决定了多少代王朝的
盛衰兴亡 此兴彼落
所以古来就有问鼎中原之说
当年 先总理领革命军
分三路汇合徐州
兴师北上
光复徐州的第二天
清帝见大势已去 宣告退位
民国十六年四月
也正是在徐州城郊
我有幸亲率数十万健儿
征讨北洋军阀孙传芳 张宗昌
大获全胜
我讲过 抗日战争快不得
解放战争拖不得
现在看来
这个话没有错
照一般规律
总兵力和装备不超过对方
决不可进入战略决战
也不尽然
解放战争两年多
我们滚大了 我们打精了
我们积累了有利决战的条件
好比凹凸镜
向着炎炎的烈日
百倍 千倍的光度
聚合到一点上
白热化了 冒烟了
不能不燃烧了
我不明白
为什么大家都在谈论着项羽被困垓下
仿佛这中原古战场
对于我们注定了凶多吉少
二十年前 我从徐州踏上征途
开始了第二次北伐
中华秋海棠叶遂归于一统
本党本军所到之处 民众竭诚欢迎
真可谓占尽天时
那种勃勃生机
万物竞发的境界 犹在眼前
短短二十年后
这里竟至于一变而为我的葬身之地了吗
所谓战略决战
简单说就是赌国家的命运
赌军队的命运
这个赌字啊 很不好听
可又找不出一个更恰切的字来代替它
就是这么一回事
啪地一下 押上去了
正是因为如此
事情临到了面前
又禁不住心扑扑地跳
哪有这个道理啊
心跳的什么呢
我们不怕燃烧 我们不怕白热化
我们不怕烫着这里 烫着那里
我们的手 不能发抖啊
无论怎么讲
会战兵力是八十万对六十万
优势在我"""
s2 = ""
dic = {}
dic2 = {}
r = Radical(RunOption.Radical)
p = Radical(RunOption.Pinyin)
for i in range(ord(u'\u4e00'),ord(u'\u9fa5')):
    i = chr(i)
    ri, pi, pi2 = r.trans_ch(i), p.trans_ch(i), lazy_pinyin(i)[0]
    if ri == "艹" :
        if pi in dic.keys():
            dic[pi].append(i)
        else:
            dic[pi] = [i]
        if pi2 in dic2.keys() :
            dic2[pi2].append(i)
        else :
            dic2[pi2] = [i]
for i in s :
    if p.trans_ch(i) and p.trans_ch(i) in dic.keys() :
        tmp = dic[p.trans_ch(i)]
        s2 += tmp[randint(0, len(tmp) - 1)]
    elif lazy_pinyin(i)[0] in dic2.keys() :
        tmp = dic2[lazy_pinyin(i)[0]]
        s2 += tmp[randint(0, len(tmp) - 1)]
    else :
        s2 += i
print(s2)