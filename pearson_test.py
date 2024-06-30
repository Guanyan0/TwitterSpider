import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 读取情感分析数据和联邦基金有效利率
sentiment_data = pd.read_excel('result/scores_data.xlsx')  # 包含 'date' 和 'out_sentiment' 列
bond_data = pd.read_csv('result/联邦基金有效利率历史数据.csv')  # 包含 '日期' 和 '收盘' 列

# 将日期列转换为datetime类型
sentiment_data['date'] = sentiment_data['date'].str[:10]
sentiment_data['date'] = pd.to_datetime(sentiment_data['date'])
bond_data['日期'] = pd.to_datetime(bond_data['日期'])

# 重命名bond_data的日期列为'date'以便于合并
bond_data.rename(columns={'日期': 'date', '收盘': 'bond_yield'}, inplace=True)

# 合并两个数据集，按日期对齐
merged_data = pd.merge(sentiment_data, bond_data, on='date', how='inner')

# 计算滑动平均值
window_size = 120
merged_data['sentiment_rolling'] = merged_data['out_sentiment'].rolling(window=window_size).mean()
merged_data['bond_yield_rolling'] = merged_data['bond_yield'].rolling(window=window_size).mean()

# 删除NaN值
merged_data.dropna(inplace=True)

# 打印合并后的数据集长度和滑动平均值的非NaN数据点数量
print("Merged data length:", len(merged_data))
print("Non-NaN sentiment rolling mean count:", merged_data['sentiment_rolling'].count())
print("Non-NaN bond yield rolling mean count:", merged_data['bond_yield_rolling'].count())

# 确保有足够的数据点进行相关性分析
if len(merged_data) >= 2:
    # 计算皮尔逊相关系数并进行假设检验
    pearson_corr, p_value = stats.pearsonr(merged_data['sentiment_rolling'], merged_data['bond_yield_rolling'])
    print("Pearson Correlation Coefficient:", pearson_corr)
    print("P-value:", p_value)

    # 判断是否存在显著负相关性
    alpha = 0.05
    if p_value < alpha and pearson_corr < 0:
        print("存在显著负相关性")
    else:
        print("不存在显著负相关性")
else:
    print("Not enough data points for correlation analysis")
