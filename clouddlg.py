import pandas as pd
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# 读取 Excel 文件
df = pd.read_excel('copy.xlsx', header=0)
# 获取第五列评论数据
comments = df.iloc[:, 4].tolist()

# 对空值进行填充
comments = [str(comment) for comment in comments]
comments = pd.Series(comments).fillna("").tolist()
# 对数据中的 ## 和空格进行替换
comments = [re.sub(r"##|\s", "", comment) for comment in comments if comment.strip() != ""]
comments = [re.sub(r"[，。]|\s", "", comment) for comment in comments]

# 中文分词处理
words = []
for comment in comments:
    words += jieba.lcut(comment)

# 指定需要删除的词语列表
stopwords = ["的", "好", "很", "也", "有","会","已","挺","进","这个","一个","大",
             "这里","就","是","高","和","在","小","到","都","不","新","给","！","酒店"
             ,"去","我","了","#","人员","住","用户","一次","房间","就是","而且","特别",
             "我们","、","方面","来","人","非常","总体","出差","让","床","再","多","说","要","入住",
             "很多","没有","有点","下次","里","吧","能","还会","吃饭","装修","还","没","这","离","能"]
# 统计词语出现次数
word_counts = Counter(words)
# 删除指定的词语
for word in stopwords:
    if word in word_counts:
        del word_counts[word]

# 筛选出现次数最多的前 k 个词
k = 100
top_k_words = dict(word_counts.most_common(k))
print(top_k_words)
# 词云图生成
wc = WordCloud(width=800, height=600, font_path="仿宋_GB2312.ttf", background_color="white")
wc.generate_from_frequencies(top_k_words)

# 显示词云图
plt.imshow(wc)
plt.axis("off")
plt.show()