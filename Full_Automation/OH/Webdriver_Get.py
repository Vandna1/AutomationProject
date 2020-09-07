from selenium import webdriver


class Get_chrome_driver():
    driver = None

    def launch_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(15)
        return self.driver