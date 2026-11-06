"""src/feed.html（Claude上の公開ページと同じ形式）から、サーバー用の site/index.html を作る。"""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(os.path.join(root, "src", "feed.html"), encoding="utf-8").read()
# 公開ページの雛形（<html><head>…<body>）付きで保存された場合は、本文部分だけを使う
if "<body>" in s:
    s = s.split("<body>", 1)[1].rsplit("</body>", 1)[0]
# Claude上でしか開けない詳細記事へのリンクを外す
s = re.sub(r'\n\s*\$\{it\.topic \? `<a class="btn sub" href="\$\{BETA\}#topic-\$\{it\.topic\}"[^\n]*', "", s)
s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
t_end = s.index("</title>") + len("</title>")
st_end = s.index("</style>") + len("</style>")
meta = """
<meta name="description" content="ネットで話題の「身体によいと言われるもの」と、健康診断や検査の数値・基準値に関する情報を、発信元と販売・PRとの関係つきで集めたサイトです。">
<meta property="og:title" content="Health Clip ヘルスクリップ">
<meta property="og:description" content="気になる健康情報を、まとめてチェック。">
<meta property="og:type" content="website">
<meta property="og:url" content="https://healthclip.thinki.co.jp/">
<link rel="canonical" href="https://healthclip.thinki.co.jp/">
<meta name="theme-color" content="#2F6BFF">"""
GTAG = '<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-P9D6VCBJ"></script>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag(\'js\', new Date());\n</script>\n'
html = ("<!doctype html>\n<html lang=\"ja\">\n<head>\n" + GTAG + "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
        "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
        "body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>\n"
        + s[:t_end] + meta + s[t_end:st_end] + "\n</head>\n<body>" + s[st_end:] + "\n</body>\n</html>\n")
os.makedirs(os.path.join(root, "site"), exist_ok=True)
open(os.path.join(root, "site", "index.html"), "w", encoding="utf-8").write(html)
n = len(re.findall(r'"?url"?: "', s))
print(f"site/index.html を作成しました（記事 {n} 件）")
