def EncyclopediaBritannica(startDate, endDate):
    # Encyclopedia Britannica
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
    vendorURL = 'http://stats.eb.com'

    datePattern = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Starting date must be in the following format: MM/DD/YYYY')

    if datePattern.fullmatch(endDate) == None:
        raise SyntaxError('Ending date must be in the following format: MM/DD/YYYY')
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        driver.find_element(By.XPATH, '//*[@id="accessId"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="passcode"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="command"]/div[4]/input').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')
    
    
    
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startDate"]'))) #To ensure the webpage loads before filling out the form
    # Fill out the Report
    
    
    ## Start Date
    try:
        driver.find_element(By.XPATH, '//*[@id="startDate"]').send_keys(startDate)
    except:
        raise ReferenceError('Start Date box not found. Update the XPATH.')
    
    ## End Date
    try:
        driver.find_element(By.XPATH, '//*[@id="endDate"]').send_keys(endDate) # DD/MM/YYYY or MM/DD/YYYY are both acceptable
    except:
        raise ReferenceError('End Date box not found. Update the XPATH.')
    
    # Click on the Subscribed Product Button
    try:
        driver.find_element(By.XPATH, '//*[@id="choosenProductNames1"]').click()
    except:
        raise ReferenceError('Subscribed Product botton not found. Update the XPATH.')

    # Change to the new Report

    try:
        driver.find_element(By.XPATH, '//*[@id="includeClassicReport1"]').click()
    except:
        raise ReferenceError('New Report button not found. Update the XPATH.')
    
    # Export Report
    try:
        driver.find_element(By.XPATH, '//*[@id="form-submit-button"]').click()
    except:
        raise ReferenceError('Submit button not found. Update the XPATH.')

    
    keyword = input('When you are finished, type anything here to close the browser.')

    driver.close()

def EncyclopediaBritannica_Info():
    print('Input keys needed:')
    print('Start Date: MM/DD/YYYY format')
    print('End Date: MM/DD/YYYY format')