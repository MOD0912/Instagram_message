# By MOD

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import time
while True:
    x = time.strftime('%H:%M:%S', time.localtime())
    if x == "22:03:50":                 # if you want to use a specific time, delete the next two lines and replace 22:03:50 with the time you want 
        pass                                     
    else:                               
        username = 'Your Username'    # replace it with your Instagram username
        password = 'Your Password'    # replace it with your Instagram password
        user = "user"                   # replace with the username, to wich you want to send your message
        url = 'https://instagram.com/' + user 
        Firefox = webdriver.Firefox()   # if it doesn't work add executable_path = "path to your driver"
        Firefox.maximize_window()       
        Firefox.get(url)
        try:
            bttn = Firefox.find_element(By.CLASS_NAME, 'aOOlW')
            bttn.click()
        except:
            pass
        try:
            bttn = Firefox.find_element(By.TAG_NAME, "button")
            bttn.click()
            time.sleep(0.5)
        except:
            pass
        try:
            bttn = Firefox.find_element(By.CLASS_NAME, 'L3NKy')
            time.sleep(1)
            bttn.click()
        except:
            pass
        usern = Firefox.find_element(By.NAME, "username")
        usern.send_keys(username)
        passw = Firefox.find_element(By.NAME, "password")
        passw.send_keys(password)
        passw.send_keys(Keys.RETURN)
        time.sleep(3)
        store_login_informations = Firefox.find_element(By.CLASS_NAME, "yWX7d")     
        store_login_informations.click()
        time.sleep(1)
        send_message_button = Firefox.find_element(By.CLASS_NAME, "L3NKy") 
        send_message_button.click()
        time.sleep(1)
        activate_notifications = Firefox.find_element(By.CLASS_NAME, 'HoLwm  ')
        activate_notifications.click()
        l = input("Message: ")
        mbox = Firefox.find_element(By.TAG_NAME, 'textarea')
        mbox.send_keys(l)
        mbox.send_keys(Keys.RETURN)
        Firefox.close()
