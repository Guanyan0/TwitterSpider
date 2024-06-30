import pandas as pd
import re
import ast  # 导入 ast 模块用于解析字符串表示的元组

# 假设这是你的 DataFrame 数据
data = pd.read_excel('result/scores_data.xlsx')
# data = {
#     'date': ['2024-05-01', '2024-05-02', '2024-05-03'],
#     'sentiment': [
#         [('r', 'Trump', 0.7269)],
#         [('r', 'Trump', 0.5106), ('d', 'Biden', 0.4588), ('d', 'dsfa', -0.1779)],
#         []  # 空数组示例
#     ]
# }
df = pd.DataFrame(data)

# 从xlsx读取时无法识别元组
df['sentiment'] = df['sentiment'].apply(ast.literal_eval)

# 定义提取和计算函数
def calculate_out_sentiment(sentiment_list):
    if not sentiment_list:
        return 0.0  # 如果列表为空，返回0.0

    r_values = [s[2] for s in sentiment_list if len(s) > 2 and s[0] == 'r']
    d_values = [s[2] for s in sentiment_list if len(s) > 2 and s[0] == 'd']

    if not r_values and not d_values:
        return 0.0  # 如果没有'r'或'd'的情感值，返回0.0

    total_sum = sum(d_values) - sum(r_values)
    total_count = len(r_values) + len(d_values)

    return total_sum if total_count != 0 else 0.0


# 计算每一行的out_sentiment
# out_sentiment越小，支持共和党和Trump的倾向就越大，越大则支持民主党和Biden的倾向就越大，越趋近于0则越中立
df['out_sentiment'] = df['sentiment'].apply(calculate_out_sentiment)

df.to_excel('result/scores_data.xlsx',index=False)