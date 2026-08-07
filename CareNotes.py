def CareNotes():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    import pandas as pd
    import time
    import re
    import getpass
    # Merative CareNotes
    
    # Input the URL for the main website here
    vendorURL = 'https://app.amplitude.com/analytics/share/8a9e16021b9842a79831dca22a2244df'

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onenav-scroll-container"]/div/div/div[2]/div/div/div/div/div/div/div/input'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="onenav-scroll-container"]/div/div/div[2]/div/div/div/div/div/div/div/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="onenav-scroll-container"]/div/div/div[2]/div/div/button').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')        


    # Right-Click on the Usage Table

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cell-2YqeXha9"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]/div'))) #To ensure the webpage loads before filling out the form
        action = ActionChains(driver)
        action.context_click(driver.find_element(By.XPATH, '//*[@id="cell-2YqeXha9"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]/div')).perform()
    except:
        raise ReferenceError('Usage table not found. Double-check the password for login; otherwise, update the XPATH in the code. Make sure to right-click the table.')


    # Select Export
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cell-2YqeXha9"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[5]/div/div/div[8]/span[2]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="cell-2YqeXha9"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[5]/div/div/div[8]/span[2]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH in the code.')


    keyword = input('Press the CSV Export button that appears on screen to download the data. If it does not appear, click on "Export" to pop it up. When you are done, type anything here to close the browser.')

    driver.close()

def CareNotes_Info():
    print('No keys needed.')
    print('')
    print('The CSV will need to be downloaded manually as the final step.')