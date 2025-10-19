import markdown

html模板 = """<!doctype html>
<html>
<head>
<meta charset='UTF-8'><meta name='viewport' content='width=device-width initial-scale=1'>
<title></title>
<link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@11.6.0/styles/atom-one-dark.min.css">
<script src="https://unpkg.com/@highlightjs/cdn-assets@11.6.0/highlight.min.js"></script>
<script src="https://unpkg.com/@highlightjs/cdn-assets@11.6.0/languages/go.min.js"></script>
</head>

<body>
{body}
</body>
<script>
  hljs.highlightAll();
</script>
</html>
"""
def markdown转换为html(内容):
    global html模板
    extensions = ['markdown.extensions.fenced_code']
    md = markdown.Markdown(extensions=extensions)
    html = md.convert(内容)
    html =  html模板.format(body=html)
    return html

# from pyefun import *
# 写到文件("1.html", markdown转换为html(读入文本("1.md")))