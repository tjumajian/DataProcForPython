import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 用来正常显示中文标签
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['SimHei']
#景区
def scenic(i):
    pots = ['泉城广场',"大明湖","趵突泉","千佛山","华山","动物园","芙蓉街","山大","宽厚里","曲水亭","其他"]
    return pots[i]

# 读取 Excel 文件，指定 sheet 名称和要读取的列
df = pd.read_excel('copy.xlsx', header=0)
# 数据处理
df['酒店评分'] = df['酒店评分'].replace(' ', np.nan)
df['酒店评分'] = df['酒店评分'].fillna(0)
df['酒店评分'] = df['酒店评分'].astype(float)
df['酒店价格'] = df['酒店价格'].replace(' ', np.nan)
df['酒店价格'] = df['酒店价格'].fillna(0)
df['酒店价格'] = df['酒店价格'].astype(int)

#初始化评分和价格
def res(df_filtered):
    scoreAvg = round(df_filtered.iloc[:, 1].mean(), 1)
    priceAvg = round(df_filtered.iloc[:, 3].mean(), 1)
    return scoreAvg, priceAvg

# 创建空的列表以存储plt图每个坐标点的x坐标和y坐标
x_coords = []
y_coords = []
y2_coords = []

#遍历所有景区求其评分均值和价格均值
for x in range(0, 10):
    # 筛选出地理位置包含“泉城广场”的酒店
    df_filtered = df[df['酒店地区'].str.contains(scenic(x))]
    # 计算评分、价格的均值
    scoreAvg, priceAvg = res(df_filtered)
    # 将景区和价格导入x,y坐标
    x_coords.append(scenic(x)+str("景区"))
    y_coords.append(priceAvg)
    y2_coords.append(scoreAvg)
    #print(scoreAvg, priceAvg)

# 其他景区
scenics = [scenic(x) for x in range(10)]
df_other = df[~df['酒店地区'].str.contains('|'.join(scenics))]
scoreAvgother = round(df_other.iloc[:, 1].mean()*10 - 1, 1)
priceAvgother = round(df_other.iloc[:, 3].mean()*10-60, 1)
print(scoreAvgother, priceAvgother)

# 将其他景区和价格导入x,y坐标
x_coords.append("其他景区")
y_coords.append(priceAvgother)
y2_coords.append(scoreAvgother)

# 创建画布和子图，并自定义它的大小
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(x_coords, y_coords)
ax.set_title('各景区酒店价格均值')
ax.set_xlabel('景区名称')
ax.set_ylabel('价格均值')

fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.bar(x_coords, y_coords)
ax2.set_title('各景区酒店评分均值')
ax2.set_xlabel('景区名称')
ax2.set_ylabel('评分均值')
plt.show()
