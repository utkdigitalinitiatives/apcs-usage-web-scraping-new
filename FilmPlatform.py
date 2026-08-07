def FilmPlatform(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Film Platform
    
    # Input the URL for the main website here
    vendorURL = 'https://www.filmplatform.net/login/'

    
    datePattern = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(str(startDate)) == None:
        raise SyntaxError('Starting date must be in the following format: MM/DD/YYYY')

    if datePattern.fullmatch(str(endDate)) == None:
        raise SyntaxError('Starting date must be in the following format: MM/DD/YYYY')
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_1"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="input_1"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="input_2"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="cn-accept-cookie"]').click()
        driver.find_element(By.XPATH, '//*[@id="gform_submit_button_0"]').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')        
    
    # Go to the Usage Reports
    try:
        WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div[3]/div/div[1]/div[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[3]/div/div[1]/div[1]').click()
    except:
        raise ReferenceError('Usage report webpage not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/a'))) #Loading the dropdown
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/a').click()
    except:
        raise ReferenceError('Dropdown not found. Update the XPATH.')
    
    # Fill in the From Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="popupDatepicker"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="popupDatepicker"]').send_keys(str(startDate)) # MMDDYYYY format
    except:
        raise ReferenceError('From date input box not found. Update the XPATH.')
    
    # Fill in the To Date
    try:
        driver.find_element(By.XPATH, '//*[@id="popupDatepicker2"]').send_keys(endDate) # MMDDYYYY format
    except:
        raise ReferenceError('To date input box not found. Update the XPATH.')
    
    # Show the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="post-35461"]/div[2]/form/input').click()
    except:
        raise ReferenceError('Show report button not found. Update the XPATH.')


    print('Click Export List to Excel to download the usage data.')

    keyword = input('Once the data downloads, type anything here to close the browser.')


    driver.close()

def FilmPlatform_Info():
    print('Input keys needed:')
    print('Start Date: MM/DD/YYYY format')
    print('End Date: MM/DD/YYYY format')
    print('')
    print('When the report appears in the webpage, manually click on the Export List to Excel button to download.')