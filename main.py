from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://voters.eci.gov.in/login")

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
