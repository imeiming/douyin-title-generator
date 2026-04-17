#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

# 床盖卖点数据
FUNCTIONALITY = ["铺床+盖毯+沙发垫+野餐布四合一", "一物多用超省钱", "四季通用多功能", "从卧室到客厅再到户外都能用"]
QUALITY = ["垂感绝了酒店风", "高级感拉满", "质感堪比五星级酒店", "显贵又显高级"]
PROTECTION = ["防尘防污保护床垫", "告别清洁烦恼", "床垫守护神", "脏了也不心疼"]
FAMILY_FRIENDLY = ["有娃家庭必备", "养宠家庭福音", "租房党首选", "小户型救星"]
EASY_CARE = ["机洗不变形不缩水", "洗完干得超快", "随便造随便洗", "懒人友好易打理"]

# 情感触发词
EMOTION_WORDS = ["震惊", "绝了", "后悔没早买", "太香了", "闭眼入", "救命", "绝绝子", "YYDS", "神仙单品"]
URGENCY_PHRASES = ["限时优惠", "手慢无", "库存告急", "最后100件", "错过等一年", "今天下单立减", "抢到就是赚到"]
SOCIAL_PROOF = ["10W+宝妈推荐", "爆卖20W+件", "网红同款", "博主都在用", "全网断货王", "小红书爆款", "抖音热销榜第一"]

# Emoji
EMOJIS = ["🛏️", "✨", "🔥", "💯", "🌟", "👏", "😍", "🛒", "🎉", "🏆", "💎", "⚡"]

# 话题标签
HASHTAGS = ["#家居好物", "#租房必备", "#带娃神器", "#养宠必备", "#小户型改造", "#懒人福音", "#高颜值好物", "#生活必备"]

def generate_title():
    # 随机选择卖点组合
    functionality = random.choice(FUNCTIONALITY)
    quality = random.choice(QUALITY)
    protection = random.choice(PROTECTION)
    family_friendly = random.choice(FAMILY_FRIENDLY)
    easy_care = random.choice(EASY_CARE)
    
    # 随机选择情感词、紧迫感话术、社交证明
    emotion = random.choice(EMOTION_WORDS)
    urgency = random.choice(URGENCY_PHRASES)
    social_proof = random.choice(SOCIAL_PROOF)
    
    # 随机选择emoji和话题标签
    emoji1 = random.choice(EMOJIS)
    emoji2 = random.choice(EMOJIS)
    while emoji2 == emoji1:
        emoji2 = random.choice(EMOJIS)
    
    hashtags = " ".join(random.sample(HASHTAGS, 3))
    
    # 构建标题模板
    templates = [
        f"{emotion}！{functionality}+{quality}，{social_proof}🔥{urgency}！{emoji1}{emoji2} {hashtags}",
        f"后悔没早买！{family_friendly}的{protection}神器，{easy_care}还{quality}✨{social_proof}，{urgency}！{emoji1}{emoji2} {hashtags}",
        f"闭眼入！{functionality}的床盖绝了，{quality}+{protection}+{easy_care}，{social_proof}💯{urgency}！{emoji1}{emoji2} {hashtags}",
        f"救命！这个{family_friendly}的床盖也太香了吧！{functionality}，{quality}质感，{social_proof}🌟{urgency}！{emoji1}{emoji2} {hashtags}",
        f"绝绝子！{quality}床盖，{functionality}超实用，{protection}还{easy_care}，{social_proof}🔥{urgency}！{emoji1}{emoji2} {hashtags}"
    ]
    
    title = random.choice(templates)
    
    # 确保标题长度超过40字
    while len(title) < 40:
        extra_emoji = random.choice(EMOJIS)
        title += extra_emoji
    
    return title

def main():
    titles = []
    for i in range(10):
        title = generate_title()
        # 确保每个标题都超过40字
        while len(title) < 40:
            title += random.choice(EMOJIS)
        titles.append(f"{i+1}. {title}")
    
    for title in titles:
        print(title)
        print()

if __name__ == "__main__":
    main()