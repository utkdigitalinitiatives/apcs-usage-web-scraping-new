def ReferenceUSA(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Data Axle - Reference Solutions

    # Input the URL for the main website here
    vendorURL = 'http://referenceusa.com/Account/LogOn'

    datePattern = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start date must be in MM/DD/YYYY format.')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End date must be in MM/DD/YYYY format.')
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)


    print('Press the OK button to close the pop-up box. Make sure the page is in full screen, and wait for the code to continue.')
    time.sleep(7)
        
    
    # Input the username and password, then log in
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="authenticationForm"]/fieldset/div[6]/div[2]/a').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    
    
    # Go to the Admin Page
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[4]/ul/li[2]/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[4]/ul/li[2]/a[1]').click()
    except:
        raise ReferenceError('Admin button not found. Double-check the login information; if it is correct, then update the XPATH.')
    
    
    # Click on the ICOLC Usage Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dbSelector"]/div/div[1]/div/div/div[2]/div/ul/li[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="dbSelector"]/div/div[1]/div/div/div[2]/div/ul/li[1]/a').click()
    except:
        raise ReferenceError('ICOLC Usage Report button not found. Update the XPATH.')

    print('Select "Detailed" from the Report Type dropdown that appeared.')
    time.sleep(5)
    
      
    ## Input Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fromDatePicker"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="fromDatePicker"]').clear()
        driver.find_element(By.XPATH, '//*[@id="fromDatePicker"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')

    
    ## End Date
    try:
        driver.find_element(By.XPATH, '//*[@id="toDatePicker"]').clear()
        driver.find_element(By.XPATH, '//*[@id="toDatePicker"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')
    
    
    ## Select Subtotal by Month
    
    try:
        driver.find_element(By.XPATH, '//*[@id="subtotalByMonth"]').click()
    except:
        raise ReferenceError('Subtotal by Month button not found. Update the XPATH.')

    
    # Create Report
    try:
        driver.find_element(By.XPATH, '//*[@id="btnIcolcReport"]').click()
    except:
        raise ReferenceError('Create Report button not found. Update the XPATH.')


    # Export to Excel

        
    keyword = input('Click Expor to Excel to download the report. When the report appears in Downloads, type anything here to close the browser.')


    driver.close()

def ReferenceUSA_Info():
    print('Input keys needed:')
    print('Start date - MM/DD/YYYY format.')
    print('End date - MM/DD/YYYY format.')
    print('')
    print('A pop-up box at the start must be closed manually.')
    print('The report must be downloaded manually once the code finishes running.')