from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import re

result=pd.read_excel('result/US Presidential Election2000.xlsx')['content']
filtered_text=[]
for text in result:

    text=re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\$\$,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    filtered_text.append(text)

df=pd.DataFrame(filtered_text,columns=['content'])
all_comments = ' '.join(df['content'].dropna())

# 生成词云对象
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments)

# 绘制词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 去除坐标轴
plt.title('Word Cloud of Comments')
plt.show()