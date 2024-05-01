from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

USER = os.getenv("USER")
print("🪪 ~ USER:", USER)
PASSWORD = os.getenv("PASSWORD")

# create chromeoptions instance
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")

chromedriver = "/usr/bin/chromedriver"
service = Service(chromedriver)
# options.set_binary("/usr/bin/brave-browser")

# provide location where chrome stores profiles
options.add_argument(r"--user-data-dir=/home/shakespear/snap/chromium/common/chromium")

# provide the profile name with which we want to open browser
options.add_argument(r"--profile-directory=Default")

# specify where your chrome driver present in your pc
driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Chrome()
print("Opening the browser")


try:
    driver.get("https://voters.eci.gov.in/login")
    user = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="loginId"]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/input[1]',
            )
        )
    )
    password = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="loginId"]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[2]/div[1]/input[1]',
            )
        )
    )
    user.send_keys(USER)
    password.send_keys(PASSWORD)
    time.sleep(60)
except Exception as e:
    print("🚀 ~ e:", e)


driver.get("https://voters.eci.gov.in/Homepage")

title = driver.title

driver.implicitly_wait(5000)


# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text


track_div = driver.find_element(
    By.XPATH,
    '//*[@id="textContent"]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div',
)
track_div.click()


# def get_reference_status(reference_number):
#     reference_input = driver.find_element(
#         By.XPATH,
#         '//*[@id="textContent"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]',
#     )

#     reference_input.send_keys(reference_number)

#     state_dropdown = driver.find_element(
#         By.XPATH,
#         '//*[@id="textContent"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/select[1]',
#     )
#     state_dropdown.find_element(By.XPATH, "//option[. = 'Maharashtra']").click()

#     button = driver.find_element(
#         By.XPATH,
#         '//*[@id="textContent"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/button[1]',
#     )
#     button.click()

#     # read the value from the XPATH //*[@id="AppHistory"]/td[9]
#     # find value of td[9] and print it
#     driver.implicitly_wait(5000)

#     track = driver.find_element(By.XPATH, '//*[@id="AppHistory"]/td[9]')
#     print(track.text)
#     return track.text


df = pd.read_csv("voter-list.csv")

# Create an empty list to store the status values
status_list = []

# create an empty list to store the EPIC values
EPIC_list = []
EXPAND_VIEW = False

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    application_no = row["APPLICATION NO"]
    Epic_no = "EPIC NOT FOUND"
    if (
        type(application_no) == str
        and application_no != "nan"
        and application_no != " "
        and str(row["APPLICATION STATUS"]).lower() != "eroll updated"
    ):
        print(type(application_no), application_no)
        # status = get_reference_status(application_no)
        # print("🚀 ~ status:", status)

        # reference_input = driver.find_element(
        #     By.XPATH,
        #     '//*[@id="textContent"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]',
        # )
        reference_input = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="textContent"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]',
                )
            )
        )
        time.sleep(1)
        reference_input.clear()
        driver.implicitly_wait(1)
        reference_input.send_keys(application_no)

        state_dropdown = driver.find_element(
            By.XPATH,
            '//*[@id="textContent"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/select[1]',
        )
        state_dropdown.find_element(By.XPATH, "//option[. = 'Maharashtra']").click()

        button = driver.find_element(
            By.XPATH,
            '//*[@id="textContent"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/button[1]',
        )
        button.click()

        # read the value from the XPATH //*[@id="AppHistory"]/td[9]
        # find value of td[9] and print it
        # driver.implicitly_wait(5000)
        time.sleep(2)
        try:
            track = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="AppHistory"]/td[9]')
                )
            )
            track = driver.find_element(By.XPATH, '//*[@id="AppHistory"]/td[9]')
            retrieved_status = track.text
            print("⏺️⏺️ ~ retrieved_status:", retrieved_status)
            status_list.append(track.text)
            # time.sleep(1)
            try:
                if retrieved_status.upper() in ("EROLL UPDATED", "EROLL_UPDATED"):
                    # expand_view_click = (
                    #     WebDriverWait(driver, 2)
                    #     .until(
                    #         EC.element_to_be_clickable(
                    #             (
                    #                 By.XPATH,
                    #                 '//*[@id="AppHistory"]/td[10]/b[1]/i[1]',
                    #             )
                    #         )
                    #     )
                    #     .click()
                    # )
                    print("✅✅ ~ retrieved_status:", retrieved_status)

                    if EXPAND_VIEW == False:

                        expand_view_click = driver.find_element(
                            By.XPATH,
                            '//*[@id="AppHistory"]/td[10]/b[1]/i[1]',
                        ).click()
                        EXPAND_VIEW = True

                    EPIC_cell = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="TA7"]'))
                    )
                    time.sleep(1)
                    EPIC = EPIC_cell.text
                    Epic_no = EPIC
                    print("🚀 ~ EPIC:", EPIC[15:])
                    # collapse_view_click = driver.find_element(
                    #     By.XPATH,
                    #     '//*[@id="AppHistory"]/td[10]/b[1]/i[1]',
                    # ).click()
                    # driver.implicitly_wait(1)
            except Exception as e:
                print("🚀 ~ e:", e)
        except Exception as e:
            EXPAND_VIEW = False
            print("🚀 ~ e:", e)
            reference_input.clear()
            status_list.append("NOT FOUND- CHECK DETAIL")
        # track = driver.find_element(By.XPATH, '//*[@id="AppHistory"]/td[9]')
        # print("🚀 ~ track:", track.text)
        # print(track.text)
        # driver.implicitly_wait(5000)
        # print("I AM HERE ALREADY")
        # status_list.append("crawl")
    elif str(row["APPLICATION STATUS"]).lower() == "eroll updated":
        # reference_input.clear()
        status_list.append("EROLL UPDATED")
    else:
        # reference_input.clear()
        status_list.append("CHECK MANUALLY")
    EPIC_list.append(Epic_no)


# Add the status list as a new column to the DataFrame
print("🚀 ~ status_list:", status_list)
df["UPDATED STATUS"] = status_list
df["EPIC NO RETRIEVED"] = EPIC_list

# Save the DataFrame back to CSV
df.to_csv("voter-list-with-status.csv", index=False)

time.sleep(2)

print("Closing the browser")

driver.quit()
