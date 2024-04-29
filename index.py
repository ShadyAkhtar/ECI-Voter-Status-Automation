from selenium import webdriver

# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service

# create chromeoptions instance
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser-stable"
options.add_argument("--headless")
options.add_argument("--no-sandbox")

chromedriver = "/usr/bin/chromedriver"
service = Service(chromedriver)
# options.set_binary("/usr/bin/brave-browser")

# provide location where chrome stores profiles
options.add_argument(
    r"--user-data-dir=/home/shakespear/.config/BraveSoftware/Brave-Browser"
)

# provide the profile name with which we want to open browser
options.add_argument(r"--profile-directory=Profile 1")

# specify where your chrome driver present in your pc
driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Chrome()

driver.get("https://voters.eci.gov.in/Homepage")

title = driver.title

driver.implicitly_wait(5000)


# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

time.sleep(20)

driver.quit()
