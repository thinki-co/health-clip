# Health Clip の補助ページ（運営者情報・免責事項・プライバシーポリシー）を生成する
import os
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")
TODO = lambda t: f'<span class="todo">【要入力：{t}】</span>'

CSS = """
:root { --bg:#F3F8FD; --surface:#FFFFFF; --line:#DCE7F3; --ink:#16324F; --muted:#4A6178; --blue:#2F6BFF; --lime:#B7F34D; --todo-bg:#FFF1C2; --todo-ink:#7A4B00;
  --grad:linear-gradient(120deg,#2F6BFF 0%,#49A8FF 55%,#36CFC9 100%);
  --f-display:"Plus Jakarta Sans","Zen Kaku Gothic New",system-ui,sans-serif; --f-body:"Zen Kaku Gothic New","Hiragino Sans","Yu Gothic",system-ui,sans-serif; }
@media (prefers-color-scheme: dark) { :root { --bg:#0E1A27; --surface:#15263A; --line:#24384F; --ink:#E8F0F8; --muted:#A5B8CB; --blue:#6E9BFF; --todo-bg:#3A3013; --todo-ink:#FFD98A; color-scheme: dark; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font-family:var(--f-body); font-size:15px; line-height:1.8; }
.wrap { max-width:720px; margin:0 auto; padding-left:max(16px,env(safe-area-inset-left,0px)); padding-right:max(16px,env(safe-area-inset-right,0px)); }
header { background:var(--surface); border-bottom:1px solid var(--line); }
header .wrap { padding-block:14px; }
.logo { display:inline-flex; align-items:center; gap:7px; font-family:var(--f-display); font-weight:800; font-size:22px; color:var(--ink); text-decoration:none; }
.logo b { width:20px; height:20px; border-radius:6px; background:var(--grad); position:relative; }
.logo b::after { content:""; position:absolute; right:-3px; top:-3px; width:8px; height:8px; border-radius:50%; background:var(--lime); border:2px solid var(--surface); }
main .wrap { padding-block:24px 40px; }
h1 { margin:0 0 6px; font-size:22px; font-weight:900; }
.updated { margin:0 0 20px; font-size:12.5px; color:var(--muted); }
h2 { margin:28px 0 8px; font-size:16px; font-weight:900; }
p, li { font-size:14.5px; }
ul, ol { padding-left:1.3em; display:grid; gap:4px; }
table { width:100%; border-collapse:collapse; background:var(--surface); border:1px solid var(--line); border-radius:12px; overflow:hidden; font-size:14px; }
th, td { text-align:left; vertical-align:top; padding:12px 14px; border-bottom:1px solid var(--line); }
th { width:32%; font-weight:700; color:var(--muted); background:var(--bg); }
tr:last-child th, tr:last-child td { border-bottom:0; }
.todo { background:var(--todo-bg); color:var(--todo-ink); font-weight:700; padding:1px 6px; border-radius:4px; }
table a, li a, p a { color:var(--blue); }
.back { display:inline-block; margin-top:28px; color:var(--blue); font-weight:700; text-decoration:none; }
footer { border-top:1px solid var(--line); background:var(--surface); }
footer .wrap { padding-block:18px 24px; display:grid; gap:8px; font-size:12.5px; color:var(--muted); }
footer nav { display:flex; flex-wrap:wrap; gap:6px 16px; }
footer a { color:var(--ink); text-decoration:none; font-weight:700; }
a:focus-visible { outline:3px solid var(--blue); outline-offset:2px; }
"""

FOOTER = """<footer><div class="wrap">
  <nav aria-label="サイト情報"><a href="./">記事一覧</a><a href="about.html">運営者情報・お問い合わせ</a><a href="disclaimer.html">免責事項</a><a href="privacy.html">プライバシーポリシー</a></nav>
  <small>© 2026 Health Clip</small>
</div></footer>"""

def page(fname, title, desc, body):
    html = f"""<!doctype html>
<html lang="ja">
<head>
<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-P9D6VCBJ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}｜Health Clip</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&display=swap">
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap"><a class="logo" href="./"><b aria-hidden="true"></b>Health Clip</a></div></header>
<main><div class="wrap">
<h1>{title}</h1>
<p class="updated">制定日：2026年11月5日</p>
{body}
<a class="back" href="./">← 記事一覧に戻る</a>
</div></main>
{FOOTER}
</body>
</html>
"""
    open(os.path.join(OUT, fname), "w").write(html)

page("about.html", "運営者情報・お問い合わせ", "Health Clipの運営者情報とお問い合わせ先を掲載しています。", f"""
<h2>運営者情報</h2>
<table>
<tr><th>サイト名</th><td>Health Clip（ヘルスクリップ）</td></tr>
<tr><th>サイトURL</th><td>https://healthclip.thinki.co.jp/</td></tr>
<tr><th>運営者</th><td>株式会社THINK i</td></tr>
<tr><th>所在地</th><td>東京都新宿区</td></tr>
<tr><th>お問い合わせ先</th><td>contact@thinki.co.jp</td></tr>
<tr><th>サイトの内容</th><td>ネットで話題の「身体によいと言われるもの」についての記事を収集し、発信元と販売・PRとの関係を添えて掲載しています。</td></tr>
</table>

<h2>お問い合わせ</h2>
<p>Health Clipへのご意見・掲載内容の誤りのご指摘・掲載記事の削除依頼は、上記のメールアドレスで受け付けます。</p>
<ul>
<li>件名に「Health Clipについて」と記載してください。</li>
<li>掲載記事に関するお問い合わせは、記事の見出しと元記事のURLを本文に記載してください。</li>
<li>記事の発信元から削除の依頼を受けた場合は、内容を確認したうえで、原則として掲載を取りやめます。</li>
<li>返信までに数日かかる場合があります。内容によっては返信を控える場合があります。</li>
<li>健康状態や治療についての個別のご相談には、お答えできません。体調に不安がある場合は、医療機関にご相談ください。</li>
</ul>
""")

page("disclaimer.html", "免責事項", "Health Clipの掲載内容に関する免責事項を掲載しています。", """
<h2>掲載内容の位置づけ</h2>
<ul>
<li>Health Clipは、ネット上で公開された健康情報の記事を収集・整理して紹介するサイトであり、医療機関ではありません。</li>
<li>掲載内容は情報提供を目的とし、医師などによる診断・治療・助言の代わりにはなりません。体調に不安がある場合や、治療中・服薬中の場合は、医療機関にご相談ください。</li>
<li>Health Clipは、掲載した記事の内容の正誤・効果を判定しません。見出しと概要は、発信元の記載を短くまとめたものです。</li>
</ul>

<h2>作成方法</h2>
<ul>
<li>記事の収集、見出し・概要・分類の作成は、生成AIを用いて行っています。</li>
<li>掲載内容は、医師などの専門家による監修を受けていません。</li>
<li>見出し・概要には、元記事の意図と異なる要約が含まれる可能性があります。内容は、必ず元記事でご確認ください。</li>
</ul>

<h2>販売・PRとの関係の表示</h2>
<ul>
<li>販売・PRとの関係は、記事・サイト上の記載から確認できた範囲でのみ表示しています。</li>
<li>「確認できず」の表示は、販売・PRとの関係がないことを示すものではありません。</li>
<li>Health Clipは、商品の購入ページへのリンクを掲載せず、アフィリエイトなどによる収益も得ていません。</li>
</ul>

<h2>情報の正確性</h2>
<ul>
<li>掲載内容は収集日時点のものです。元記事は、その後に更新・削除されている場合があります。</li>
<li>Health Clipは、掲載内容の正確性・完全性・最新性を保証しません。</li>
</ul>

<h2>リンク先の内容</h2>
<p>Health Clipからリンクしている外部サイトの内容は、各サイトの運営者が責任を持ちます。Health Clipは、リンク先の内容・商品・サービスについて責任を負いません。</p>

<h2>損害の免責</h2>
<p>Health Clipの掲載内容を利用したことで生じた損害について、運営者は責任を負いません。</p>

<h2>著作権</h2>
<ul>
<li>掲載している見出し・概要は、元記事を要約したものです。元記事の著作権は、各発信元に帰属します。</li>
<li>記事の発信元から掲載の取りやめを求められた場合は、内容を確認したうえで対応します。</li>
</ul>

<h2>免責事項の変更</h2>
<p>運営者は、必要に応じて本免責事項を変更します。変更後の内容は、本ページに掲載した時点から効力を持ちます。</p>
""")

page("privacy.html", "プライバシーポリシー", "Health Clipにおける個人情報と閲覧データの取り扱いを掲載しています。", f"""
<h2>取得する情報</h2>
<ul>
<li>Health Clipは、会員登録・ログインの機能を持たず、記事の閲覧にあたって氏名・メールアドレスなどの個人情報を取得しません。</li>
<li>お問い合わせを受けた場合に限り、メールアドレス・氏名（記載があった場合）・お問い合わせ内容を取得します。</li>
</ul>

<h2>利用目的</h2>
<p>お問い合わせで取得した情報は、お問い合わせへの回答と、掲載内容の修正・削除の対応にのみ利用します。</p>

<h2>第三者への提供</h2>
<p>運営者は、法令に基づく場合を除き、取得した個人情報を本人の同意なく第三者に提供しません。</p>

<h2>マイクリップ（★）の保存</h2>
<ul>
<li>★を付けた記事の情報は、閲覧者の端末のブラウザ内（ローカルストレージ）にのみ保存します。</li>
<li>保存した情報は、運営者のサーバーには送信されず、運営者は内容を取得しません。</li>
<li>ブラウザの履歴やサイトデータを削除すると、保存した★も削除されます。</li>
</ul>

<h2>外部サービスの利用</h2>
<ul>
<li>Health Clipは、文字の表示にGoogle Fonts（Google LLC）を利用しています。</li>
<li>Health Clipは、閲覧状況の把握とサイトの改善を目的に、Google アナリティクス（Google LLC）を利用しています。</li>
<li>Google アナリティクスは、Cookieを使って閲覧データを収集します。収集したデータに、氏名・メールアドレスなど個人を特定する情報は含みません。</li>
<li>Google アナリティクスでのデータの取り扱いは、<a href="https://policies.google.com/technologies/partner-sites?hl=ja" target="_blank" rel="noopener">Googleのポリシー</a>に従います。</li>
<li>Google アナリティクスによる収集は、ブラウザのCookieを無効にするか、<a href="https://tools.google.com/dlpage/gaoptout?hl=ja" target="_blank" rel="noopener">Google アナリティクス オプトアウト アドオン</a>を利用して停止できます。</li>
</ul>

<h2>外部送信される情報</h2>
<p>Health Clipのページを開いた際に、閲覧者の端末から次の外部サービスへ情報が送信されます。</p>
<table>
<tr><th>送信先</th><td>Google LLC（Google アナリティクス・Google タグ）</td></tr>
<tr><th>送信される情報</th><td>閲覧したページのURL・閲覧日時・スクロールの状況・外部サイトへのリンクのクリック・参照元のURL・端末とブラウザの種類・IPアドレス・Cookieの識別子</td></tr>
<tr><th>利用目的</th><td>閲覧状況の把握とサイトの改善</td></tr>
</table>
<table style="margin-top:10px">
<tr><th>送信先</th><td>Google LLC（Google Fonts）</td></tr>
<tr><th>送信される情報</th><td>IPアドレス・ブラウザの種類・閲覧したページのURL</td></tr>
<tr><th>利用目的</th><td>文字の表示</td></tr>
</table>
<p>★マイクリップと、テーマ・部位などの絞り込みの操作は、外部サービスに送信しません。</p>

<h2>個人情報の管理</h2>
<p>運営者は、取得した個人情報を適切に管理し、漏えい・滅失・毀損の防止に努めます。お問い合わせへの対応が終わった情報は、必要な期間を過ぎた時点で削除します。</p>

<h2>開示・訂正・削除の請求</h2>
<p>本人から個人情報の開示・訂正・利用停止・削除の請求を受けた場合は、本人であることを確認したうえで対応します。請求は、運営者情報のページに記載したお問い合わせ先で受け付けます。</p>

<h2>プライバシーポリシーの変更</h2>
<p>運営者は、必要に応じて本ポリシーを変更します。変更後の内容は、本ページに掲載した時点から効力を持ちます。</p>

<h2>お問い合わせ窓口</h2>
<p>運営者：株式会社THINK i<br>メールアドレス：contact@thinki.co.jp</p>
""")
print("ok")
