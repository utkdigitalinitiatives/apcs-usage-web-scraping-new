def IPA(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # IPA Source
    
    # Input the URL for the main website here
    vendorURL = 'https://www.ipasource.com/customer/account/login/'
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    if startMonth not in months:
        raise ValueError('The start month must be the full month name.')
    elif endMonth not in months:
        raise ValueError('The end month must be the full month name.')


    datePattern = re.compile('[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(str(startYear)) == None:
        raise SyntaxError('Start year must be in YYYY format.')
    elif datePattern.fullmatch(str(endYear)) == None:
        raise SyntaxError('End year must be in YYYY format.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        print('Fill out the CAPTCHA to prove this is not a robot. Yes, this does work.')
        print('The code will continue in 15 seconds. Do not press the login button; this will cause the code to break.')
        time.sleep(15)
        driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[6]/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Click on User Statistics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar"]/section/nav/ul/li[3]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="sidebar"]/section/nav/ul/li[3]/a').click()
    except:
        raise ReferenceError('User Statistics button not found. Double-check the login information; if it is correct, then update the XPATH in the code.')
    
    
    # Fill out the date dropdowns
    
    ## Each must be done individually
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select-start_month-field"]'))) #To ensure the webpage loads before trying
    
    ## Start Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="select-start_month-field"]'))
        select.select_by_visible_text(startMonth) #Full month name
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')
    
    ## Start Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="select-start_year-field"]'))
        select.select_by_visible_text(str(startYear)) #YYYY format
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')
    
    
    ## End Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="select-end_month-field"]'))
        select.select_by_visible_text(endMonth) #Full month name
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')
    
    ## End Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="select-end_year-field"]'))
        select.select_by_visible_text(str(endYear)) #YYYY format
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')
    
    
    # Generate the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="0"]/div/div/div/div/form/div/button').click()
    except:
        raise ReferenceError('Generate Report button not found. Update the XPATH.')

    keyword = input('When the report appears in Downloads, type anything here to close the browser.')


    driver.close()


def IPA_Info():
    print('Input keys needed:')
    print('Start Month: Full month name')
    print('Start year: YYYY format')
    print('End Month: Full month name')
    print('End Year: YYYY format')
    print('')
    print('The login includes a CAPTCHA that needs to be filled out manually. Filling it out manually should allow auto-login.')
