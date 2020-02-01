from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOpts


def test():
    chrome_opts = ChromeOpts()
    chrome_opts.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_opts)
    driver.get('http://wikipedia.org')
    print(driver.title)
    driver.quit()


if __name__ == '__main__':
    test()
