from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class NewsScraper:
    def __init__(self):
        # self.service = Service(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=self.service)
        self.driver = webdriver.Chrome(service=Service('D:/chrome-win64/chrome-win64/chromedriver.exe'))

    def fetch_news(self, url):
        self.driver.get(url)
        time.sleep(5)  # 使用显式等待更佳

        try:
            title = self.driver.find_element(By.TAG_NAME, 'h1').text
            content = self.driver.find_element(By.CLASS_NAME, 'content').text
            image = self.driver.find_element(By.TAG_NAME, 'img').get_attribute('src')

            return {
                'title': title,
                'content': content,
                'image_url': image
            }
        except Exception as e:
            return {'error': str(e)}

    def close(self):
        self.driver.quit()
