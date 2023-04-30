import os, pathlib, unittest
from selenium import webdriver

driver = webdriver.Chrome()

def file_uri(file_path):
    return pathlib.Path(os.path.abspath(file_path)).as_uri()

class WebTests(unittest.TestCase):

    def test_tittle(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Count")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        inc = driver.find_element("id", "increase")
        inc.click()
        h1 = driver.find_element("tag name", "h1")
        self.assertEqual(h1.text, "1")

if __name__ == "__main__":
    unittest.main()