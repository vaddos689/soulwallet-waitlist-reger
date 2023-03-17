from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def main(mail, number):
    email = mail[number]
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--incognito')
    options.add_argument('--disable-infobars')
    options.add_argument('--start-maximized')
    #options.add_argument('--headless')
    s = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://www.soulwallet.io/')
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/section[1]/div[1]/div[2]/input').send_keys(email)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/section[1]/div[1]/div[2]/button/span[6]').click()
    time.sleep(3)
    driver.close()
    number += 1
    with open('result.txt', 'a') as f:
        f.write(f"{email} | success\n")
    main(mail, number)


def get_data_from_file():
    f = open('mails.txt', 'r')
    i = 0
    for line in f:
        i
        i += 1
    with open("mails.txt", "r") as f:
        mail = f.read().split('\n')
        number = 0
        main(mail, number)


if __name__ == '__main__':
    get_data_from_file()