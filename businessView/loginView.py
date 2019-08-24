#encoding=utf-8
from common.common_fun import Common,logging
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginView(Common):

    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')
    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    mysefl = (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username = (By.ID,'com.tal.kaoyan:id/activity_usercenter_username')
    userheader = (By.ID,'com.tal.kaoyan:id/activity_usercenter_userheader')
    rightButton = (By.ID,'com.tal.kaoyan:id/myapptitle_RightButtonWraper')
    logout = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    tip_commit = (By.ID,'com.tal.kaoyan:id/tip_commit')

    def login_before_action(self):
        try:
            self.driver.find_element(*self.mysefl)
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(*self.mysefl).click()
            self.driver.find_element(*self.userheader).click()

    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('===============login===============')
        logging.info('input username:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('input password:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn.')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished ')

    def check_account_alert(self):
        try:
            logging.info("====check account alert====")
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            element.click()
            logging.info("close account alert")

    def logout_action(self):
        logging.error("===logout action===")
        self.driver.find_element(*self.rightButton).click()
        self.driver.find_element(*self.logout).click()
        self.driver.find_element(*self.tip_commit).click()

    def check_login_status(self):
        logging.info('=====ckeck loginStatus=====')
        self.check_market_ad()
        self.check_account_alert()
        try:
            self.driver.find_element(*self.mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error("===login fail===")
            self.getScreenShot("login fail")
            return False
        else:
            logging.info("===login success===")
            self.logout_action()
            return True

if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    # l.login_before_action()
    l.login_action('自学网2018','zxw2018123')
    l.check_login_status()