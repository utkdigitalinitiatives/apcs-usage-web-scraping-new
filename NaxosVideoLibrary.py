def NaxosVideoLibrary(startMonth, startYear, endMonth, endYear):
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
    vendorURL = 'https://www.naxosvideolibrary.com/'

    yearFormat = re.compile('[0-9][0-9][0-9][0-9]')

    if yearFormat.fullmatch(str(startYear)) == None:
        raise SyntaxError('Start Year must be in YYYY format.')
    elif yearFormat.fullmatch(str(endYear)) == None:
        raise SyntaxError('End Year must be in YYYY format.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)


    # Close the Cookies pop-up
    #try:
    #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cmpwelcomebtnsave"]/a'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="cmpwelcomebtnsave"]/a').click()
    #except:
    #    raise ReferenceError('Cookies pop-up not found. If a pop-up did not appear, then remove these lines. Otherwise, update the XPATH in the code.')    


    print('Close the cookies pop-up that appears. If one does not appear, then wait for a few seconds for the code to continue.')
    time.sleep(7)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_username"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="login_username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/header/nav[1]/ul/li/form/div[3]/button').click()
    except:
        raise ReferenceError('Login boxes not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    # Go to the Usage Statistics page
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarDropdown"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="navbarDropdown"]').click()
    except:
        raise ReferenceError('Account link not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav[1]/span[2]/ul/div/div/ul/li[3]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/nav[1]/span[2]/ul/div/div/ul/li[3]/a').click()
    except:
        raise ReferenceError('Usage Statistics button not found. Update the XPATH.')


    # Set the Date Range
    
    ## Start Date - Month
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/form/select[1]')))
        select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/select[1]'))
        select.select_by_visible_text(startMonth.upper()) # Full month name
    except:
        raise ReferenceError('Start Month dropdown not found. Double-check the URLs leading to this page; if correct, update the XPATH.')
    
    
    ## Start Date - Year
    try:
        select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/select[2]'))
        select.select_by_visible_text(str(startYear)) # YYYY format
    except:
        raise ReferenceError('Start Year dropdown not found. Update the XPATH.')
    
    
    ## End Date - Month
    try:
        select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/select[3]'))
        select.select_by_visible_text(endMonth.upper()) # Full month name
    except:
        raise ReferenceError('End Month dropdown not found. Update the XPATH.')
    
    ## End Date - Year
    try:
        select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/select[4]'))
        select.select_by_visible_text(str(endYear)) # YYYY format
    except:
        raise ReferenceError('End Year dropdown not found. Update the XPATH.')


    # Click Go
    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/input[2]').click()
    except:
        raise ReferenceError('Go button not found. Update the XPATH.')


    # Export to Excel
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lbl-ip"]')))
        driver.find_element(By.XPATH, '//*[@id="lbl-ip"]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')


    keyword = input('When the report appears in Downloads, type anything here to close the browser.')


def NaxosVideoLibrary_Info():
    print('Keys needed:')
    print('Start month - First three letters of month name only.')
    print('Start year - YYYY format.')
    print('End month - First three letters of month name only.')
    print('End year - YYYY format.')
    print('')
    print('Sometimes, the webpage will have a cookies pop-up that needs to be closed manually.')
    print('')
    print('Usage is only available in 12 month chunks maximum.')


        