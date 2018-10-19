from nerodia.browser import Browser
from time import sleep

REDIRECT_SLEEP_SEC = 2
def login():
    username = 'chengji'
    password = ""
    browser.link(text='Log In').click()
    sleep(REDIRECT_SLEEP_SEC)
    # require 'pry'; binding.pry
    browser.text_field(name='username').set(username)
    browser.text_field(name='password').set(password)
    browser.input(class_name='twikiSubmit').click()
    sleep(REDIRECT_SLEEP_SEC)
    my_link = browser.element(text="Cheng Ji")
    print(my_link.html)

# if in the root:
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# browser = Browser(browser='chrome', options=options)
browser = Browser(browser='chrome', headless=True)
# cannot using with
# with Browser(browser='chrome', headless=False) as browser:
browser.goto("http://wiki.fortinet.com/twiki/bin/view")
login()
# browser.close()