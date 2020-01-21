# ipnotify

Google Domains の API に IP 通知をするオレオレスクリプト

# 環境

- Python 3.6.4 で作った

# 設定

1. .config.sample を /etc/ipnotify/config に設置
1. .config にサンプルのように通知したいドメイン、API のユーザー名およびパスワードを入力
1. 実行

   ```
   $ python3 notify.py
   ```

1. 定期実行には cron なり systemd-timer を使う

# ライセンス

[MIT LICENSE](./LICENSE)
