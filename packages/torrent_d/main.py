url="https://1337xto.to/"

import requests
proxies = {'http': 'socks5://user:pass@host:port',
           'https': 'socks5://user:pass@host:port'}

resp = requests.get('http://example.com', proxies=proxies )