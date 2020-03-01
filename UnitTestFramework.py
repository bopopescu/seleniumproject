import unittest
from selenium import webdriver

class searchGoogle(unittest.TestCase):
    def test_google(self):
        self.driver=webdriver.Chrome(executable_path='C:\selenium\drivers\chromedriver.exe')
        self.driver.get('https://www.google.com/')
        print(self.driver.title)
        self.driver.close()

    def youtube(self):
        self.driver=webdriver.Chrome(executable_path='C:\selenium\drivers\chromedriver.exe')
        self.driver.get('https://www.youtube.com/')
        print(self.driver.title)
        self.driver.close()

if __name__ =='__main__':
    unittest.main()
