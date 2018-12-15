from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os
import sys
import logging#日志


class Base(object):

    def __init__(self, driver, url):
        self.driver = driver
        # self.driver=webdriver.Chrome()
        self.url = url

    def __base_open(self):
        return self.url in self.driver.current_url

    def base_open_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        # 断言
        assert self.__base_open(), "打开页面失败 %s" % self.url

    def base_find_element(self, args, timeout=30, poll=0.5):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll).until(EC.visibility_of_element_located(args))
            return self.driver.find_element(*args)
        except:
            print("%s页面中没有找到%s元素" % (self, args))

    def base_send_keys(self, args, value, first_click=True, first_clear=True):
        try:
            if first_click:
                self.base_find_element(args).send_keys(value)
            elif first_clear:
                self.base_find_element(args).clear()
                self.base_find_element(args).send_keys(value)
        except:
            print("%s页面中未找到%s元素" % (self, args))

    def base_click(self, args):
        self.base_find_element(args).click()

    def base_show_username(self, args):
        return self.base_find_element(args).text

    def base_switch_frame(self, args):
        return self.driver.switch_to.frame(args)

    def base_scripts(self, args):
        self.driver.execute_script(args)

    def base_screenhot(self):
        self.base_screen = sys._getframe(0).f_code.co_name
        self.path_screen = os.getcwd() + os.sep + "screenhot" + os.sep + (
                    self.base_screen + ("%s..jpg" % time.strftime("%Y-%m-%d %H_%M_%S")))
        self.driver.get_screenshot_as_file(self.path_screen)

    def base_logging(self):
        pass