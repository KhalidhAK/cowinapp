from telethon import TelegramClient, events, sync
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import datetime

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 5938076
api_hash = '1bdf8b683eb39ab552332b3ac8e065bf'

client = TelegramClient('session_name', api_id, api_hash)

# @client.on(events.NewMessage(chats='testakro'))
@client.on(events.NewMessage(chats='CowinSlotsCoimbatore'))
async def my_event_handler(event):
    print('event - trigger -',datetime.datetime.now())
    if "641035" in event.raw_text:
        trigger()

def trigger():
    webpage = r"https://selfregistration.cowin.gov.in/"  # edit me
    searchterm = "7539903768"  # edit me

    chrome_options = Options()
    chrome_options.add_extension('cwn.crx')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(webpage)

    sbox = driver.find_element_by_tag_name('input')
    sbox.send_keys(searchterm)
    sbutton = driver.find_element_by_tag_name('ion-button')
    sbutton.click()
    pyautogui.click(861, 73)
    pyautogui.click(811, 199)
    time.sleep(1)
    pyautogui.click(830, 75)
    time.sleep(1)
    pyautogui.click(575, 437)
    time.sleep(1)
    pyautogui.click(565, 517)
    pyautogui.write('641035')
    pyautogui.moveTo(833, 237)
    pyautogui.scroll(-10000,833,237)
    pyautogui.click(527, 655)
    pyautogui.click(253, 519)
    flag = True
    while flag:
        time.sleep(1)
        if driver.current_url == "https://selfregistration.cowin.gov.in/dashboard":
            flag = False
            time.sleep(3)
            bookslot()

def bookslot():
    pyautogui.click(831, 551)
    time.sleep(1)
    pyautogui.click(831, 75)
    time.sleep(1)
    pyautogui.click(663, 359)
    time.sleep(1)
    pyautogui.moveTo(833, 237)
    pyautogui.scroll(-10000, 833, 237)
    pyautogui.click(527, 655)
client.start()
client.run_until_disconnected()