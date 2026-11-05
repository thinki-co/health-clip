#!/bin/sh
# Health Clip：GitHub の site/ を、さくらのサーバーの ~/www/healthclip/ に反映する。
# さくらのコントロールパネルの CRON から定期実行する。
# 新しい更新がない場合は、何もせずに終了する。
set -eu

BASE="/home/think-i"
DIR="$BASE/www/healthclip-sync"      # このスクリプトと記録ファイルを置くフォルダ（.htaccess で外部からの閲覧を禁止）
DEST="$BASE/www/healthclip"          # 公開フォルダ
REPO="thinki-co/health-clip"
API="https://api.github.com/repos/$REPO"

# リポジトリを非公開に戻した場合のみ、読み取り専用のトークンを token ファイルに置く
AUTH=""
if [ -s "$DIR/token" ]; then
  AUTH="Authorization: Bearer $(cat "$DIR/token")"
fi

get() {
  if [ -n "$AUTH" ]; then curl -fsSL -H "$AUTH" "$@"; else curl -fsSL "$@"; fi
}

SHA=$(get -H "Accept: application/vnd.github.sha" "$API/commits/main")
if [ -f "$DIR/last_sha" ] && [ "$(cat "$DIR/last_sha")" = "$SHA" ]; then
  exit 0
fi

TMP="$DIR/tmp"
rm -rf "$TMP"
mkdir -p "$TMP"
get "$API/tarball/$SHA" -o "$TMP/repo.tgz"
tar -xzf "$TMP/repo.tgz" -C "$TMP"
SRC=$(find "$TMP" -maxdepth 2 -type d -name site | head -n 1)
if [ ! -f "$SRC/index.html" ]; then
  echo "site/index.html が見つからないため、反映を中止しました" >&2
  exit 1
fi

mkdir -p "$DEST"
cp -Rp "$SRC/." "$DEST/"
echo "$SHA" > "$DIR/last_sha"
rm -rf "$TMP"
echo "$(date '+%Y-%m-%d %H:%M') 反映しました：$SHA" >> "$DIR/sync.log"
