def MADCAD():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass

    # Input the URL for the main website here
    vendorURL = 'https://www.madcad.com/login/?loginRef=%2F'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[25]/div/div[1]/div[2]/form/div[2]/input').send_keys(username)
        driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[25]/div/div[1]/div[2]/form/div[4]/input').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[25]/div/div[1]/div[2]/form/div[6]/input').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')

    # Go to the Account Admin page
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topLayout"]/tbody/tr/td[1]/div/div/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topLayout"]/tbody/tr/td[1]/div/div/a').click()
    except:
        raise ReferenceError('Account admin button not found. Double-check the login information; if it is correct, then update the XPATH in the code.')


    # Input the Administrator Login information

    accountNumber = '122516'
    accountPIN = '87970'

    try:
        driver.find_element(By.XPATH, '//*[@id="account_number"]').send_keys(accountNumber)
        driver.find_element(By.XPATH, '//*[@id="account_pin"]').send_keys(accountPIN)
        driver.find_element(By.XPATH, '//*[@id="myAccountLogin"]/button').click()
    except:
        raise ReferenceError('Administrator Login page not found. Update the XPATH in the code.')


    # Go to Account Usage
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-5"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ui-id-5"]').click()
    except:
        raise ReferenceError('Account Usage button not found. Double-check the admin login information; if it is correct, then update the XPATH in the code.')


    # Export the Usage to CSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dataTable1"]/caption/span/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="dataTable1"]/caption/span/a').click()
    except:
        raise ReferenceError('Download as CSV button not found. Update the XPATH in the code.')

    keyword = input('When the report finishes downloading, type anything here to close the browser.')

    driver.close()



def MADCAD_Info():
    print('No input keys needed.')

    