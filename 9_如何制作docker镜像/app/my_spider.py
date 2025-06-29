import os  # 导入os模块，用于访问环境变量
import requests  # 导入requests库，用于发送HTTP请求
from bs4 import BeautifulSoup  # 从bs4库导入BeautifulSoup，用于解析HTML

# 从环境变量中获取目标URL，如果没有设置则使用默认值"https://www.baidu.com"
url = os.environ.get("TARGET_URL", "https://www.baidu.com")

# 发送GET请求获取网页内容
r = requests.get(url)

# 自动检测网页编码并设置，确保内容正确解码
r.encoding = r.apparent_encoding

# 使用BeautifulSoup解析网页内容，指定解析器为"html.parser"
soup = BeautifulSoup(r.text, "html.parser")

# 提取网页中的所有文本内容并打印输出
print(soup.get_text())