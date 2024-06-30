import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
fond_data = pd.read_csv('result/联邦基金有效利率历史数据.csv')

# 将日期列设为索引
fond_data['日期'] = pd.to_datetime(fond_data['日期'])
fond_data = fond_data.set_index('日期').sort_index()

# 计算联邦基金有效利率的滑动平均值
bond_window_size = 120  # 滑动窗口大小
bond_rolling_average = fond_data['收盘'].rolling(window=bond_window_size).mean()

# 读取情感分析数据
sentiment_data = pd.read_excel('result/scores_data.xlsx')

# 将日期列设为索引
sentiment_data['date'] = pd.to_datetime(sentiment_data['date'])
sentiment_data = sentiment_data.set_index('date').sort_index()

# 计算情感分析数据的滑动平均值
sentiment_window_size = 120  # 滑动窗口大小
sentiment_rolling_average = sentiment_data['out_sentiment'].rolling(window=sentiment_window_size).mean()

# 创建两个坐标轴
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制联邦基金有效利率的滑动平均值
ax1.plot(bond_rolling_average.index, bond_rolling_average, label='US 10-Year Bond Yield (Rolling Average)', color='blue')
ax1.set_xlabel('Date')
ax1.set_ylabel('Bond Yield (Rolling Average)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.legend(loc='upper left')

# 创建第二个坐标轴
ax2 = ax1.twinx()

# 绘制情感分析数据的滑动平均值
ax2.plot(sentiment_rolling_average.index, sentiment_rolling_average, label='Sentiment Analysis (Rolling Average)', color='green')
ax2.set_ylabel('Sentiment Analysis (Rolling Average)', color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.legend(loc='upper right')

plt.title('Federal funds effective rate vs Sentiment Analysis - Rolling Average')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()