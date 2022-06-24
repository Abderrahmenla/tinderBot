from selenium import webdriver
from time import sleep


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(20)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        accept_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_btn.click()
        sleep(10)
        fb_btn.click()
        sleep(10)
        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(5)
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('your email')

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('your password')
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)
        sleep(15)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        sleep(15)
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        sleep(2)
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def auto_swipe(self):
        while True:
              try:
                  self.like()
              except:
                  sleep(2)
                  self.close_popup()

bot = TinderBot()
bot.login()
bot.auto_swipe()
