def CLCD(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    from datetime import datetime
    from selenium.webdriver.common.keys import Keys
    import getpass
    
    # Children's Literature Comprehensive Database
    
    # Input the URL for the main website here
    vendorURL = 'https://enterprise.clcd.com/#/iplogin'
    
    datePattern = re.compile('[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Starting date must be in the following format: MM/YYYY')

    if datePattern.fullmatch(endDate) == None:
        raise SyntaxError('Ending date must be in the following format: MM/YYYY')


    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-0"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="mainContent"]/app-login/form/mat-card/mat-card-content/div[4]/button[2]').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL used; if it is correct, then update the XPATH.')
    

    print('If a pop-up appears, close it. Otherwise, wait for the code to continue.')
    time.sleep(10)
    
    # Go to the Usage Statistics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/app-search/div/div[1]/app-header/div/div[1]/button[2]/span[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mainContent"]/app-search/div/div[1]/app-header/div/div[1]/button[2]/span[2]').click()
    except:
        raise ReferenceError('Header not found. Double-check the login information and update if necessary; if the login is correct, then update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-menu-panel-3"]/div/button[6]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-menu-panel-3"]/div/button[6]').click()
    except:
        raise ReferenceError('Usage Stats button not found. Update the XPATH.')
    

    # Fill out the date range:
    
    ## Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-21"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-input-21"]').click()
        for i in range(7):
            driver.find_element(By.XPATH, '//*[@id="mat-input-21"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="mat-input-21"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date input bar not found. Update the XPATH.')


    ## End Date
    try:
        driver.find_element(By.XPATH, '//*[@id="mat-input-22"]').click()
        for i in range(7):
            driver.find_element(By.XPATH, '//*[@id="mat-input-22"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="mat-input-22"]').send_keys(endDate) 
        driver.find_element(By.XPATH, '//*[@id="mat-input-22"]').send_keys(Keys.ENTER) 
    except:
        raise ReferenceError('End date input bar not found. Update the XPATH.')
        

    keyword = input('Copy the statistics shown into an Excel file. Once done, type anything here to close the browser.')

    driver.close()



def CLCD_Info():
    print('Keys needed:')
    print('Start date - MM/YYYY format.')
    print('End date - MM/YYYY format.')
    print('')
    print('The usage data will need to be manually copied into Excel after the function finishes running.')