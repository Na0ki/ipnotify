import requests
import yaml


def load():
    """
    settings.ymlからIP通知のリストを取得する
    :return: [{domain: username: password:}]
    """
    with open("./settings.yml", "r") as f:
        notify_list = yaml.load(f) | []
    return notify_list


def request(info):
    """
    Google DomainsのAPIに問い合わせ
    :param info: {domain: username: password:} のdict
    :return: 成功の可否
    """
    base_url = 'https://domains.google.com/nic/update'
    payload = {'hostname': info['domain']}
    auth = (info['username'], info['password'])
    response = requests.post(base_url, payload, auth=auth)
    return response.status_code == requests.codes.ok


def main():
    """
    メイン関数
    :return:
    """
    notify_list = load()
    for i in notify_list:
        if not i["username"] or not i["password"]:
            raise Exception("username or password is undefined")
        success = request(i)
        print(success)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print("An Error Occurred: ", error)
