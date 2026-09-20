import os
import time
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def analyze(comment):
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个情感分析助手，只回答'正面'或'负面'。"},
            {"role": "user", "content": comment}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"]

df = pd.read_csv("comments.csv")

results = []
for comment in df["评论"]:
    sentiment = analyze(comment)
    results.append(sentiment)
    time.sleep(1)  # 每条之间停1秒，防止请求太快

df["情感"] = results
df.to_csv("评论分析结果.csv", index=False)
print("已保存 评论分析结果.csv")
print(df)
print("这是我修改后的代码")