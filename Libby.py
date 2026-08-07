def Libby(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass


    datePattern = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('The start date must be in the following format: MM/DD/YYYY')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('The to date must be in the following format: MM/DD/YYYY')



    # Input the URL for the main website here
    vendorURL = 'https://marketplace.overdrive.com/Account/Login'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)


    # Close the Cookies Tab
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dialogModalContainer"]/dialog/button'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="dialogModalContainer"]/dialog/button').click()
    except:
        raise ReferenceError('Cookies pop-up not found. If the webpage did not load properly, double-check the URL. If a pop-up did not appear on the webpage, comment out this part of the code. Otherwise, update the XPATH.')


    # Log in
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="UserName"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[4]/input').click()
    except:
        raise ReferenceError('Login webpage not found. Update the XPATH in the code.')


    # Go to the Insights tab
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="neck"]/nav/ul[1]/li[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="neck"]/nav/ul[1]/li[1]/a').click()
    except:
        raise ReferenceError('Insights tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')


    # Overall Checkouts Report 

    ## Go to Checkouts tab
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ReportsLeftNav"]/div/div[3]/ul/li[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ReportsLeftNav"]/div/div[3]/ul/li[1]/a').click()
    except:
        raise ReferenceError('Checkouts tab not found. Update the XPATH.')
    

    ## Set the Parameters for the report - Checkouts by Month
    #try:
    #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ext-comp-1009-inputEl"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="ext-comp-1009-inputEl"]').click()
    #except:
    #    raise ReferenceError('Checkouts by box not found. Update the XPATH.')
    #try:
    #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ext-153"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="ext-153"]').click()
    #except:
    #    raise ReferenceError('Month option not found. If the dropdown list did not appear, then change the first XPATH in this section of code. If the dropdown list did appear, change the second.')


    ## Set the Parameters for the report - Branch
    #try:
    #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ext-comp-1011-itemList"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="ext-comp-1011-itemList"]').click()
    #except:
    #    raise ReferenceError('Branch box not found. Update the XPATH.')
    #try:
    #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ext-156"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="ext-156"]').click()
    #except:
    #    raise ReferenceError('UT Knoxville option not found. If the dropdown list did not appear, then change the first XPATH in this section of code. If the dropdown list did appear, change the second.')


    ## Set the Parameters for the report - Change Days to Months
    #try:
    #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="combo-1025-inputEl"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="combo-1025-inputEl"]').click()
    #except:
    #    raise ReferenceError('Date type box not found. Update the XPATH.')
    #try:
    #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ext-167"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="ext-167"]').click()
    #except:
    #    raise ReferenceError('Months option not found. If the dropdown list did not appear, then change the first XPATH in this section of code. If the dropdown list did appear, change the second.')


    ## Set the Parameters for the report - Start Date
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="datefield-1027-inputEl"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="datefield-1027-inputEl"]').click()
        driver.find_element(By.XPATH, '//*[@id="datefield-1027-inputEl"]').clear()
        driver.find_element(By.XPATH, '//*[@id="datefield-1027-inputEl"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')



    ## Set the Parameters for the report - End Date
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="datefield-1028-inputEl"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="datefield-1028-inputEl"]').click()
        driver.find_element(By.XPATH, '//*[@id="datefield-1028-inputEl"]').clear()
        driver.find_element(By.XPATH, '//*[@id="datefield-1028-inputEl"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')

    ## Update the Report
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="button-1035-btnInnerEl"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="button-1035-btnInnerEl"]').click()
    except:
        raise ReferenceError('Update button not found. Update the XPATH.')



    keyword = input('The report will appear on the screen. If it needs to be downloaded, click the Create Worksheet button. When you are done, type anything here to close the browser.')

    driver.close()
    
def Libby_Info():
    print('Inputs needed:')
    print('Start Date - must be in the following format: MM/DD/YYYY')
    print('End Date - must be in the following format: MM/DD/YYYY')
