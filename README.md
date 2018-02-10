# ipnotify
Google DomainsのAPIにIP通知をするオレオレスクリプト

# 環境
* Python 3.6.4で作った

# 設定
1. settings.sample.yml を settings.yml に変更
2. settings.yml にサンプルのように通知したいドメイン、APIのユーザー名およびパスワードを入力
3. 依存関係インストール

    ```
    $ pip3 install -r requirements.txt
    ```
4. 実行

    ```
    $ python3 notify.py
    ```

5. 定期実行にはcronなりsystemd-timerを使う

# ライセンス
[MIT LICENSE](./LICENSE)
