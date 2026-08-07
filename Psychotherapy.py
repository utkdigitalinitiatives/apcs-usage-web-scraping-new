def Psychotherapy(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Psychotherapy.net


    dateString = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if dateString.fullmatch(startDate) == None:
        raise SyntaxError('Start date must be in MM/DD/YYYY format.')
    elif dateString.fullmatch(endDate) == None:
        raise SyntaxError('End date must be in MM/DD/YYYY format.')

    # Input the URL for the main website here
    vendorURL = 'https://library.psychotherapy.net/account'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)


    print('If a cookies pop-up appears, close it. Otherwise, wait for the code to continue.')
    time.sleep(10)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-box"]/form/div[1]/input'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="login-box"]/form/div[1]/input').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="login-box"]/form/div[2]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login-box"]/form/div[3]/button').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')  


    # Click on the Admin tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account-nav-admin"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="account-nav-admin"]').click()
    except:
        raise ReferenceError('Admin tab not found. Update the XPATH.')


    # Input the Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="report-start-date"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="report-start-date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start Date box not found. Update the XPATH.')


    # Input the End Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="report-end-date"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="report-end-date"]').send_keys(endDate)
    except:
        raise ReferenceError('End Date box not found. Update the XPATH.')


    # Download the Statistics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account-content-admin"]/div/table[4]/tbody/tr[3]/td/button'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="account-content-admin"]/div/table[4]/tbody/tr[3]/td/button').click()
    except:
        raise ReferenceError('Download button not found. Update the XPATH.')


    keyboard = input('When the report appears in Downloads, type anything here to close the browser.')

    driver.close()



def Psychotherapy_Info():
    print('Keys needed:')
    print('Start date - MM/DD/YYYY format needed, including the slashes.')
    print('End date - Same format as the start date.')

        