# Health Clip

ネットで話題の「身体によいと言われるもの」を、発信元と販売・PRとの関係つきで集めたサイトです。

## フォルダ構成

| パス | 内容 |
|---|---|
| `src/feed.html` | 記事一覧ページの元データ。毎週の自動収集で更新します |
| `site/` | さくらのサーバーにアップロードするファイル一式 |
| `site/about.html` ほか | 運営者情報・免責事項・プライバシーポリシー（直接編集します） |
| `tools/build_index.py` | `src/feed.html` から `site/index.html` を作ります |
| `tools/sakura-sync.sh` | さくらのサーバーで定期実行し、`site/` の最新版を公開フォルダに反映します |

## さくらのサーバーへの反映の仕組み

さくらのサーバーは海外からのFTP接続を制限しているため、GitHubから送るのではなく、さくらのサーバー側から定期的に最新版を取得します。

1. さくらのファイルマネージャーで `/home/think-i/healthclip-sync/` を作り、`tools/sakura-sync.sh` を置きます。
2. リポジトリが非公開の場合は、同じフォルダに読み取り専用のトークンを書いた `token` ファイルを置きます。
3. さくらのコントロールパネルの CRON で、`sh /home/think-i/healthclip-sync/sakura-sync.sh` を1時間ごとに実行します。
4. 反映の記録は `/home/think-i/healthclip-sync/sync.log` に残ります。

## 公開前に入力する項目

`site/about.html` と `site/privacy.html` の【要入力】の箇所（運営者名・所在地・メールアドレス・サイトURL・公開日・アクセス解析の有無）を書き換えます。

## 毎週の更新

毎週月曜日に自動収集が `src/feed.html` と `site/index.html` を更新して main ブランチに反映します。さくらのサーバーは、1時間以内に最新版を取得します。
