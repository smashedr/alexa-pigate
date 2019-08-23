import requests


def open_gate(access_key):
    url = 'https://entry.luac.es:1313/door/open/'
    data = {'accessKey': access_key}
    r = requests.post(url, data=data, timeout=10)
    if not r.ok:
        r.raise_for_status()
