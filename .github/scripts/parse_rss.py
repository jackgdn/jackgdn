import feedparser
from datetime import datetime

# 配置
RSS_URL = "https://jackgdn.github.io/index.xml"
MAX_POSTS = 5
OUTPUT_FILE = "README.md"

# 解析 RSS
feed = feedparser.parse(RSS_URL)
posts = feed.entries[:MAX_POSTS]

# 生成 Markdown 内容
markdown_content = "## 📝 最新博客文章\n\n"
for post in posts:
    date = datetime.strptime(post.published, "%a, %d %b %Y %H:%M:%S %Z").strftime("%Y-%m-%d")
    markdown_content += f"- [{post.title}]({post.link}) - {date}\n"

# 更新 README.md
with open(OUTPUT_FILE, "r") as f:
    readme = f.read()

# 替换 <!-- BLOG-POSTS:START --> 和 <!-- BLOG-POSTS:END --> 之间的内容
updated_readme = readme.split("<!-- BLOG-POSTS:START -->")[0] + \
                 "<!-- BLOG-POSTS:START -->\n" + markdown_content + \
                 "<!-- BLOG-POSTS:END -->" + \
                 readme.split("<!-- BLOG-POSTS:END -->")[1]

with open(OUTPUT_FILE, "w") as f:
    f.write(updated_readme)
