def Micromedex():
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
    vendorURL = 'https://app.amplitude.com/analytics/share/68358ce29dc547d9b66d9e45936e440c'

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    print('If a pop-up appears in the bottom of the screen, close it. The code will continue in a few seconds.')
    time.sleep(10)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onenav-scroll-container"]/div/div/div[2]/div/div/div/div/div/div/div/input'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="onenav-scroll-container"]/div/div/div[2]/div/div/div/div/div/div/div/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="onenav-scroll-container"]/div/div/div[2]/div/div/button').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')        


    # Right-Click on the Usage Table

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cell-tD1HtyIM"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]'))) #To ensure the webpage loads before filling out the form
        action = ActionChains(driver)
        action.context_click(driver.find_element(By.XPATH, '//*[@id="cell-tD1HtyIM"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]')).perform()
    except:
        raise ReferenceError('Usage table not found. Double-check the password for login; otherwise, update the XPATH in the code. Make sure to right-click the table.')


    # Select Export
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cell-tD1HtyIM"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[5]/div/div/div[8]/span[2]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="cell-tD1HtyIM"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[5]/div/div/div[8]/span[2]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH in the code.')


    # Select CSV Export
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cell-tD1HtyIM"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[6]/div/div/div[2]/span[2]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="cell-tD1HtyIM"]/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div[6]/div/div/div[2]/span[2]').click()
    except:
        raise ReferenceError('CSV Export button not found. Update the XPATH in the code.')




    keyword = input('When the report appears in Downloads, type anything here to close the browser.')


    driver.close()
    

def Micromedex_Info():
    print('No keys needed.')
    print('')
    print('A popup at the start will need to be manually closed.')