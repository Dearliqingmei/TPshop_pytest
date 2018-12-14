"""
    目标：统一入口类实现
    操作：
        1. 新建page_in模块
        2. 新建PageIn类
        3. 需要管理几个页面对象，就创建几个获取页面对象的方法
        4. 解决driver问题
"""

from page.page_login import *
from page.page_mall_homepage import *
from page.page_mymall import *



class PageIn():
    def page_get_pagelogin(self,driver,url):
        return Pagelogin(driver,url)

    def page_get_pagemymall(self,driver,url):
        return Pagehomepage(driver,url)

    def page_get_pagemallhomepage(self,driver,url):
        return Pagemallhomepage(driver,url)