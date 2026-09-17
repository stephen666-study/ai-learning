# 写TXT文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")

# 读TXT文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("文件内容:")
print(content)