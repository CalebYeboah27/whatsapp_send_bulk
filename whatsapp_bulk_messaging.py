# import time
import pandas as pd
import schedule as schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.chrome.options as options

# Set the Chrome WebDriver options
# this option is to allow selenium to access chrome webdriver
chrome_options = options.ChromiumOptions()
chrome_options.add_argument("--remote-allow-origins=http://127.0.0.1:28943")


Enter = '\ue007'  # code for enter key

# Read data from Excel Sheet
Data = pd.read_excel(open('contacts.xlsx', 'rb'), sheet_name='Data')
df = pd.DataFrame(Data)

Settings = pd.read_excel(open('contacts.xlsx', 'rb'), sheet_name='Settings')
setting1 = pd.DataFrame(Settings)

hour = setting1['Values'].values[0]
minutes = setting1['Values'].values[1]

# Init New Chrome instance and navigate to WebWhatsApp
chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Fit window to screen
chrome_browser.maximize_window()

# Wait 300,s
chrome_browser.implicitly_wait(300)

# Init New Chrome instance and navigate to WhatApp
chrome_browser.get('https://web.whatsapp.com/')


def send_whatsapp_message():
    for index, value in enumerate(list(df.values)):
        # get search text from worksheet
        search_text = f"+{df['Number'].values[index]}"
        # get text message from worksheet
        text_message = df['Text'].values[index]

        print(text_message, search_text)

        # find search box from browser screen using the elements XPATH
        search_box = chrome_browser.find_element(By.XPATH, "//*[@id=\"side\"]/div[1]/div/div/div[2]/div/div[1]/p")

        # click in the search box
        search_box.click()

        # wait 500ms
        chrome_browser.implicitly_wait(500)

        search_box.send_keys(search_text)

        # wait 500ms
        chrome_browser.implicitly_wait(500)

        # Press Enter to confirm the search
        search_box.send_keys(Enter)

        # wait 500ms
        chrome_browser.implicitly_wait(500)

        # find message box from browser screen using the elements XPATH
        message_box = chrome_browser.find_element(By.XPATH, "//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div["
                                                            "2]/div[1]/div/div[1]/p")
        # click in the search box
        message_box.click()

        # wait 500ms
        chrome_browser.implicitly_wait(500)

        # Load message into WebWhatsApp
        message_box.send_keys(text_message)

        # wait 500ms
        chrome_browser.implicitly_wait(500)

        # Press enter to confirm the message text
        message_box.send_keys(Enter)

        # wait 500ms
        chrome_browser.implicitly_wait(500)

        # clear search box before beginning again
        search_box.clear()
    return schedule.CancelJob


send_whatsapp_message()


# run scheduled job only once at specified time
# schedule.every().day.at(f'{hour}:{minutes}').do(send_whatsapp_message)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
