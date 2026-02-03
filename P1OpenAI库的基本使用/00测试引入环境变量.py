import os
# 打印环境变量值（None表示未读取到）
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
# 打印所有环境变量（可搜索确认）
# print(dict(os.environ))