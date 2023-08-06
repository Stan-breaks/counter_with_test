import os 
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver=webdriver.Chrome()

class webpageTests(unittest.TestCase):
    def test_title(self):
        driver.get(file_uri('counter.html'))
        self.assertEqual(driver.title,'Counter')
    def test_increase(self):
        driver.get(file_uri('counter.html'))
        increase=driver.find_element(By.ID, ("add"))
        increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,'h1').text,'1')

    def test_decrease(self):
        driver.get(file_uri('counter.html'))
        decrease=driver.find_element(By.ID, ("minus"))
        decrease.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,'h1').text,'-1')
    def test_multiple_increase(self):
        driver.get(file_uri('counter.html'))
        increase=driver.find_element(By.ID, ("add"))
        for i in range(10):
            increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,'h1').text,'10')

if __name__=='__main__':
    unittest.main()