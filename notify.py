#!/usr/bin/python3

import re
import urllib.parse
import urllib.request
from configparser import ConfigParser


def load():
    """
    .config からIP通知のリストを取得する
    :return: ConfigParser object
    """
    config = ConfigParser()
    try:
        with open('/etc/ipnotify/config') as f:
            config.read_file(f)
    except IOError:
        raise Exception("failed to open config file")
    return config


def request(info):
    """
    Google DomainsのAPIに問い合わせ
    :param info: {domain: username: password:} のdict
    :return: 成功の可否
    """
    base_url = 'https://domains.google.com/nic/update'

    manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    manager.add_password(None, base_url, info['username'], info['password'])
    handler = urllib.request.HTTPBasicAuthHandler(manager)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

    params = urllib.parse.urlencode({"hostname": info["domain"]}).encode('UTF-8')
    response = urllib.request.urlopen(base_url, params)
    if response.status is not 200:
        print("Invalid Status Code", response.status)
        return False

    body = response.read().decode("utf-8")
    matched = re.match(r"^(good|nochg)\s.+$", body)

    if matched is None:
        print("Something went wrong!\n\tREASON: ", body)
        return False
    print("Notification succeeded! ", body)
    return True


def main():
    """
    メイン関数
    :return:
    """
    config = load()
    for sec in config.sections():
        username = config.get(sec, "username")
        password = config.get(sec, "password")
        if not username or not password:
            raise Exception("username or password is undefined")
        request({"domain": sec, "username": username, "password": password})


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print("An Error Occurred: ", error)
