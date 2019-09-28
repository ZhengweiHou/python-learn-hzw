from urllib import request

class Spider():
    url = 'https://www.zhihu.com/hot'
    @classmethod
    def cookie_to_dict(cookie):
        cookie_dict={}
        items = cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            cookie_dict[key] = value
        return cookie_dict

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        print(htmls)

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


# spider = Spider()
# spider.go()



# <h2 class="HotItem-title">iPhone 为什么不加大内存？</h2>
#
# < div class ="HotItem-metrics HotItem-metrics--bottom" >
# < svg >.... < / svg >
# 3081 万热度
# < span class ="HotItem-action" > < / span >
# < / div >
