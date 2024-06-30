# 数据预处理
import pandas as pd

data = pd.read_excel('result/US Presidential Election2000.xlsx')
data = data.dropna()

import jieba

# 去除 content 列的特殊字符和标点符号
data['content'] = data['content'].str.replace('[^\w\s]', '')

# 对 content 列进行分词处理
data['cut_content'] = data['content'].apply(lambda x: list(jieba.cut(x)))

# 统计总字数
data['content_length'] = data['content'].apply(len)

# 计算 content 列的总字数
total_characters = data['content_length'].sum()

print(f"content 列的总字数: {total_characters}")