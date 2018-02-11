# ipnotify
Google DomainsのAPIにIP通知をするオレオレスクリプト

# 環境
* Python 3.6.4で作った

# 設定
1. .config.sample を .config に変更
1. .config にサンプルのように通知したいドメイン、APIのユーザー名およびパスワードを入力
1. 実行

    ```
    $ python3 notify.py
    ```

1. 定期実行にはcronなりsystemd-timerを使う

# ライセンス
[MIT LICENSE](./LICENSE)
