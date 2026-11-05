# Health Clip

ネットで話題の「身体によいと言われるもの」を、発信元と販売・PRとの関係つきで集めたサイトです。

## フォルダ構成

| パス | 内容 |
|---|---|
| `src/feed.html` | 記事一覧ページの元データ。毎週の自動収集で更新します |
| `site/` | さくらのサーバーにアップロードするファイル一式 |
| `site/about.html` ほか | 運営者情報・免責事項・プライバシーポリシー（直接編集します） |
| `tools/build_index.py` | `src/feed.html` から `site/index.html` を作ります |
| `.github/workflows/deploy.yml` | main ブランチの更新時に、`site/` をさくらのサーバーへアップロードします |

## 初回の設定（1回だけ）

1. GitHub で非公開（Private）のリポジトリ `health-clip` を作り、このフォルダの中身をアップロードします。
2. リポジトリの Settings → Secrets and variables → Actions → New repository secret で、次の4つを登録します。

| 名前 | 値 | 例 |
|---|---|---|
| `FTP_SERVER` | さくらのFTPサーバ名 | `アカウント名.sakura.ne.jp` |
| `FTP_USERNAME` | FTPアカウント | さくらの初期ドメインのアカウント名 |
| `FTP_PASSWORD` | サーバパスワード | さくらのコントロールパネルで確認 |
| `FTP_SERVER_DIR` | アップロード先のフォルダ（末尾に / を付ける） | `www/` または `www/healthclip/` |

3. Actions タブ → Deploy to Sakura → Run workflow で、初回のアップロードを実行します。
4. ブラウザでサイトを開き、表示を確認します。

## 公開前に入力する項目

`site/about.html` と `site/privacy.html` の【要入力】の箇所（運営者名・所在地・メールアドレス・サイトURL・公開日・アクセス解析の有無）を書き換えます。

## 毎週の更新

毎週月曜日に自動収集が `src/feed.html` を更新して main ブランチに反映し、GitHub Actions がさくらのサーバーへアップロードします。
