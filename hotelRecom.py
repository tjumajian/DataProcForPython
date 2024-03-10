import pandas as pd
import numpy as np

# 读取Excel文件，指定sheet名称和要读取的列
df = pd.read_excel('copy.xlsx', header=0, usecols=[0, 1, 2, 3, 4])
# 数据处理
df['酒店评分'] = df['酒店评分'].replace(' ', np.nan)
df['酒店评分'] = df['酒店评分'].fillna(0)
df['酒店评分'] = df['酒店评分'].astype(float)
df['酒店价格'] = df['酒店价格'].replace(' ', np.nan)
df['酒店价格'] = df['酒店价格'].fillna(0)
df['酒店价格'] = df['酒店价格'].astype(int)

# 将酒店评论整体转化为小写字母，以便于后续的文本处理
df['酒店评论'] = df['酒店评论'].str.lower()

# 定义积极词列表
positive_words = ['好', '棒', '赞', '满意', '舒适', '值得', '喜欢', '推荐']

# 定义负面词列表
negative_words = ['差', '坏', '不满', '不舒适', '不值', '失望', '不喜欢', '不推荐']

# 基于积极词和负面词的出现统计每个酒店的得分
scores = {}
for idx, row in df.iterrows():
    name = row[0]
    comment = row[4]
    if isinstance(comment, str):
        score = 0
        for word in positive_words:
            score += comment.count(word)
        for word in negative_words:
            score -= comment.count(word)
        scores[name] = round(float(row[1]) + score, 1)

# 按照评分进行排序，选出前20名的酒店
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:20]

# 输出排行榜
print('排名 | 酒店名称 | 地点 | 价格 | 评分 | 得分')
print('-' * 40)
for i, (name, score) in enumerate(sorted_scores):
    loc = df.loc[df['酒店名称'] == name].iloc[0, 2]
    price = df.loc[df['酒店名称'] == name].iloc[0, 3]
    print('{0:<4} | {1:<8} | {2:<10} | {3:<6} | {4:<5} | {5:<5}'.format(i+1, name, loc, price, round(score, 1), round(score*price, 1)))
