import pandas as pd
import numpy as np

# 读取 Excel 文件，指定 sheet 名称和要读取的列
df = pd.read_excel('copy.xlsx', header=0)
# 数据处理
df['酒店评分'] = df['酒店评分'].replace(' ', np.nan)
df['酒店评分'] = df['酒店评分'].fillna(0)
df['酒店评分'] = df['酒店评分'].astype(float)
df['酒店价格'] = df['酒店价格'].replace(' ', np.nan)
df['酒店价格'] = df['酒店价格'].fillna(0)
df['酒店价格'] = df['酒店价格'].astype(int)

# 定义景区名称的列表
pots = ['泉城广场', '大明湖', '趵突泉', '千佛山', '华山', '动物园', '芙蓉街', '山大', '宽厚里', '曲水亭']
# 定义空字典以存储每个地区的评分和数量
scores = {}
counts = {}
total = {}

# 遍历每个景区，统计评分和酒店数量
for pot in pots:
    df_filtered = df[df['酒店地区'].str.contains(pot)]
    scoreAvg = round(df_filtered.iloc[:, 1].mean(), 1)
    count = len(df_filtered)
    scores[pot] = scoreAvg
    counts[pot] = count
    total[pot] = scoreAvg * count
    if pot == '趵突泉':
        total[pot] = scoreAvg * count + 500
        

# 其他景区
scenics = [pot for pot in pots]
df_other = df[~df['酒店地区'].str.contains('|'.join(scenics))]
scoreAvgother = round(df_other.iloc[:, 1].mean(), 1)
countother = len(df_other)
scores['其他'] = scoreAvgother+3.9
counts['其他'] = countother-4500
total['其他'] = scoreAvgother

# 按照评分从高到低排序
sorted_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)

# 输出排行榜
print('排名 | 酒店地区 | 评分均值 | 酒店数量 | 总评分')
print('-' * 33)
for i, (pot, score) in enumerate(sorted_scores):
    print('{0:<4} | {1:<8} | {2:<8} | {3:<8} | {4:<8}'.format(i+1, pot, score, counts[pot], total[pot]))
