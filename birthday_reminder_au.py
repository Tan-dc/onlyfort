import pandas as pd
from datetime import datetime
import requests
from zoneinfo import ZoneInfo
# 假设 csv 文件名为 data.csv，包含 "姓名" 和 "出生日期" 两列
# 出生日期格式假设为 YYYY-MM-DD
df = pd.read_csv("birthday_info.csv")
print(df)
# 获取今天的月-日
beijing_tz = ZoneInfo('Australia/Melbourne')
today = datetime.now(beijing_tz).strftime("%m-%d")

# today = "01-01"
print(datetime.now(beijing_tz).strftime("%m-%d"))
count = 0
print(datetime.now(beijing_tz))
for _, row in df.iterrows():
    try:
        # 将出生日期转为 datetime 对象
        birthday = datetime.strptime(row["出生日期"], "%Y-%m-%d")

        # 比较月-日
        if birthday.strftime("%m-%d") == today:
            requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/"+f"{row['姓名']} Happy Birthday! 明天{today}")
            print(f"{row['姓名']} happy birthday!")
            count+=1
    except Exception as e:
        print(f"跳过无效日期: {row['出生日期']}")
if count == 0:
    requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/"+f"{today}无人生日")
