import pandas as pd

def into_xlsx(json_file,xlsx_output_file):
    # 读取 JSON 文件
    # json_file = "../result/us_presidential_election_2024_february.json"  # 替换为实际的 JSON 文件路径
    with open(json_file, "r") as f:
        json_data = f.read()

    # 将 JSON 数据加载到 DataFrame
    df = pd.read_json(json_data)

    # 将 DataFrame 写入 Excel 文件
    # xlsx_output_file = "../result/US Presidential Election2000.xlsx"  # 替换为输出 Excel 文件路径
    df.to_excel(xlsx_output_file, index=False)

    print("JSON 转换为 Excel 完成！")
