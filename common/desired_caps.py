import yaml
import logging.config
from appium import webdriver
import os

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():

    with open('../config/kyb_caps.yaml', 'r',encoding='UTF-8') as file:
        data = yaml.load(file)

    desired_caps={}
    desired_caps['platformName']=data['platformName']

    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    desired_caps['app'] = app_path
    desired_caps['noReset']=data['noReset']

    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']

    logging.info('start run app...')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)

    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()
