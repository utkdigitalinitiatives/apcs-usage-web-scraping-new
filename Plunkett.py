def Plunkett(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Plunkett Research
    
    # Input the URL for the main website here
    vendorURL = 'https://www.plunkettresearchonline.com/default.aspx'

    datePattern = re.compile('[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start Date must be in MM-DD-YYYY format.')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End Date must be in MM-DD-YYYY format.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    # Log into the website
    driver.get(vendorURL)
    
    
    
    # Go to the Administrator tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Header1_hideadmintab"]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="Header1_hideadmintab"]/a').click()
    except:
        raise ReferenceError('Administrator tab not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Log in using the password
    
    password = getpass.getpass('Enter the Password Here:')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="txtPassword"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="txtPassword"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="imgbtn1"]').click()
    except:
        raise ReferenceError('Login page not found. Update the XPATH.')

    print('Allowing the webpage to properly login...')
    time.sleep(10)
    
    # There are two websites that have data on them:
    
    ## eBooks Access: 
    url2 = 'https://www.plunkettresearchonline.com/AcctAdmin/StatsPRO.aspx'
    driver.get(url2)
    
    
    # Put in Date Range:
    
    ## Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="txtDateFrom"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="txtDateFrom"]').clear()
        driver.find_element(By.XPATH, '//*[@id="txtDateFrom"]').send_keys(startDate) # MM-DD-YYYY format
    except:
        raise ReferenceError('Start date box not found. Double-check the eBooks URL; if it is correct, then update the XPATH.')
    
    
    ## End Date
    try:
        driver.find_element(By.XPATH, '//*[@id="txtDateTo"]').clear()
        driver.find_element(By.XPATH, '//*[@id="txtDateTo"]').send_keys(endDate) # MM-DD-YYYY format
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')
    
    
    # Export Data:
    try:
        driver.find_element(By.XPATH, '//*[@id="btnexportByMonth"]').click()
    except: 
        raise ReferenceError('Export button not found. Update the XPATH.')
        
    time.sleep(2) #Wait before heading to next page
    
    
    
    ## Online Usage: 
    url3 = 'https://www.plunkettresearchonline.com/AcctAdmin/StatsEbooks.aspx?'
    driver.get(url3)
    
    
    # Put in Date Range:
    
    ## Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="txtDateFrom"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="txtDateFrom"]').clear()
        driver.find_element(By.XPATH, '//*[@id="txtDateFrom"]').send_keys(startDate) # MM-DD-YYYY format
    except:
        raise ReferenceError('Start date box not found. Double-check the eBooks URL; if it is correct, then update the XPATH.')
    
    
    ## End Date
    try:
        driver.find_element(By.XPATH, '//*[@id="txtDateTo"]').clear()
        driver.find_element(By.XPATH, '//*[@id="txtDateTo"]').send_keys(endDate) # MM-DD-YYYY format
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')
    
    
    # Export Data:
    try:
        driver.find_element(By.XPATH, '//*[@id="btnexport"]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')

    keyword = input('When the report appears in Downloads, type anything here to close the browser.')


    driver.close()


def Plunkett_Info():
    print('Input keys needed:')
    print('Start Date: MM-DD-YYYY format.')
    print('End Date: MM-DD-YYYY format.')
    print()
    print('The website prints two reports on separate pages. The code will automatically download both.')