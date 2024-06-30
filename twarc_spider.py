import subprocess
from utils.into_xlsx import into_xlsx

# 设置查询参数
query = "US Presidential Election 2024"
start_date = "2024-02-01T00:00:00"
end_date = "2024-02-29T23:59:59"
output_file = "us_presidential_election_2024_february.json"

# 执行 twarc 命令来爬取数据
subprocess.run([
    "twarc2", "search",
    query,
    "--start-time", start_date,
    "--end-time", end_date,
    "--archive",
    output_file
])

# 得到us_presidential_election_2024_february.json

json_file = "result/us_presidential_election_2024_february.json"
xlsx_output_file = "result/US Presidential Election2000.xlsx"
into_xlsx(json_file, xlsx_output_file)


# Donald Trump
# president election Republican