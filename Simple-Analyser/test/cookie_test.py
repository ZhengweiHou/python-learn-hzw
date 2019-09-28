import requests
import http.cookiejar as cj

class Cookie_Util():
    @staticmethod
    def cookie_test():
        url = 'https://www.zhihu.com/hot'
        r = requests.session()
        r.cookies = cj.LWPCookieJar()  # 接入容器
        r.get(url)  # 不过需要注意，就算使用了会话，方法级别的参数也不会被跨请求保持,此cookie只发送给该请求
        print(r)
        r.post(url)
        # 请求x N
        r.cookies.save(filename='cookies_hzw.txt', ignore_discard=True, ignore_expires=True)  # 保存cookie到本地，忽略关闭浏览器丢失，忽略失效
        r.close()  # 对话支持with打开以实现自动close

    @staticmethod
    def cookie_local():
        url = 'https://www.zhihu.com/hot'
        r = requests.session()
        r.cookies = cj.LWPCookieJar(filename='cookies_hzw.txt')
        r.cookies.load(filename='cookies_hzw.txt', ignore_discard=True)
        r.get(url)
        print(r)

# Cookie_Util.cookie_test()

Cookie_Util.cookie_local()