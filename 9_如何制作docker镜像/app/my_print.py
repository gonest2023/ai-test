import os  # 导入操作系统相关的模块，用于访问环境变量

# 从环境变量中获取 "TARGET_URL" 的值，如果没有设置该环境变量，则使用默认值 "https://www.baidu.com"
url = os.environ.get("TARGET_URL", "https://www.baidu.com")  # 默认值

# 打印获取到的 URL
print(url)