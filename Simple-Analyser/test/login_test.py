# user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
# cookie: _zap=d722f6c8-f398-46d3-a067-fcd73f3ec26b; d_c0="AOAoiwyQYQ-PTh7_3m5gDmLaPLfHbkv3aX8=|1557025359"; z_c0=Mi4xaHBzMERBQUFBQUFBNENpTERKQmhEeGNBQUFCaEFsVk5yYlkzWGdDV09HTy16VUJlSDdhTkNzaldGMFlLa0JxT19B|1565157549|d9c0b75d2225d475746a2b8bd4f9a315f3c1c0d2; _xsrf=05a97db3-f19a-4b57-956b-de7049c47778; tst=h; tshl=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569658639,1569660030; q_c1=a3c64227335f49c28188e499cbc24f35|1569660158000|1557025359000; tgw_l7_route=116a747939468d99065d12a386ab1c5f; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569663503


import requests

cookie='_zap=d722f6c8-f398-46d3-a067-fcd73f3ec26b; d_c0="AOAoiwyQYQ-PTh7_3m5gDmLaPLfHbkv3aX8=|1557025359"; z_c0=Mi4xaHBzMERBQUFBQUFBNENpTERKQmhEeGNBQUFCaEFsVk5yYlkzWGdDV09HTy16VUJlSDdhTkNzaldGMFlLa0JxT19B|1565157549|d9c0b75d2225d475746a2b8bd4f9a315f3c1c0d2; _xsrf=05a97db3-f19a-4b57-956b-de7049c47778; tst=h; tshl=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569658639,1569660030; q_c1=a3c64227335f49c28188e499cbc24f35|1569660158000|1557025359000; tgw_l7_route=116a747939468d99065d12a386ab1c5f; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569663503'


def cookie_to_dict(cookie):
    cookie_dict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        cookie_dict[key] = value
    return cookie_dict

# print(cookie_to_dict(cookie))

url = 'https://www.zhihu.com/hot'
r = requests.session()

headers={'cookie':cookie_to_dict(cookie),'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

kw={'headers':headers}

r.get(url,**kw)

print(r)