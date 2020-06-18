import time
import pickle
from selenium import webdriver


# INITIAL COOKIE LOADING
def ln_login(driver, config_file, cookies_file):
    driver.get("https://www.linkedin.com/login")
    file = open(config_file)
    lines = file.readlines()
    username = lines[0]
    password = lines[1]
    element_id = driver.find_element_by_id("username")
    element_id.send_keys(username)
    element_id = driver.find_element_by_id("password")
    element_id.send_keys(password)
    element_id.submit()
    pickle.dump(driver.get_cookies(), open(cookies_file, "wb"))


def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    url = "https://www.google.com" if url is None else url
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)


ln_url = "https://www.linkedin.com"
g_url = "https://google.com"
chrome = webdriver.Chrome()
load_cookies(chrome, "cookies.txt")
chrome.get(ln_url)
