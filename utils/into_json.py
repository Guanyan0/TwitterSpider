import pandas as pd

def into_json(xlsx_file,output_json_file_url):
    # 读取 Excel 文件
    # xlsx_file = "../result/US Presidential Election2000.xlsx"  # 替换为实际的 Excel 文件路径
    df = pd.read_excel(xlsx_file)

    # 将 DataFrame 转换为 JSON
    json_output = df.to_json(orient="records")

    # 将 JSON 数据保存到文件
    # output_json_file = "../result/us_presidential_election_2024_february.json"  # 替换为输出 JSON 文件路径
    with open(output_json_file_url, "w") as json_file:
        json_file.write(json_output)

    print("Excel 转换为 JSON 完成！")

